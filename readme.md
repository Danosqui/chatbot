# Chatbot

Un bot creado por y para la Copa de Algoritmia de UADE.

## Características

- Responde preguntas basándose en los datos almacenados en archivos CSV.
- Soporta múltiples categorías, cada una representada por un archivo CSV.
- Si no encuentra una respuesta, guarda la pregunta en un archivo llamado `Preguntas sin poder responder.csv`. [configurable]
- Comparación rápida de similitud con **RapidFuzz** y un sistema artesanal de lematización sin dependencias externas.
- Permite respuestas aleatorias al consultar directamente por el nombre de una categoría.
- Soporte para comandos en la línea de comandos (por ejemplo, `/salir`, `/cargar`, `/info`, etc.).
- Posibilidad de cargar una pregunta previamente guardada (en GUI o terminal).
- **Interfaz gráfica moderna con Flet**:
  - Modo claro, oscuro y compatibilidad con protanopía y deuteranopía.
  - Panel de configuración que permite ajustes en tiempo real.
  - Animación de carga (`"."`, `".."`, `"..."`) personalizable.
  - Procesamiento de preguntas y animación de carga en paralelo.
  - Tiempo de respuesta mostrado en milisegundos.

## Requisitos

- Python 3.7 o superior [3.11.x recomendado, 3.13.x no es recomendado con Flet].
- pip para instalar dependencias.
- **RapidFuzz** para comparación de similitud.
- **Flet** para la interfaz gráfica.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Danosqui/chatbot.git
   cd chatbot
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install flet rapidfuzz
   ```

3. Asegúrate de que los archivos CSV estén en la carpeta `CSVs`. Ejemplo de estructura:
   ```
   chatbot/
   ├── CSVs/
   │   ├── Archivos.json
   │   ├── Programacion.csv
   │   ├── Pokemon.csv
   │   └── Preguntas sin poder responder.csv
   ├── .gitignore
   ├── Ayuda.txt
   ├── chat.py
   ├── config.json
   ├── Info.txt
   ├── interfaz.py
   ├── procesamiento_texto.py
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
    "unanswered_questions_file": "Preguntas sin poder responder.csv",
    "help_file": "Ayuda.txt",
    "info_file": "Info.txt"
  },
  "interface": {
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
- **`csv_directory`**: Ruta de la carpeta donde se encuentran los CSVs.
- **`default_similarity_threshold`**: Porcentaje (del 1 al 100) en el que considera el minimo de similitud para que sea considerada valida la respuesta.
- **`save_unanswered_quiestions`**: Boolean para decidir si guardar el input ingresado por el usuario cuando no se le encuentra una respuesta acertada.
- **`unanswered_questions_file`**: Nombre del archivo CSV en el cual se guardan los input ingresados por el usuario cuando no se le encuentra una respuesta acertada.
- **`help_file`**: Ruta de archivo el cual acciona el comando /ayuda
- **`info_file`**: Ruta de archivo el cual acciona el comando /info
- **`default_mode`**: Modo predeterminado de la interfaz gráfica (`claro`, `oscuro`, `protanopia`, `deuteranopia`).
- **`loading_delay`**: Tiempo (en segundos) entre los puntos de la animación (`"."`, `".."`, `"..."`).
- **`loading_animation`**: Activa o desactiva la animación de carga.
- **`loading_cycles`**: Cantidad de ciclos de la animación de carga.
- **`completion_delay`**: Tiempo (en segundos) que tarda en desaparecer el mensaje "Cargando completado." antes de mostrar la respuesta.
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

Consulta la documentación completa **en ingles** en el siguiente enlace y/o markdown:

[![ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/Danosqui/chatbot)
[Documentacion](https://deepwiki.com/Danosqui/chatbot)

## Changelog
b indica que pertenece a la version Development de el proyecto
f indica que pertenece a la version Flet-Development de el proyecto
```
8 de mayo de 2025 0.1
• Creación del chatbot
11 de mayo de 2025 1.0
• Implementación de RapidFuzz y spaCy
11 de mayo de 2025 1.0b
• Implementación de interfaz gráfica
13 de mayo de 2025 1.1b
• Mejora en la GUI e implementación de un config.json
• animación de carga mejorada y manejo dinámico del historial
• procesamiento de preguntas y animación en paralelo
14 de mayo de 2025 1.2b
• bloqueo al estar procesando una pregunta, eliminado errores inesperados
• eliminacion de "palabras vacias" al procesar la pregunta
• loading_animation ahora es funcional
• configuración a tiempo real dentro de la interfaz
• muestra en milisegundos el tiempo de respuesta
14 de mayo de 2025 1.2F
• Rework a chat.py [eliminacion de spaCy e "implementacion manual"]
• Rework a interfaz.py [eliminacion de tkinter e implementación de flet]
14 de mayo de 2025 1.2.1F
• revisión del readme.md
14 de mayo de 2025 1.3F
• Ajuste de modo oscuro en interfaz.py
• Eliminacion de temas de tkinter en config.json
• Modificaciones del readme.md acorde a cambios anteriores
• "Centralizada" la lógica en chat.py
• "Simplificado" interfaz.py
15 de mayo de 2025 1.4F
• Fix de ⚙ Configurar [ahora abre y guarda exitosamente]
• Ahora es posible cargar una pregunta desde la interfaz
15 de mayo de 2025 1.5
• Fix de ⚙ Configurar [ahora cierra sin guardar exitosamente]
• Fix de cargar_pregunta
• Ahora es posible cargar una pregunta desde la consola también
• Ahora chat.py es utilizable (wow!) [python chat.py]
• Utilización de comandos ("/salir", "/cargar" y "ayuda" "/info")
• Creación de utilidades varias (ahora config.json realmente es útil en su totalidad*)
• Arreglos dentro de ⚙ Configurar
16 de mayo de 2025 1.6
• Ajustes visuales a interfaz
• La animacion funciona esta vez
• Texto a la derecha y la izquierda, ¡Como en una conversacion!
• Rework del manejo de la respuesta en la interfaz
• Ahora es posible añadir una categoría [consola e interfaz]
```

## Autores

- [@Dante](https://www.github.com/Danosqui)
- [@Benjamin](https://www.github.com/DuckyCom)
- [@Amélie](https://www.github.com/Ame005)
- [@Noah](https://www.github.com/Dexnou)
- [@Juli](https://www.github.com/)

---

### **Notas adicionales**
- **SI ESTO SIGUE ACÁ ES POSIBLE QUE NO ESTÉ ACTUALIZADO AL 100% EL RESTO DE SECCIONES DEL README**
---

### TO-DO
- ~~Arreglar el modal de configuracion de la interfaz~~
- ~~Que se puedan añadir preguntas desde el chat y la interfaz~~
- Que permita buscar preguntas específicas dentro de una categoría o en todas las categorías disponibles.
- Implementar nuevos tipos de archivos para leer

---