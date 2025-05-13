import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from chat import procesar_pregunta  # Importamos la función procesar_pregunta desde chat.py
import os
import time
import threading
import json

# Cargar configuraciones desde config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Ruta absoluta a la carpeta CSVs
directorio_csv = config["chatbot"]["csv_directory"]

# Configuración de delay, animación y resolución
loading_delay = config["interface"]["loading_delay"]  # Tiempo entre "." y ".."
completion_delay = config["interface"]["completion_delay"]  # Tiempo antes de borrar "Cargando completado."
loading_animation_enabled = config["interface"]["loading_animation"]
loading_cycles = config["interface"]["loading_cycles"]  # Cantidad de ciclos de "Cargando..."
resolution = config["interface"]["resolution"]  # Resolución de la ventana

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

# Función para procesar la pregunta con delay
def procesar_pregunta_con_delay():
    pregunta = entrada_pregunta.get()
    if not pregunta.strip():
        messagebox.showwarning("Advertencia", "Por favor, escribe una pregunta.")
        return

    # Variables compartidas entre hilos
    respuesta_event = threading.Event()  # Evento para indicar que la respuesta está lista
    respuesta_data = {"respuesta": None, "categoria": None, "similitud": None}  # Almacena la respuesta del chatbot

    # Hilo para procesar la pregunta
    def procesar_pregunta_en_hilo():
        respuesta, categoria, similitud = procesar_pregunta(pregunta, directorio_csv)
        respuesta_data["respuesta"] = respuesta
        respuesta_data["categoria"] = categoria
        respuesta_data["similitud"] = similitud
        respuesta_event.set()  # Indicar que la respuesta está lista

    # Hilo para mostrar la animación de carga
    def animar_y_responder():
        salida_respuesta.config(state="normal")
        salida_respuesta.insert(tk.END, f"Tú: {pregunta}\n")
        salida_respuesta.config(state="disabled")

        # Mostrar animación de carga
        mostrar_cargando()

        # Esperar a que la respuesta esté lista si aún no lo está
        respuesta_event.wait()

        # Mostrar la respuesta cuando esté lista
        salida_respuesta.config(state="normal")
        if respuesta_data["respuesta"]:
            salida_respuesta.insert(
                tk.END,
                f"Chatbot ({respuesta_data['categoria']}): {respuesta_data['respuesta']} (Similitud: {respuesta_data['similitud']:.2f}%)\n\n",
            )
        else:
            salida_respuesta.insert(tk.END, "Chatbot: Lo siento, no entiendo tu pregunta.\n\n")
        salida_respuesta.config(state="disabled")

        entrada_pregunta.delete(0, tk.END)

    # Crear y ejecutar los hilos
    threading.Thread(target=procesar_pregunta_en_hilo).start()
    threading.Thread(target=animar_y_responder).start()

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