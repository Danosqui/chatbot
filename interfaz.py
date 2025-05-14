import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from chat import procesar_pregunta  # Importamos la función procesar_pregunta desde chat.py
import os
import time
import threading
import json

# Cargar configuraciones desde config.json
def cargar_config():
    with open("config.json", "r") as config_file:
        return json.load(config_file)

config = cargar_config()

# Ruta absoluta a la carpeta CSVs
directorio_csv = config["chatbot"]["csv_directory"]

# Configuración de delay, animación y resolución
def aplicar_config():
    global loading_delay, completion_delay, loading_animation_enabled, loading_cycles, resolution
    loading_delay = config["interface"]["loading_delay"]
    completion_delay = config["interface"]["completion_delay"]
    loading_animation_enabled = config["interface"]["loading_animation"]
    loading_cycles = config["interface"]["loading_cycles"]
    resolution = config["interface"]["resolution"]

aplicar_config()

# Colores para los modos
MODOS = {
    "claro": {
        "bg": "#ffffff",
        "fg": "#000000",
        "entry_bg": "#f0f0f0",
        "entry_fg": "#000000",
        "button_bg": "#e0e0e0",
        "button_fg": "#000000",
    },
    "oscuro": {
        "bg": "#2e2e2e",
        "fg": "#ffffff",
        "entry_bg": "#3e3e3e",
        "entry_fg": "#ffffff",
        "button_bg": "#5e5e5e",
        "button_fg": "#ffffff",
    },
    "protanopia": {
        "bg": "#fdf6e3",
        "fg": "#073642",
        "entry_bg": "#eee8d5",
        "entry_fg": "#073642",
        "button_bg": "#93a1a1",
        "button_fg": "#073642",
    },
    "deuteranopia": {
        "bg": "#fdf6e3",
        "fg": "#002b36",
        "entry_bg": "#eee8d5",
        "entry_fg": "#002b36",
        "button_bg": "#839496",
        "button_fg": "#002b36",
    },
}

# Variable global para controlar si el chatbot está ocupado
chatbot_ocupado = False

# Función para guardar configuraciones en config.json
def guardar_configuracion(clave, valor):
    config["interface"][clave] = valor
    with open("config.json", "w") as config_file:
        json.dump(config, config_file, indent=4)

# Función para cambiar el modo
def cambiar_modo(modo):
    colores = MODOS[modo]
    root.config(bg=colores["bg"])
    pregunta_label.config(bg=colores["bg"], fg=colores["fg"])
    respuesta_label.config(bg=colores["bg"], fg=colores["fg"])
    entrada_pregunta.config(bg=colores["entry_bg"], fg=colores["entry_fg"])
    salida_respuesta.config(bg=colores["entry_bg"], fg=colores["entry_fg"])
    enviar_button.config(bg=colores["button_bg"], fg=colores["button_fg"])
    modo_claro_button.config(bg=colores["button_bg"], fg=colores["button_fg"])
    modo_oscuro_button.config(bg=colores["button_bg"], fg=colores["button_fg"])
    protanopia_button.config(bg=colores["button_bg"], fg=colores["button_fg"])
    deuteranopia_button.config(bg=colores["button_bg"], fg=colores["button_fg"])
    config_button.config(bg=colores["button_bg"], fg=colores["button_fg"])
    guardar_configuracion("default_mode", modo)  # Guardar el modo seleccionado en config.json

# Función para mostrar puntos suspensivos de carga en el historial
def mostrar_cargando():
    if not loading_animation_enabled:
        return
    salida_respuesta.config(state="normal")
    cargando_tag = salida_respuesta.index("end-1c")  # Guardar la posición inicial del texto "Cargando"
    salida_respuesta.insert(tk.END, "Chatbot: Cargando.\n")
    for ciclo in range(loading_cycles):  # Repetir la cantidad de ciclos configurada
        for puntos in [".", "..", "..."]:
            salida_respuesta.delete(cargando_tag, "end-1c")  # Eliminar el texto anterior de "Cargando"
            salida_respuesta.insert(tk.END, f"Chatbot: Cargando{puntos}\n")
            salida_respuesta.update()
            time.sleep(loading_delay)  # Usar el delay configurado en config.json
    salida_respuesta.delete(cargando_tag, "end-1c")  # Eliminar el texto de "Cargando" al finalizar
    salida_respuesta.insert(tk.END, "Chatbot: Cargando completado.\n")
    salida_respuesta.update()
    time.sleep(completion_delay)  # Esperar antes de borrar "Cargando completado."
    salida_respuesta.delete("end-2l", "end-1c")  # Borrar "Cargando completado."

