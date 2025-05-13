---

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
  - Animación de carga (`"."`, `".."`, `"..."`) con un mensaje de "Cargando completado.".
  - Configuración dinámica de la interfaz mediante un archivo `config.json`.
  - Procesamiento de preguntas y animación de carga en paralelo para mejorar la experiencia del usuario.

## Requisitos

- Python 3.7 o superior [3.11.x recomendado, 3.13.x no es soportado actualmente por limitaciones de spaCy].
- pip para instalar dependencias.
- **spaCy** y el modelo de español (`es_core_news_sm`).
- **RapidFuzz** para comparación de similitud.
- **Tkinter** (incluido en Python por defecto) para la interfaz gráfica.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Danosqui/chatbot.git
   cd chatbot
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install spacy rapidfuzz
   python -m spacy download es_core_news_sm
   ```

3. Asegúrate de que los archivos CSV estén en la carpeta `CSVs`. Ejemplo de estructura:
   ```
   chatbot/
   ├── CSVs/
   │   ├── programacion.csv
   │   ├── pokemon.csv
   │   └── Preguntas sin poder responder.csv
   ├── chat.py
   ├── interfaz.py
   ├── config.json
   ├── readme.md
   ```

## Configuración

El archivo `config.json` permite personalizar el comportamiento del chatbot y la interfaz gráfica. Ejemplo de configuración:

```json
{
  "chatbot": {
    "csv_directory": "CSVs",
    "default_similarity_threshold": 70,
    "save_unanswered_questions": true,
    "unanswered_questions_file": "Preguntas sin poder responder.csv"
  },
  "interface": {
    "default_theme": "arc",
    "default_mode": "oscuro",
    "loading_delay": 0.5,
    "loading_animation": true,
    "loading_cycles": 3,
    "completion_delay": 1.75,
    "resolution": "900x450"
  }
}
```

### Opciones configurables:
- **`default_theme`**: Tema predeterminado para la interfaz gráfica (compatible con `ttkthemes`).
- **`default_mode`**: Modo predeterminado de la interfaz gráfica (`claro`, `oscuro`, `protanopia`, `deuteranopia`).
- **`loading_delay`**: Tiempo (en segundos) entre los puntos de la animación (`"."`, `".."`, `"..."`).
- **`completion_delay`**: Tiempo (en segundos) que tarda en desaparecer el mensaje "Cargando completado." antes de mostrar la respuesta.
- **`loading_animation`**: Activa o desactiva la animación de carga.
- **`loading_cycles`**: Cantidad de ciclos de la animación de carga.
- **`resolution`**: Resolución de la ventana gráfica (por ejemplo, `"800x600"`).

## Uso

### **Interfaz gráfica**
1. Ejecuta el archivo `interfaz.py`:
   ```bash
   python interfaz.py
   ```

2. Interactúa con el chatbot escribiendo preguntas en el cuadro de texto y presionando el botón "Enviar".

3. Cambia entre los modos claro, oscuro o soporte para daltonismo utilizando los botones correspondientes.

4. La animación de carga se mostrará antes de la respuesta, con un mensaje de "Cargando completado." que se borra automáticamente.

5. El procesamiento de preguntas y la animación de carga ocurren en paralelo para mejorar la experiencia del usuario.

### **Línea de comandos**
1. Ejecuta el archivo `chat.py`:
   ```bash
   python chat.py
   ```

2. Escribe preguntas directamente en la consola. Ejemplo:
   ```bash
   Chatbot listo. Escribe 'salir' para terminar.
   Tú: ¿Qué es pandas?
   Chatbot (Programación): El módulo pandas permite trabajar con datos estructurados. (Similitud: 100.00%)
   ```

3. Si el chatbot no reconoce una pregunta, la guardará en el archivo `Preguntas sin poder responder.csv` dentro de la carpeta `CSVs`.

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

## Changelog
b indica que pertenece a la version Development de el proyecto
```
8 de mayo de 2025 - Creación del chatbot V0.1
11 de mayo de 2025 - Implementación de RapidFuzz y spaCy V1.0
11 de mayo de 2025 - Implementación de interfaz gráfica V1.0b
13 de mayo de 2025 - Mejora en la GUI e implementación de un config.json, animación de carga mejorada y manejo dinámico del historial, procesamiento de preguntas y animación en paralelo 1.1b
```

## Instalación alternativa con npm

Si prefieres instalarlo con npm, sigue estos pasos:

```bash
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
- Documentación en proceso.

---