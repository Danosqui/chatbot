ladies and gentleman this is clase number five

Hoy vamos a ver un monton de cosas

## Tipos y técnicas de pruebas

Categorizar los enfoquees de las pruebas para elegir la estrategia para probar en distintos ambientes formas segun los objetivos, las especificaciones del cliente
Se clasifican por el aspecto del software que devemos evaluar; funcionalidad, rendimiento, seguridad, usabilidad, etc

**tipos de pruebas **
- Funcionales
	- Responden al negocio
	- Se basan en las funcionalidades que espeifican los requisitos. Pueden no estar documentadas pero se requiere un nivel elevado para interpretar las pruebas. Si yo lo hago con un equipo de juniors la documentacion tiene que ser muy detallada
	- Las funcoines declaradas de noseque
	- La funcionalidad se clasifica en:
		- Completitud funcional
		- Correccion funcional
		- Pertenencia funcional
- No funcionales
	- Son mas tecnicas, comprotamiento externo del software osea como funciona el sistema
		- Pruebas de carga: se aumenta la carga mas usuarios y asi, se prueba cuanto aguanta con mucha carga
		- Prueba de rendimiento: se prueba la velocidad. Parecidas a las de carga, pero esto tiene que ver con el tiempo de respuesta. 
		- Pruebas de volumen: mucha capcadidad de dato. Tiene que ver con la paginacion 😏
		- Pruebas de esfuerzo: se prueba sobrecargar el sistema y se analiza la recuperacion
		- Pruebas de seguridad: acceso no autorizado, ataque de denegacion. Le pego con este servicio de post osea protegemos de cyberataques con cyberdefensas para que no se haga cyberpelota el servidor
		- Pruebas de estabilidad, eficiencia robustez: como responde el sistema a los errores de funcionamiento, o sea, erroes controlado creo
		- Pruebas de compatibilidad: funcionamiento del sistema en diferentes plataformas (en web no tanto)
		- Pruebas de usabilidad: la facilidad de uso, efectividad y satisfaccion con un grupo de usuarios
- Estructurales
	- Medir la totalida d de las pruebas mediante la evaluacion de tipo estructura

| Tipo de prueba        | Qué valida                                           | Ejemplo                                                       |
|-----------------------|------------------------------------------------------|---------------------------------------------------------------|
| Funcional             | Que el sistema haga lo que debe                     | ¿El botón de "comprar" realiza la acción?                     |
| No funcional          | Cómo lo hace (rendimiento, etc.)                    | ¿Carga en menos de 3 segundos?                                |
| De seguridad          | Que no tenga vulnerabilidades                       | ¿Se puede acceder sin login?                                  |
| De compatibilidad     | Que funcione en distintos entornos                  | ¿Funciona igual en Chrome y Firefox?                          |
| De regresión          | Que algo que funcionaba no se haya roto            | ¿El login sigue funcionando después de un cambio?             |
## Tecnicas de prueba
Es el metodo que se usa para diseñar y ejecutar la s pruebas

- Estaticas
	- No ejecutan la aplicacion, es a nivel de especificaciones, analisis estatico del codigo
	- Analisis estatico: objetivo detectar defectos en el source ocde sin ejecutarlo
	- Revisiones: deteccion y correccion temprana de posibles defectos, y reducicon del tiempo y dinero invertido en el desarrollo y pruebas de software
		- Informal
		- Guiada
		- Tecnica
		- Inspeccion
- Dinamicas
	- Caja blanca: revision de codigo
		- **Sabemos que es lo que pasa adentro**
		- Ruta basica, algo especifico
		- Ciclos o bucles, que no haiga ciclo eterno
		- Condicion y condicion multiple, si logicamente esta bien hecho el fuente
	- Caja negra: lado funcional de la aplicacion
		- **analisis de la especificacion** sin tener en cuenta la estructura interna, no les interesa si es una mierda el programa, solo importa lo que entra y lo que sale, es muy de lciente final
		- Particion de equivalencia
		- Analisis de valor limite
		- Tablas de decisiones: si me da esto tal
		- Trancision de estados
		- Casos de uso que nos dio el cliente
