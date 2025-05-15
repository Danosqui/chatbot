import flet as ft
import json
import threading
import time
from chat import procesar_pregunta

# Cargar configuraciones desde config.json
def cargar_config():
    with open("config.json", "r") as config_file:
        return json.load(config_file)

config = cargar_config()

# Globales desde config
def aplicar_config():
    global directorio_csv, loading_delay, completion_delay, loading_animation_enabled, loading_cycles, resolution, default_mode
    directorio_csv = config["chatbot"]["csv_directory"]
    loading_delay = config["interface"]["loading_delay"]
    completion_delay = config["interface"]["completion_delay"]
    loading_animation_enabled = config["interface"]["loading_animation"]
    loading_cycles = config["interface"]["loading_cycles"]
    resolution = config["interface"]["resolution"]
    default_mode = config["interface"]["default_mode"]

aplicar_config()

# Colores para los modos
MODOS = {
    "claro": {
        "bg": "#ffffff",
        "fg": "#000000",
    },
    "oscuro": {
        "bg": "#2e2e2e",
        "fg": "#ffffff",
    },
    "protanopia": {
        "bg": "#fdf6e3",
        "fg": "#073642",
    },
    "deuteranopia": {
        "bg": "#fdf6e3",
        "fg": "#002b36",
    },
}

# Guardar configuración en tiempo real
def guardar_config():
    with open("config.json", "w") as config_file:
        json.dump(config, config_file, indent=4)


