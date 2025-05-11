import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from chat import procesar_pregunta  # Importa la nueva función del chatbot
import os

# Ruta absoluta a la carpeta CSVs
directorio_csv = os.path.join(os.path.dirname(__file__), "CSVs")

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
}

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

# Función para procesar la pregunta
def procesar_pregunta_gui():
    pregunta = entrada_pregunta.get()
    if not pregunta.strip():
        messagebox.showwarning("Advertencia", "Por favor, escribe una pregunta.")
        return

    # Procesar la pregunta con el chatbot
    respuesta, categoria, similitud = procesar_pregunta(pregunta, directorio_csv)
    if respuesta:
        salida_respuesta.config(state="normal")
        salida_respuesta.insert(tk.END, f"Tú: {pregunta}\n")
        salida_respuesta.insert(tk.END, f"Chatbot ({categoria}): {respuesta} (Similitud: {similitud:.2f}%)\n\n")
        salida_respuesta.config(state="disabled")
    else:
        salida_respuesta.config(state="normal")
        salida_respuesta.insert(tk.END, f"Tú: {pregunta}\n")
        salida_respuesta.insert(tk.END, "Chatbot: Lo siento, no entiendo tu pregunta.\n\n")
        salida_respuesta.config(state="disabled")

    entrada_pregunta.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Chatbot")
root.geometry("600x400")

# Widgets
pregunta_label = tk.Label(root, text="Escribe tu pregunta:")
pregunta_label.pack(pady=5)

entrada_pregunta = tk.Entry(root, width=80)
entrada_pregunta.pack(pady=5)

enviar_button = tk.Button(root, text="Enviar", command=procesar_pregunta_gui)
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

# Establecer el modo inicial
cambiar_modo("claro")

# Ejecutar la aplicación
root.mainloop()