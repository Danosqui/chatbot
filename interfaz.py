import flet as ft
import json
import threading
import time
import os
from chat import (
    procesar_pregunta,
    procesar_comando_ayuda,
    procesar_comando_info,
    getCategorias,
    cargarPregunta,
    crear_categoria,
)

def cargar_config():
    with open("config.json", "r") as config_file:
        return json.load(config_file)

config = cargar_config()

def aplicar_config():
    global directorio_csv, loading_delay, completion_delay, loading_animation_enabled, loading_cycles, resolution, default_mode, chatbot_name
    directorio_csv = config["chatbot"]["csv_directory"]
    loading_delay = config["interface"]["loading_delay"]
    completion_delay = config["interface"]["completion_delay"]
    loading_animation_enabled = config["interface"]["loading_animation"]
    loading_cycles = config["interface"]["loading_cycles"]
    resolution = config["interface"]["resolution"]
    default_mode = config["interface"]["default_mode"]
    chatbot_name = config["chatbot"]["chatbot_name"]

aplicar_config()

MODOS = {
    "claro": {
        "bg": "#ffffff",
        "fg": "#000000",
        "bot": "#333333"
    },
    "oscuro": {
        "bg": "#2e2e2e",
        "fg": "#ffffff",
        "bot": "#ffffff"
    },
    "protanopia": {
        "bg": "#fdf6e3",
        "fg": "#073642",
        "bot": "#073642"
    },
    "deuteranopia": {
        "bg": "#fdf6e3",
        "fg": "#002b36",
        "bot": "#002b36"
    },
}

def guardar_config():
    with open("config.json", "w") as config_file:
        json.dump(config, config_file, indent=4)

def cambiar_nombre_chatbot(nuevo_nombre):
    config["chatbot"]["chatbot_name"] = nuevo_nombre
    guardar_config()
    aplicar_config()

