import os
import csv
import json
import random
from rapidfuzz import fuzz
import spacy
import unicodedata

# Cargar el modelo de spaCy para español
nlp = spacy.load("es_core_news_sm")

# Función para normalizar texto (eliminar tildes y convertir a minúsculas)
def normalizar_texto(texto):
    texto = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('utf-8')
    return texto.lower()

# Función para lematizar texto usando spaCy
def lematizar_texto(texto):
    doc = nlp(texto)
    return ' '.join([token.lemma_ for token in doc])

# Función para leer múltiples archivos CSV y extraer preguntas, respuestas y categorías
def cargar_datos_csv(directorio):

    datos = []
    for archivo in os.listdir(directorio):

        if archivo != 'Preguntas sin poder responder.csv':  # Ignorar el archivo de preguntas no respondidas
        
            ruta = os.path.join(directorio, archivo)
            with open(ruta, 'r', encoding='utf-8') as f:

                filas = []
                if (archivo.endswith('.csv')):
                    lector = csv.reader(f)
                    filas = [fila for fila in lector if fila]  # Filtrar filas vacías
                    
                    
                elif (archivo.endswith('.json')):
                    lector = json.load(f)
                    
                    filas.append([lector[0]["categoria"]])
                    for fila in lector[1:]:
                        filas.append([fila["pregunta"],fila["respuesta"]])
                    #filas = [[fila["pregunta"], fila["respuesta"]] for fila[1:] in lector]
                    #filas.insert(f)
                
        
                if filas and len(filas[0]) > 0:  # Verificar que haya contenido en la primera fila
        
                    categoria = filas[0][0].strip()  # Primera línea como categoría
        
                    if categoria:  # Ignorar archivos con categoría vacía
        
                        for fila in filas[1:]:  # recorrer las filas salteando la primera
        
                            if len(fila) >= 2:  # Asegurarse de que haya pregunta y respuesta
        
                                pregunta, respuesta = fila[0], fila[1]
                                datos.append({
                                    'categoria': categoria,
                                    'pregunta': pregunta,
                                    'respuesta': respuesta,
                                    'categoria_lematizada': normalizar_texto(lematizar_texto(categoria)),
                                    'pregunta_lematizada': normalizar_texto(lematizar_texto(pregunta))
                                })
    return datos

# Función para buscar la pregunta más similar o interpretar la categoría
def buscar_pregunta_mas_similar(pregunta_usuario, datos, umbral=70):
    pregunta_usuario_lematizada = normalizar_texto(lematizar_texto(pregunta_usuario))
    mejor_similitud = 0
    mejor_respuesta = None
    mejor_categoria = None

    # Verificar si el usuario solo escribió el nombre de una categoría
    categorias = {entrada['categoria_lematizada'] for entrada in datos}
    if pregunta_usuario_lematizada in categorias:
        categoria = pregunta_usuario_lematizada
        entradas_categoria = [entrada for entrada in datos if entrada['categoria_lematizada'] == categoria]
        ejemplos = random.sample([entrada['pregunta'] for entrada in entradas_categoria], min(3, len(entradas_categoria)))
        return f"En la categoría '{categoria.capitalize()}' hay {len(entradas_categoria)} entradas! Entre ellas: {', '.join(ejemplos)}", categoria.capitalize(), 100

    # Buscar coincidencias con las preguntas dentro de la categoría específica (si se menciona)
    for entrada in datos:
        if entrada['categoria_lematizada'] in pregunta_usuario_lematizada:
            similitud_pregunta = fuzz.token_set_ratio(pregunta_usuario_lematizada, entrada['pregunta_lematizada'])

            if similitud_pregunta > mejor_similitud:
                mejor_similitud = similitud_pregunta
                mejor_respuesta = entrada['respuesta']
                mejor_categoria = entrada['categoria']

    # Si no se encuentra en la categoría específica, buscar en el resto
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
def guardar_pregunta_no_respondida(pregunta, directorio_csv, archivo='Preguntas sin poder responder.csv'):
    ruta_archivo = os.path.join(directorio_csv, archivo)
    with open(ruta_archivo, 'a', encoding='utf-8', newline='') as f:
        escritor = csv.writer(f)
        escritor.writerow([pregunta])

# Flujo principal
def chatbot(directorio_csv):
    
    print("Cargando datos...")
    datos = cargar_datos_csv(directorio_csv)
    #os.system('cls')
    print("Chatbot listo. Escribe 'salir' para terminar.")
    print("Chatbot: Hola! Soy un chatbot, puedes hacerme preguntas sobre las siguientes categorias: Pokemon, Programacion y Archivos.")

    while True:
        pregunta_usuario = input("Tú: ")
        if pregunta_usuario.lower() == 'salir':
            print("Chatbot: ¡Adiós!")
            break

        respuesta, categoria, similitud = buscar_pregunta_mas_similar(pregunta_usuario, datos)

        if respuesta:
            print(f"Chatbot ({categoria}): {respuesta} (Similitud: {similitud:.2f}%)")
        else:
            print("Chatbot: Lo siento, no entiendo tu pregunta.")
            guardar_pregunta_no_respondida(pregunta_usuario, directorio_csv)

# Ejecutar el chatbot
if __name__ == "__main__":
    directorio_csv = "CSVs"
    chatbot(directorio_csv)