def main(page: ft.Page):

    dlg = ft.AlertDialog(
        title=ft.Text("Hello"),
        content=ft.Text("You are notified!"),
        alignment=ft.alignment.center,
        on_dismiss=lambda e: print("Dialog dismissed!"),
        title_padding=ft.padding.all(25),
    )
    page.add(
        ft.ElevatedButton("Open dialog", on_click=lambda e: page.open(dlg)),
    )

    aplicar_config()
    page.title = "Chatbot Flet UI"
    page.window_width, page.window_height = map(int, resolution.split("x"))
    page.scroll = ft.ScrollMode.AUTO

    # Aplicar el modo inicial desde la configuración
    colores = MODOS[default_mode]
    page.bgcolor = colores["bg"]
    page.color = colores["fg"]
    page.theme_mode = ft.ThemeMode.DARK if default_mode == "oscuro" else ft.ThemeMode.LIGHT

    entrada_pregunta = ft.TextField(label="Escribe tu pregunta", expand=True)
    salida_respuesta = ft.TextField(multiline=True, read_only=True, min_lines=10, expand=True)
    boton_enviar = ft.ElevatedButton("Enviar", disabled=False)

    # Estilo CSS para cambiar el cursor cuando el botón está deshabilitado
    page.styles = {
        "button:disabled": {
            "cursor": "not-allowed",
        }
    }

    def mostrar_respuesta(respuesta, categoria, similitud, tiempo_ms):
        salida_respuesta.value += f"\nChatbot ({categoria}): {respuesta} (Similitud: {similitud:.2f}%) [{tiempo_ms} ms]\n"
        page.update()

    def mostrar_cargando():
        if not loading_animation_enabled:
            return
        cargando_tag = len(salida_respuesta.value)
        for ciclo in range(loading_cycles):
            for puntos in [".", "..", "..."]:
                salida_respuesta.value = salida_respuesta.value[:cargando_tag] + f"Chatbot: Cargando{puntos}\n"
                page.update()
                time.sleep(loading_delay)
        salida_respuesta.value = salida_respuesta.value[:cargando_tag] + "Chatbot: Cargando completado.\n"
        page.update()
        time.sleep(completion_delay)

    def manejar_pregunta(e):
        pregunta = entrada_pregunta.value.strip()
        if not pregunta:
            return

        # Bloquear el campo de entrada y el botón de enviar
        entrada_pregunta.disabled = True
        boton_enviar.disabled = True
        page.update()

        salida_respuesta.value += f"\nTú: {pregunta}\n"
        entrada_pregunta.value = ""
        page.update()

        def hilo_chat():
            inicio = time.perf_counter()
            respuesta, categoria, similitud, tiempo_ms = procesar_pregunta(pregunta, directorio_csv)
            if loading_animation_enabled:
                mostrar_cargando()
            if respuesta:
                mostrar_respuesta(respuesta, categoria, similitud, tiempo_ms)
            else:
                salida_respuesta.value += f"\nChatbot: Lo siento, no entiendo tu pregunta. [{tiempo_ms} ms]\n"
                page.update()

            # Habilitar el campo de entrada y el botón de enviar nuevamente
            entrada_pregunta.disabled = False
            boton_enviar.disabled = False
            page.update()

        threading.Thread(target=hilo_chat).start()

    def cambiar_modo(modo):
        config["interface"]["default_mode"] = modo
        guardar_config()
        aplicar_config()
        colores = MODOS[modo]
        page.bgcolor = colores["bg"]
        page.color = colores["fg"]
        page.theme_mode = ft.ThemeMode.DARK if modo == "oscuro" else ft.ThemeMode.LIGHT
        page.update()

    def abrir_config_modal(e):
        campos = []

        def guardar_nueva_config(e):
            try:
                for campo in campos:
                    secciones = campo["key"].split(".")
                    valor = campo["entrada"].value
                    obj = config
                    for k in secciones[:-1]:
                        obj = obj[k]
                    clave_final = secciones[-1]
                    # Validar y convertir el valor ingresado
                    if valor.lower() in ["true", "false"]:
                        obj[clave_final] = valor.lower() == "true"
                    elif valor.replace('.', '', 1).isdigit():
                        obj[clave_final] = float(valor) if '.' in valor else int(valor)
                    else:
                        obj[clave_final] = valor
                # Guardar la configuración y aplicar los cambios
                guardar_config()
                aplicar_config()
                page.window_width, page.window_height = map(int, resolution.split("x"))
                colores = MODOS[default_mode]
                page.bgcolor = colores["bg"]
                page.color = colores["fg"]
                page.theme_mode = ft.ThemeMode.DARK if default_mode == "oscuro" else ft.ThemeMode.LIGHT
                dlg.open = False
                page.snack_bar = ft.SnackBar(ft.Text("Configuración guardada con éxito."), open=True)
                page.update()
            except Exception as ex:
                page.snack_bar = ft.SnackBar(ft.Text(f"Error al guardar configuración: {ex}"), open=True)
                page.update()

        contenido = []
        for seccion, datos in config.items():
            if isinstance(datos, dict):
                for clave, valor in datos.items():
                    key_path = f"{seccion}.{clave}"
                    entrada = ft.TextField(label=key_path, value=str(valor))
                    campos.append({"key": key_path, "entrada": entrada})
                    contenido.append(entrada)

        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Editar Configuración"),
            content=ft.Container(
                content=ft.Column(contenido, scroll=ft.ScrollMode.ADAPTIVE),
                padding=ft.padding.all(10),
            ),
            actions=[
                ft.TextButton("Guardar", on_click=guardar_nueva_config),
                ft.TextButton("Cancelar", on_click=lambda e: setattr(dlg, "open", False))
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )

        # Asignar el modal a la página y abrirlo
        page.dialog = dlg
        page.open(dlg)
        page.update()

    boton_config = ft.ElevatedButton("⚙ Configurar", on_click=abrir_config_modal)
    botones_modo = ft.Row([
        ft.ElevatedButton("Claro", on_click=lambda e: cambiar_modo("claro")),
        ft.ElevatedButton("Oscuro", on_click=lambda e: cambiar_modo("oscuro")),
        ft.ElevatedButton("Protanopia", on_click=lambda e: cambiar_modo("protanopia")),
        ft.ElevatedButton("Deuteranopia", on_click=lambda e: cambiar_modo("deuteranopia"))
    ], alignment=ft.MainAxisAlignment.CENTER)

    boton_enviar.on_click = manejar_pregunta
    entrada_pregunta.on_submit = manejar_pregunta  # Permitir enviar con Enter

    page.add(
        entrada_pregunta,
        boton_enviar,
        salida_respuesta,
        ft.Divider(),
        botones_modo,
        boton_config
    )

ft.app(target=main)