- Basadas en la experiencia
	- Derivan de la habilidad y intuicion del tester.
	- Prediccion de error: se diseñan casos de prueba en base a la experiencia, se anticipan los errores. 
	- Pruebas exploratorias: incapie en la libertad personal. El es garantia de que sale barbaro el es el que sabe dejenlo que haga lo que quiera

| Técnica de prueba           | Qué hace                                           | Ejemplo                                                              |
|----------------------------|----------------------------------------------------|----------------------------------------------------------------------|
| Caja negra                 | Prueba sin ver el código                          | Probar que un formulario funciona bien sin ver su implementación    |
| Caja blanca                | Prueba con acceso al código                       | Revisar condiciones, bucles, caminos del código                     |
| Partición de equivalencia  | Divide entradas en grupos válidos/inválidos       | Probar solo 1 valor representativo por grupo                        |
| Valores límite             | Prueba los extremos del input                     | Probar edades: 0, 1, 99, 100                                        |
| Exploratoria               | Prueba libre sin casos predefinidos               | Navegar la app buscando errores sin un guión                        |
| Basada en la experiencia   | Usa el criterio del tester experto                | “Este campo suele fallar, lo testeo primero”                        |
![[Pasted image 20250411191754.png]]


## Niveles de pruebas

Son capas hasta donde llega el testing ![[Pasted image 20250411191926.png|500]]

- Testung unitario
	- Verifica si cada componente cumple sos especificaciones
- Testing de integracion
	- Los grupos de componentes interactuan de manera correcta.
	- Los componentes funcionan bien por separado pero juntos capaz que no
- Testing del sistema
	- Verifica si el sistema como conjunto cumple con los requisitos, el sistema como un todo en un entorno realista
		- Las capas front ->  back ->  datos
- Testing de aceptacion
	- Orientado al usuario, el cliente prueba que el sistema hace lo que espera que haga
## Ejecución de pruebas y hallazgo de defectos

El mecanismo para encotrar defectos

Pasos para la ejecucion:
- Definir los objetivos de pruebas
- Crear escenarios de pruebas
- Generar datos
- Diseñar y documentar los casos de prueba: no podes hacer las pruebas asi nomas tienen que estar documentadas
- Ejecutar los casos y registrar los resultados

Hallazgo y seguimiento de defectos:
- Analizar resultado de las pruebas
- Identificar reportar y priorizar los defectos
- Hacer seguimiento y resuolucion de los errores encontrados
## Definición de bug
Error en un programa, defecto en el codigo fuente o en la logica del programa que impide su funcionamiento
Los datos no son bug, estan dentro del programa los bugs

Ejs comunes: 
- Problemas de rendimiento
- Funcionalidad no cumpre con los requisitos
- Errores de interfaz

Ciclo de vida de un bug:

## Ciclo de vida de un bug

Se identifican, se informan se gestionan y se resuelven
Es costo arreglar el bug, si zafa el sistema nos concentramos en otra cosa

1. Algiuen descubre que hay un bug. Se encuentran durante los diferentas atividades de pruebas
2. Se reporta el bug, con documentacion