def main(page: ft.Page):
    aplicar_config()
    page.title = "Pokedexnou"
    page.window_width, page.window_height = map(int, resolution.split("x"))
    page.scroll = ft.ScrollMode.AUTO

    colores = MODOS[default_mode]
    page.bgcolor = colores["bg"]
    page.color = colores["fg"]
    page.theme_mode = ft.ThemeMode.DARK if default_mode == "oscuro" else ft.ThemeMode.LIGHT

    entrada_pregunta = ft.TextField(label="Escribe tu pregunta", expand=True)
    salida_respuesta = ft.ListView(
        expand=True,
        spacing=5,
        auto_scroll=True,
        height=400,
    )
    boton_enviar = ft.ElevatedButton("Enviar", disabled=False)

    page.styles = {
        "button:disabled": {
            "cursor": "not-allowed",
        }
    }

    mensajes = []

    def renderizar_mensajes():
        salida_respuesta.controls.clear()
        color_bot = MODOS[default_mode]["bot"]
        bg_usuario = "#e3f2fd"
        bg_bot = "#424242" if default_mode == "oscuro" else "#f1f1f1"
        for texto, es_usuario in mensajes:
            salida_respuesta.controls.append(
                ft.Row(
                    [
                        ft.Container(
                            ft.Text(
                                texto,
                                text_align="right" if es_usuario else "left",
                                style=ft.TextThemeStyle.BODY_LARGE,
                                color="#2196F3" if es_usuario else color_bot,

                                # no_wrap=False,
                                # max_lines=None,  
                                #No voy a mentir a nadie, NO SE PARA QUE SIRVEN REALMENTE
                                # Las 2 lineas comentadas de abajo hacen lo que necesitaba y creí que estas servirían

                                overflow=ft.TextOverflow.VISIBLE,  # flet bendiga esta linea
                            ),
                            bgcolor=bg_usuario if es_usuario else bg_bot,
                            padding=10,
                            border_radius=20,
                            alignment=ft.alignment.center_right if es_usuario else ft.alignment.center_left,
                            margin=ft.margin.only(left=40) if es_usuario else ft.margin.only(right=40),
                            expand=False if es_usuario else True, # Ajusta el ancho del contenedor dependiendo quien es el que escribe
                        )
                    ],
                    alignment=ft.MainAxisAlignment.END if es_usuario else ft.MainAxisAlignment.START,
                )
            )
        page.update()

    def agregar_mensaje(texto, es_usuario=False):
        mensajes.append((texto, es_usuario))
        renderizar_mensajes()

    def mostrar_respuesta(respuesta, categoria, similitud, tiempo_ms):
        agregar_mensaje(
            f"{chatbot_name} ({categoria}): {respuesta} (Similitud: {similitud:.2f}%) [{tiempo_ms} ms]",
            es_usuario=False
        )

    def mostrar_cargando():
        if not config["interface"]["loading_animation"]:
            return
        cargando_tag = len(mensajes)
        for ciclo in range(loading_cycles):
            for puntos in [".", "..", "..."]:
                if len(mensajes) > cargando_tag:
                    mensajes.pop()
                mensajes.append((f"{chatbot_name}: Cargando{puntos}", False))
                renderizar_mensajes()
                time.sleep(loading_delay)
        if len(mensajes) > cargando_tag:
            mensajes.pop()
        mensajes.append((f"{chatbot_name}: Cargando completado.", False))
        renderizar_mensajes()
        time.sleep(completion_delay)
        if len(mensajes) > cargando_tag:
            mensajes.pop()
        renderizar_mensajes()

    def manejar_pregunta(e):
        pregunta = entrada_pregunta.value.strip()
        if not pregunta:
            return
        entrada_pregunta.disabled = True
        boton_enviar.disabled = True
        page.update()
        agregar_mensaje(f"Tú: {pregunta}", es_usuario=True)
        entrada_pregunta.value = ""
        page.update()
        def hilo_chat():
            if pregunta.startswith("/ayuda"):
                respuesta = procesar_comando_ayuda()
                agregar_mensaje(f"Chatbot: {respuesta}", es_usuario=False)
            elif pregunta.startswith("/info"):
                respuesta = procesar_comando_info()
                agregar_mensaje(f"Chatbot: {respuesta}", es_usuario=False)
            elif pregunta.lower().startswith("/categoria"):
                # Permite crear categoría desde la interfaz con /categoria
                partes = pregunta.split(maxsplit=2)
                if len(partes) >= 2:
                    nombre = partes[1]
                    tipo = partes[2] if len(partes) > 2 and partes[2].lower() in ["csv", "json"] else "csv"
                    exito, mensaje = crear_categoria(directorio_csv, nombre, tipo)
                    agregar_mensaje(f"Chatbot: {mensaje}", es_usuario=False)
                else:
                    agregar_mensaje("Chatbot: Uso: /categoria <nombre> [csv|json]", es_usuario=False)
            else:
                inicio = time.perf_counter()
                respuesta, categoria, similitud, tiempo_ms = procesar_pregunta(pregunta, directorio_csv)
                if config["interface"]["loading_animation"]:
                    mostrar_cargando()
                if respuesta:
                    mostrar_respuesta(respuesta, categoria, similitud, tiempo_ms)
                else:
                    agregar_mensaje(f"Chatbot: Lo siento, no entiendo tu pregunta. [{tiempo_ms} ms]", es_usuario=False)
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
        renderizar_mensajes()
        page.update()

    def abrir_config_modal(e):
        campos = []
        def guardar_nueva_config(e):
            try:
                for campo in campos:
                    secciones = campo["key"].split(".")
                    valor = campo["entrada"].value if isinstance(campo["entrada"], ft.TextField) else campo["entrada"].value
                    obj = config
                    for k in secciones[:-1]:
                        obj = obj[k]
                    clave_final = secciones[-1]
                    if isinstance(campo["entrada"], ft.Dropdown):
                        if valor in ["true", "false"]:
                            obj[clave_final] = valor == "true"
                        else:
                            obj[clave_final] = valor
                    elif isinstance(campo["entrada"], ft.TextField) and valor.lower() in ["true", "false"]:
                        obj[clave_final] = valor.lower() == "true"
                    elif valor.replace('.', '', 1).isdigit():
                        obj[clave_final] = float(valor) if '.' in valor else int(valor)
                    else:
                        obj[clave_final] = valor
                guardar_config()
                aplicar_config()
                page.window_width, page.window_height = map(int, resolution.split("x"))
                colores = MODOS[default_mode]
                page.bgcolor = colores["bg"]
                page.color = colores["fg"]
                dlg.open = False
                renderizar_mensajes()
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
                    if isinstance(valor, bool) or key_path == "interface.loading_animation":
                        entrada = ft.Dropdown(
                            label=key_path,
                            value=str(valor).lower(),
                            options=[
                                ft.dropdown.Option("true"),
                                ft.dropdown.Option("false"),
                            ],
                        )
                    elif key_path == "interface.default_mode":
                        entrada = ft.Dropdown(
                            label=key_path,
                            value=valor,
                            options=[
                                ft.dropdown.Option(modo) for modo in MODOS.keys()
                            ],
                        )
                    else:
                        entrada = ft.TextField(label=key_path, value=str(valor))
                    campos.append({"key": key_path, "entrada": entrada})
                    contenido.append(entrada)
        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Editar Configuración"),
            content=ft.Container(
                content=ft.Column(contenido, scroll=ft.ScrollMode.ADAPTIVE),
                padding=ft.padding.all(10),
                width=600,
                height=500,
            ),
            actions=[
                ft.TextButton("Guardar", on_click=guardar_nueva_config),
                ft.TextButton("Cancelar", on_click=lambda e: (setattr(dlg, "open", False), page.update())),
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )
        page.dialog = dlg
        page.open(dlg)
        page.update()

    def abrir_cargar_categoria_modal(e):
        entrada_nombre = ft.TextField(label="Nombre de la categoría")
        dropdown_tipo = ft.Dropdown(
            label="Tipo de archivo",
            value="csv",
            options=[
                ft.dropdown.Option("csv"),
                ft.dropdown.Option("json"),
            ],
        )
        def guardar_categoria(ev):
            nombre = entrada_nombre.value.strip()
            tipo = dropdown_tipo.value
            if not nombre:
                page.snack_bar = ft.SnackBar(ft.Text("El nombre no puede estar vacío."), open=True)
                page.update()
                return
            archivos = [f.lower() for f in os.listdir(directorio_csv)]
            nombre_archivo = f"{nombre.lower()}.{tipo}"
            if nombre_archivo in archivos:
                page.snack_bar = ft.SnackBar(ft.Text("La categoría ya existe."), open=True)
                page.update()
                return
            exito, mensaje = crear_categoria(directorio_csv, nombre, tipo)
            page.snack_bar = ft.SnackBar(ft.Text(mensaje), open=True)
            if exito:
                dlg.open = False
            page.update()
        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Cargar Categoría"),
            content=ft.Container(
                content=ft.Column(
                    [
                        entrada_nombre,
                        dropdown_tipo,
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE,
                ),
                padding=ft.padding.all(10),
                width=400,
                height=200,
            ),
            actions=[
                ft.TextButton("Guardar", on_click=guardar_categoria),
                ft.TextButton("Cancelar", on_click=lambda e: (setattr(dlg, "open", False), page.update())),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.dialog = dlg
        page.open(dlg)
        page.update()

    def abrir_cargar_pregunta_modal(e):
        categorias = getCategorias(directorio_csv)
        if not categorias:
            page.snack_bar = ft.SnackBar(ft.Text("No hay categorías disponibles."), open=True)
            page.update()
            return
        dropdown_categorias = ft.Dropdown(
            label="Selecciona una categoría",
            options=[ft.dropdown.Option(categoria) for categoria in categorias],
        )
        entrada_pregunta = ft.TextField(label="Escribe la pregunta")
        entrada_respuesta = ft.TextField(label="Escribe la respuesta")
        def guardar_pregunta(e):
            categoria = dropdown_categorias.value
            pregunta = entrada_pregunta.value.strip()
            respuesta = entrada_respuesta.value.strip()
            if not categoria or not pregunta or not respuesta:
                page.snack_bar = ft.SnackBar(ft.Text("Todos los campos son obligatorios."), open=True)
                page.update()
                return
            exito, mensaje = cargarPregunta(directorio_csv, categoria, pregunta, respuesta)
            page.snack_bar = ft.SnackBar(ft.Text(mensaje), open=True)
            if exito:
                dlg.open = False
            page.update()
        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Cargar Pregunta"),
            content=ft.Container(
                content=ft.Column(
                    [
                        dropdown_categorias,
                        entrada_pregunta,
                        entrada_respuesta,
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE,
                ),
                padding=ft.padding.all(10),
                width=600,
                height=400,
            ),
            actions=[
                ft.TextButton("Guardar", on_click=guardar_pregunta),
                ft.TextButton("Cancelar", on_click=lambda e: (setattr(dlg, "open", False), page.update())),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.dialog = dlg
        page.open(dlg)
        page.update()

    boton_config = ft.ElevatedButton("⚙ Configurar", on_click=abrir_config_modal)
    boton_cargar_pregunta = ft.ElevatedButton("➕ Cargar Pregunta", on_click=abrir_cargar_pregunta_modal)
    boton_cargar_categoria = ft.ElevatedButton("📁 Cargar Categoría", on_click=abrir_cargar_categoria_modal)
    botones_modo = ft.Row([
        ft.ElevatedButton("Claro", on_click=lambda e: cambiar_modo("claro")),
        ft.ElevatedButton("Oscuro", on_click=lambda e: cambiar_modo("oscuro")),
        ft.ElevatedButton("Protanopia", on_click=lambda e: cambiar_modo("protanopia")),
        ft.ElevatedButton("Deuteranopia", on_click=lambda e: cambiar_modo("deuteranopia"))
    ], alignment=ft.MainAxisAlignment.CENTER)

    boton_enviar.on_click = manejar_pregunta
    entrada_pregunta.on_submit = manejar_pregunta

    page.add(
        salida_respuesta,
        entrada_pregunta,
        boton_enviar,
        ft.Divider(),
        botones_modo,
        ft.Row([boton_config, boton_cargar_pregunta, boton_cargar_categoria], alignment=ft.MainAxisAlignment.CENTER),
    )

ft.app(target=main)