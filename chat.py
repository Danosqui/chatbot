import os
import csv
import random
import time
import json
from rapidfuzz import fuzz
from procesamiento_texto import preprocesar_texto

# Cargar configuraciones desde config.json
def cargar_config():
    with open("config.json", "r") as config_file:
        return json.load(config_file)

config = cargar_config()

def getCategorias(directorio):
    categorias = []

    for archivo in os.listdir(directorio):
        if archivo.endswith(".csv"):
            ruta_archivo = os.path.join(directorio, archivo)
            try:
                with open(ruta_archivo, newline='', encoding='utf-8') as f:
                    lector = csv.reader(f)
                    primera_fila = next(lector, None)
                    if primera_fila:
                        categorias.append(primera_fila[0])  # esto es medio feo pero funciona
            except Exception as e:
                print(f"Error al leer {archivo}: {e}")

    return categorias

def cargarPregunta(directorio, categoria, pregunta, respuesta):
    # Validar caracteres inválidos en pregunta y respuesta
    if not validar_texto(pregunta) or not validar_texto(respuesta):
        return False, "La pregunta o respuesta contiene caracteres inválidos."

    for archivo in os.listdir(directorio):
        categoriaArchivo = categoria + ".csv"
        if archivo.lower() == categoriaArchivo:
            ruta = os.path.join(directorio, categoriaArchivo)
            with open(ruta, "a", encoding="utf-8", newline="") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow([pregunta, respuesta])
            return True, "Pregunta cargada exitosamente."
    return False, "Categoría no encontrada."

def validar_texto(texto):
    try:
        texto.encode("utf-8").decode("utf-8")
        return True
    except UnicodeDecodeError:
        return False

def leer_archivo(ruta):
    """
    Lee el contenido de un archivo y lo devuelve como una cadena.
    """
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return archivo.read()
    except FileNotFoundError:
        return f"El archivo '{ruta}' no se encontró."
    except Exception as e:
        return f"Error al leer el archivo '{ruta}': {e}"

def procesar_comando_ayuda():
    """
    Procesa el comando /ayuda leyendo el archivo definido en config.json.
    """
    ruta_ayuda = config["chatbot"]["help_file"]
    return leer_archivo(ruta_ayuda)

def procesar_comando_info():
    """
    Procesa el comando /info leyendo el archivo definido en config.json.
    """
    ruta_info = config["chatbot"]["info_file"]
    return leer_archivo(ruta_info)

def seleccionar_categoria_interactiva(directorio):
    """
    Lista las categorías disponibles en el directorio con la cantidad de entradas
    y permite al usuario seleccionar una.
    """
    categorias = getCategorias(directorio)
    if not categorias:
        return None, "No hay categorías disponibles."

    print("Selecciona una categoría:")
    for i, categoria in enumerate(categorias, start=1):
        # Contar entradas en cada categoría
        ruta_archivo = os.path.join(directorio, f"{categoria}.csv")
        try:
            with open(ruta_archivo, newline='', encoding='utf-8') as f:
                lector = csv.reader(f)
                entradas = sum(1 for _ in lector) - 1  # Restar 1 para excluir la cabecera
        except Exception:
            entradas = 0
        print(f"{i}. {categoria} ({entradas} entradas)")

    while True:
        try:
            opcion = int(input("Ingresa el número de la categoría: "))
            if 1 <= opcion <= len(categorias):
                return categorias[opcion - 1], None
            else:
                print("Número inválido. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingresa un número.")

def procesar_comando_cargar_interactivo(directorio):
    """
    Procesa el comando /cargar de forma interactiva para agregar una nueva pregunta y respuesta.
    """
    # Paso 1: Seleccionar categoría
    categoria, error = seleccionar_categoria_interactiva(directorio)
    if error:
        return error

    # Paso 2: Solicitar la pregunta
    while True:
        pregunta = input("Escribe la pregunta: ").strip()
        if not pregunta:
            print("La pregunta no puede estar vacía. Intenta de nuevo.")
            continue
        if not validar_texto(pregunta):
            print("La pregunta contiene caracteres inválidos. Intenta de nuevo.")
            continue
        break

    # Paso 3: Solicitar la respuesta
    while True:
        respuesta = input("Escribe la respuesta: ").strip()
        if not respuesta:
            print("La respuesta no puede estar vacía. Intenta de nuevo.")
            continue
        if not validar_texto(respuesta):
            print("La respuesta contiene caracteres inválidos. Intenta de nuevo.")
            continue
        break

    # Cargar la pregunta en la categoría seleccionada
    exito, mensaje = cargarPregunta(directorio, categoria, pregunta, respuesta)
    return mensaje

