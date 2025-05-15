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

    datos = cargar_datos_csv(directorio_csv)
    inicio = time.perf_counter()
    respuesta, categoria, similitud = buscar_pregunta_mas_similar(pregunta, datos, umbral)
    fin = time.perf_counter()
    tiempo_ms = int((fin - inicio) * 1000)

    if respuesta is None:
        guardar_pregunta_no_respondida(pregunta, directorio_csv, config["chatbot"]["unanswered_questions_file"])

    return respuesta, categoria, similitud, tiempo_ms