3. **Priorizacion y triaje**: se ifjamos que tan malo es el bug, cual es la severidad, funciona no funciona
	1. La medida en el que el bug puede afectar el software.
	2. No cambia en el tiempo
	3. Su severidad es
		1. Bloqueador (inhibe la continuidad del desarrollo o pruebas)
		2. Critico (afecta una funcionalidad critica y no hay posibilidad de workaround)
		3. Mayor ( perdida mayor de funcionalidad, datos de salida incorrectos, dificultades que inhiben parcial o totalmente le uso del programa)
		4. Media ( parte menor de un componente que no es funcional, no estas validando la edad que sea menor a 120)
		5. Menor (perdida menor de funcionalidad y se le puede dar la vuelta)
		6. Trivial (porblemas cosmeticos)
	4. Prioridad. A veces no me alcanza el tiempo enonces le mostras al cliente que es lo mas importante. La prioridad puede cambiar. Hoy algo no es importante y mañana si.
		1. Baja. Defecto trivial posponible
		2. Media. Defecto que hay que arreglarse pronto antes de lanzar el producto
		3. Alta. Corré
	5. La severidad es evaluado por el etster
	6. La prioridad es evavludado por el manager del proyecto o por el equipo
	7. Considerar como afecta al usuario final y cuanto tiempo toma arreglarlo

Ejemplos:

| Prioridad y Gravedad           | Descripción                                                                                                                                    |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Alta Prioridad y Alta Gravedad | Un error que se produce en la funcionalidad básica de la aplicación y no permite al usuario utilizar el sistema.                               |
| Alta Prioridad y Baja Gravedad | Los errores de ortografía que ocurren en la portada o título o en el título de una aplicación.                                                 |
| Alta Gravedad y Baja Prioridad | Un error de funcionalidad de la aplicación que no permite al usuario utilizar el sistema, pero que rara vez es utilizado por el usuario final. |
| Baja Prioridad y Baja Gravedad | Cualquier problema de estética u ortografía que esté dentro de un párrafo o en algún informe (no en la portada ni en los títulos).             |
Volviendo al ciclo de vida

4. Asignacion del bug
	1. Se asigna a un desarrollador o equipo para que analize el informe y debe reproducir el error y comprender su causa raíz
5. Correccion del bug
	1. El desarrollador intenta arreglarlo, modificando el codigo fuente
	2. Se prueba la solucion para ver si se resolvio y si no se generaron nuevos problemas.
6. Verificacion del bug
	1. Una ves corregido se hacen pruebas  de verificacion
7. Cierre del bug
	1. Listo se verifico se cierra el bug, se considera corregido, se registra el arreglo y el bug

## Causa - raiz de los bugs

Es el origen del problema, no es el sintoma (lo que se ve) ni el efecto ( lo que provoca)
"No me imprime la factura" es lo que le paso al usuario, pero no es la razon porque anda mal

Por que es importante:
- Evita soluciones parche (solo tapar el sintoma)
- Permite mejoras estructurales en el codigo
- Reduce el tiempo de mantenimiento futuro
- Ayuda a **aprender de los errores** y mejorar la calidad del desarrollo

Los 5 por ques: es como el metodo socratico
- Por que fallo el boton?
- Porque no valido bien
- Por que no valido?
- Porque no se programo la validacion
- Por que no se programo?
- Porque no se definio en los requisitos
- Por que no se definio?
- No hubo analisis del flujo de datos
- Por que no hubo analisis?
- Se omitio esa tapa por apuro

Analisis de la causa y efecto (ishikawa o diagrama de espina de pescado)
- Personas (falta capcitacion)
- Fases omitidas en el proceso
- Herramientas mal configuradas
- Codigo ocn logica incorrecta 
- Requisitos mal entendidos (no mal hechos (pasa mucho con los programadores que no decimos cuando no entendemos ) )

Revision de logs y trazas
- Analizar logs para entender la secuencia de eventos

Reproduccion controlada
- Intentar replicar el bug en un entorno de pruebas para ver como y cuando ocurre

| Elemento         | Ejemplo                                                |
|------------------|--------------------------------------------------------|
| Síntoma          | La app se cuelga al guardar                            |
| Causa inmediata  | El campo de texto estaba vacío                         |
| Causa-raíz       | No se definió validación en el análisis funcional      |

Herramientas de defectos:

Todos jiran y jiran
JIRA
El malvado jira

Mantis


