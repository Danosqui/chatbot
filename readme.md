# Chatbot (Versión de Desarrollo)

Un bot creado por y para la Copa de Algoritmia de UADE.

## Características

- Responde preguntas basándose en los datos almacenados en archivos CSV.
- Soporta múltiples categorías, cada una representada por un archivo CSV.
- Lematiza y normaliza las preguntas para mejorar la precisión de las respuestas.
- Si no encuentra una respuesta, guarda la pregunta en un archivo llamado `Preguntas sin poder responder.csv`.
- Responde rápidamente gracias a la integración con **spaCy** para lematización y **RapidFuzz** para comparación de similitud.
- Permite buscar preguntas específicas dentro de una categoría o en todas las categorías disponibles.
- Responde con ejemplos aleatorios si se consulta directamente el nombre de una categoría.
- **Interfaz gráfica**:
  - Incluye un modo claro, un modo oscuro y soporte para daltonismo (protanopia y deuteranopia).
  - Permite interactuar con el chatbot de manera visual y amigable.

## Requisitos

- Python 3.7 o superior [3.11.x recomendado, 3.13.x no es soportado actualmente por limitaciones de spaCy].
- pip para instalar dependencias.
- **spaCy** y el modelo de español (`es_core_news_sm`).
- **RapidFuzz** para comparación de similitud.
- **Tkinter** (incluido en Python por defecto) para la interfaz gráfica.

## Instalación

1. Clona el repositorio:
   ```
   git clone https://github.com/Danosqui/chatbot.git
   cd chatbot
   ```

2. Instala las dependencias necesarias:
   ```
   pip install spacy rapidfuzz
   python -m spacy download es_core_news_sm
   ```

3. Asegúrate de que los archivos CSV estén en la carpeta [`CSVs`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fbenja%2Fchatbot%2FCSVs%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22766ddea9-e17f-42ed-a1dd-0c2cded3b0de%22%5D "c:\Users\benja\chatbot\CSVs"). Ejemplo de estructura:
   ```
   chatbot/
   ├── CSVs/
   │   ├── programacion.csv
   │   ├── pokemon.csv
   │   └── Preguntas sin poder responder.csv
   ├── chat.py
   ├── interfaz.py
   ├── readme.md
   ```

## Uso

### **Interfaz gráfica**
1. Ejecuta el archivo [`interfaz.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fbenja%2Fchatbot%2Finterfaz.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22766ddea9-e17f-42ed-a1dd-0c2cded3b0de%22%5D "c:\Users\benja\chatbot\interfaz.py"):
   ```
   python interfaz.py
   ```

2. Interactúa con el chatbot escribiendo preguntas en el cuadro de texto y presionando el botón "Enviar".

3. Cambia entre los modos claro, oscuro o soporte para daltonismo utilizando los botones correspondientes.

### **Línea de comandos**
1. Ejecuta el archivo [`chat.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fbenja%2Fchatbot%2Fchat.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22766ddea9-e17f-42ed-a1dd-0c2cded3b0de%22%5D "c:\Users\benja\chatbot\chat.py"):
   ```
   python chat.py
   ```

2. Escribe preguntas directamente en la consola. Ejemplo:
   ```
   Chatbot listo. Escribe 'salir' para terminar.
   Tú: ¿Qué es pandas?
   Chatbot (Programación): El módulo pandas permite trabajar con datos estructurados. (Similitud: 100.00%)
   ```

3. Si el chatbot no reconoce una pregunta, la guardará en el archivo `Preguntas sin poder responder.csv` dentro de la carpeta [`CSVs`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fbenja%2Fchatbot%2FCSVs%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22766ddea9-e17f-42ed-a1dd-0c2cded3b0de%22%5D "c:\Users\benja\chatbot\CSVs").

## Estructura de los archivos CSV

Cada archivo CSV debe seguir este formato:
1. La primera línea contiene el nombre de la categoría.
2. Las siguientes líneas contienen pares de preguntas y respuestas, separados por comas.

Ejemplo (`programacion.csv`):
```
programacion
¿qué es una variable?,Una variable es un espacio en memoria que se utiliza para almacenar datos.
¿qué es el bucle for?,Un bucle for es una estructura de control que permite repetir un bloque de código un número específico de veces.
¿qué es una función?,Una función es un bloque de código reutilizable que realiza una tarea específica.
```

## Documentación

Consulta la documentación completa en el siguiente enlace:

[Documentación](about:blank)

## Instalación alternativa con npm

Si prefieres instalarlo con npm, sigue estos pasos:

```
npm i https://github.com/Danosqui/chatbot.git
cd chatbot
```

## Autores

- [@Dante](https://www.github.com/Danosqui)
- [@Benjamin](https://www.github.com/DuckyCom)
- [@Amélie](https://www.github.com/Ame005)
- [@Noah](https://www.github.com/Dexnou)
- [@Juli](https://www.github.com/)

---

### **Notas adicionales**
- Esta es una **versión de desarrollo**, por lo que algunas características pueden estar incompletas o en progreso.
- Modo daltonismo en proceso
- Documentación en proceso.

---