# Función para leer múltiples archivos CSV y extraer preguntas, respuestas y categorías
def cargar_datos_csv(directorio):
    datos = []
    for archivo in os.listdir(directorio):
        if archivo.endswith('.csv') and archivo != config["chatbot"]["unanswered_questions_file"]:
            ruta = os.path.join(directorio, archivo)
            with open(ruta, 'r', encoding='utf-8') as f:
                lector = csv.reader(f)
                filas = [fila for fila in lector if fila]
                if filas and len(filas[0]) > 0:
                    categoria = filas[0][0].strip()
                    if categoria:
                        for fila in filas[1:]:
                            if len(fila) >= 2:
                                pregunta, respuesta = fila[0], fila[1]
                                datos.append({
                                    'categoria': categoria,
                                    'pregunta': pregunta,
                                    'respuesta': respuesta,
                                    'categoria_lematizada': preprocesar_texto(categoria),
                                    'pregunta_lematizada': preprocesar_texto(pregunta)
                                })
    return datos

# Función para buscar la pregunta más similar o interpretar la categoría
def buscar_pregunta_mas_similar(pregunta_usuario, datos, umbral):
    pregunta_usuario_lematizada = preprocesar_texto(pregunta_usuario)
    mejor_similitud = 0
    mejor_respuesta = None
    mejor_categoria = None

    categorias = {entrada['categoria_lematizada'] for entrada in datos}
    if pregunta_usuario_lematizada in categorias:
        categoria = pregunta_usuario_lematizada
        entradas_categoria = [entrada for entrada in datos if entrada['categoria_lematizada'] == categoria]
        ejemplos = random.sample([entrada['pregunta'] for entrada in entradas_categoria], min(3, len(entradas_categoria)))
        return f"En la categoría '{categoria.capitalize()}' hay {len(entradas_categoria)} entradas! Entre ellas: {', '.join(ejemplos)}", categoria.capitalize(), 100

    palabras_usuario = pregunta_usuario_lematizada.split()
    if len(palabras_usuario) == 1:
        palabra = palabras_usuario[0]
        for entrada in datos:
            if palabra in entrada['pregunta_lematizada'].split():
                return entrada['respuesta'], entrada['categoria'], 100

    for entrada in datos:
        if entrada['categoria_lematizada'] in pregunta_usuario_lematizada:
            similitud_pregunta = fuzz.token_set_ratio(pregunta_usuario_lematizada, entrada['pregunta_lematizada'])
            if similitud_pregunta > mejor_similitud:
                mejor_similitud = similitud_pregunta
                mejor_respuesta = entrada['respuesta']
                mejor_categoria = entrada['categoria']

    if mejor_respuesta is None or mejor_similitud < umbral:
        for entrada in datos:
            similitud_pregunta = fuzz.token_set_ratio(pregunta_usuario_lematizada, entrada['pregunta_lematizada'])
            if similitud_pregunta > mejor_similitud:
                mejor_similitud = similitud_pregunta
                mejor_respuesta = entrada['respuesta']
                mejor_categoria = entrada['categoria']

    if mejor_similitud >= umbral:
        return mejor_respuesta, mejor_categoria, mejor_similitud
    else:
        return None, None, mejor_similitud

# Función para guardar preguntas no respondidas
def guardar_pregunta_no_respondida(pregunta, directorio_csv, archivo):
    if config["chatbot"]["save_unanswered_questions"]:
        ruta = os.path.join(directorio_csv, archivo)
        with open(ruta, 'a', encoding='utf-8', newline='') as f:
            escritor = csv.writer(f)
            escritor.writerow([pregunta])

# Función principal del chatbot
def procesar_pregunta(pregunta, directorio_csv, umbral=None):
    if umbral is None:
        umbral = config["chatbot"]["default_similarity_threshold"]

    if pregunta.startswith("/cargar"):
        return procesar_comando_cargar_interactivo(directorio_csv), None, 100, 0
    elif pregunta.startswith("/ayuda"):
        return procesar_comando_ayuda(), None, 100, 0
    elif pregunta.startswith("/info"):
        return procesar_comando_info(), None, 100, 0

    datos = cargar_datos_csv(directorio_csv)
    inicio = time.perf_counter()
    respuesta, categoria, similitud = buscar_pregunta_mas_similar(pregunta, datos, umbral)
    fin = time.perf_counter()
    tiempo_ms = int((fin - inicio) * 1000)

    if respuesta is None:
        guardar_pregunta_no_respondida(pregunta, directorio_csv, config["chatbot"]["unanswered_questions_file"])

    return respuesta, categoria, similitud, tiempo_ms

if __name__ == "__main__":
    directorio_csv = config["chatbot"]["csv_directory"]
    umbral_similitud = config["chatbot"]["default_similarity_threshold"]

    print("Chatbot iniciado. Escribe '/salir' para terminar.")
    while True:
        entrada = input("Tú: ")
        if entrada.lower() == "/salir":
            print("Chatbot terminado.")
            break
        elif entrada.startswith("/cargar"):
            mensaje = procesar_comando_cargar_interactivo(directorio_csv)
            print(f"Chatbot: {mensaje}")
        else:
            respuesta, categoria, similitud, tiempo = procesar_pregunta(entrada, directorio_csv, umbral_similitud)
            if respuesta:
                print(f"Chatbot ({categoria}, {similitud}%): {respuesta}")
            else:
                print("Chatbot: No tengo una respuesta para eso.")