# Función para procesar la pregunta con delay y control de botón/enviar
def procesar_pregunta_con_delay():
    global chatbot_ocupado
    if chatbot_ocupado:
        messagebox.showinfo("Chatbot ocupado", "El chatbot está trabajando. Por favor, espera la respuesta.")
        return

    pregunta = entrada_pregunta.get()
    if not pregunta.strip():
        messagebox.showwarning("Advertencia", "Por favor, escribe una pregunta.")
        return

    # Borrar el input al instante
    entrada_pregunta.delete(0, tk.END)
    # Deshabilitar el botón de enviar
    enviar_button.config(state="disabled")
    chatbot_ocupado = True

    # Variables compartidas entre hilos
    respuesta_event = threading.Event()  # Evento para indicar que la respuesta está lista
    respuesta_data = {"respuesta": None, "categoria": None, "similitud": None, "tiempo_ms": None}  # Almacena la respuesta del chatbot

    # Hilo para procesar la pregunta
    def procesar_pregunta_en_hilo():
        tiempo_inicio = time.perf_counter()
        respuesta, categoria, similitud = procesar_pregunta(pregunta, config["chatbot"]["csv_directory"])
        tiempo_fin = time.perf_counter()
        respuesta_data["respuesta"] = respuesta
        respuesta_data["categoria"] = categoria
        respuesta_data["similitud"] = similitud
        respuesta_data["tiempo_ms"] = int((tiempo_fin - tiempo_inicio) * 1000)
        respuesta_event.set()  # Indicar que la respuesta está lista

    # Hilo para mostrar la animación de carga y la respuesta
    def animar_y_responder():
        salida_respuesta.config(state="normal")
        salida_respuesta.insert(tk.END, f"Tú: {pregunta}\n")
        salida_respuesta.config(state="disabled")

        if loading_animation_enabled:
            mostrar_cargando()
            respuesta_event.wait()
        else:
            respuesta_event.wait()

        salida_respuesta.config(state="normal")
        if respuesta_data["respuesta"]:
            salida_respuesta.insert(
                tk.END,
                f"Chatbot ({respuesta_data['categoria']}): {respuesta_data['respuesta']} (Similitud: {respuesta_data['similitud']:.2f}%) [{respuesta_data['tiempo_ms']} ms de respuesta]\n\n",
            )
        else:
            salida_respuesta.insert(tk.END, "Chatbot: Lo siento, no entiendo tu pregunta.\n\n")
        salida_respuesta.config(state="disabled")

        # Habilitar el botón de enviar nuevamente
        enviar_button.config(state="normal")
        global chatbot_ocupado
        chatbot_ocupado = False

    # Crear y ejecutar los hilos
    threading.Thread(target=procesar_pregunta_en_hilo).start()
    threading.Thread(target=animar_y_responder).start()

# --------- Pantalla de configuración de config.json ---------
def abrir_configuracion():
    config_window = tk.Toplevel(root)
    config_window.title("Configuración")
    config_window.geometry("400x500")
    config_window.grab_set()

    # Copia de la configuración actual para edición
    config_edit = json.loads(json.dumps(config))

    # Crear widgets para cada parámetro configurable
    row = 0
    entries = {}

    def add_entry(label, key_path, tipo="str", opciones=None):
        nonlocal row
        tk.Label(config_window, text=label).grid(row=row, column=0, sticky="w", padx=5, pady=5)
        valor = config_edit
        for k in key_path[:-1]:
            valor = valor[k]
        if opciones:
            var = tk.StringVar(value=str(valor[key_path[-1]]))
            entry = ttk.Combobox(config_window, textvariable=var, values=opciones, state="readonly", width=27)
        else:
            var = tk.StringVar(value=str(valor[key_path[-1]]))
            entry = tk.Entry(config_window, textvariable=var, width=30)
        entry.grid(row=row, column=1, padx=5, pady=5)
        entries[tuple(key_path)] = (var, tipo, opciones)
        row += 1

    # Parámetros editables
    add_entry("Directorio CSV", ["chatbot", "csv_directory"])
    add_entry("Umbral de similitud", ["chatbot", "default_similarity_threshold"], "int")
    add_entry("Guardar preguntas sin responder", ["chatbot", "save_unanswered_questions"], opciones=["True", "False"])
    add_entry("Archivo de preguntas sin responder", ["chatbot", "unanswered_questions_file"])
    add_entry("Tema por defecto", ["interface", "default_theme"])
    add_entry("Modo por defecto", ["interface", "default_mode"])
    add_entry("Delay de carga (s)", ["interface", "loading_delay"], "float")
    add_entry("Delay de finalización (s)", ["interface", "completion_delay"], "float")
    add_entry("Animación de carga", ["interface", "loading_animation"], opciones=["True", "False"])
    add_entry("Ciclos de carga", ["interface", "loading_cycles"], "int")
    add_entry("Resolución", ["interface", "resolution"])

    # Botones de guardar/cancelar
    def guardar_cambios():
        try:
            for key_path, (var, tipo, opciones) in entries.items():
                valor = var.get()
                # Validación de tipo
                if tipo == "int":
                    if not valor.isdigit():
                        raise ValueError(f"El valor '{valor}' para {key_path[-1]} debe ser un número entero.")
                    valor = int(valor)
                elif tipo == "float":
                    try:
                        valor = float(valor)
                    except ValueError:
                        raise ValueError(f"El valor '{valor}' para {key_path[-1]} debe ser un número decimal.")
                elif opciones:
                    if valor not in opciones:
                        raise ValueError(f"El valor '{valor}' para {key_path[-1]} debe ser una de las opciones: {opciones}.")
                    valor = True if valor == "True" else False
                # Asignar valor en la copia de config
                d = config_edit
                for k in key_path[:-1]:
                    d = d[k]
                d[key_path[-1]] = valor
            # Guardar en archivo
            with open("config.json", "w") as f:
                json.dump(config_edit, f, indent=4)
            # Aplicar cambios en caliente
            global config
            config = cargar_config()
            aplicar_config()
            # Cambiar modo y resolución si corresponde
            cambiar_modo(config["interface"]["default_mode"])
            root.geometry(config["interface"]["resolution"])
            messagebox.showinfo("Configuración", "¡Configuración guardada y aplicada correctamente!")
            config_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar configuración: {e}")

    def cancelar_cambios():
        config_window.destroy()

    guardar_btn = tk.Button(config_window, text="Guardar", command=guardar_cambios)
    guardar_btn.grid(row=row, column=0, padx=5, pady=20)
    cancelar_btn = tk.Button(config_window, text="Cancelar", command=cancelar_cambios)
    cancelar_btn.grid(row=row, column=1, padx=5, pady=20)

# Crear la ventana principal
root = tk.Tk()
root.title("Chatbot")
root.geometry(resolution)  # Usar la resolución configurada en config.json

# Widgets
pregunta_label = tk.Label(root, text="Escribe tu pregunta:")
pregunta_label.pack(pady=5)

entrada_pregunta = tk.Entry(root, width=80)
entrada_pregunta.pack(pady=5)

enviar_button = tk.Button(root, text="Enviar", command=procesar_pregunta_con_delay)
enviar_button.pack(pady=5)

respuesta_label = tk.Label(root, text="Respuestas:")
respuesta_label.pack(pady=5)

salida_respuesta = tk.Text(root, width=80, height=15, state="disabled")
salida_respuesta.pack(pady=5)

# Botón para abrir configuración
config_button = tk.Button(root, text="Configuración", command=abrir_configuracion)
config_button.pack(pady=5)

# Botones para cambiar el modo
modo_claro_button = tk.Button(root, text="Modo Claro", command=lambda: cambiar_modo("claro"))
modo_claro_button.pack(side="left", padx=5, pady=5)

modo_oscuro_button = tk.Button(root, text="Modo Oscuro", command=lambda: cambiar_modo("oscuro"))
modo_oscuro_button.pack(side="left", padx=5, pady=5)

protanopia_button = tk.Button(root, text="Protanopia", command=lambda: cambiar_modo("protanopia"))
protanopia_button.pack(side="left", padx=5, pady=5)

deuteranopia_button = tk.Button(root, text="Deuteranopia", command=lambda: cambiar_modo("deuteranopia"))
deuteranopia_button.pack(side="left", padx=5, pady=5)

# Establecer el modo inicial
cambiar_modo(config["interface"]["default_mode"])

# Ejecutar la aplicación
root.mainloop()