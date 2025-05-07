## Ciclo de vida del testing

- Es practicamente lo mismo que el del software. 
- A medida que el producto avanza tambien avanza el testing.
- Tambien tiene planificacion, diseño, ejecucion, control y cierre
- Es el plan maestro del testing

1. Analisis de los requisitos
	1. Se revisan los requisitos con el objetivo de saber que se debe probar. Por ejemplo los usuarios deben poder aplicar un cupon, entonces
	2. Se identifican preguntas clave y criterios de aceptacion
2. Planificacion de las pruebas
	1. Se establece la estrategia de plan de pruebas, estableciendo los objetivos y estimaciones de esfuerzo y costos y recursos
	2. Objetivo es definir como cuando y con que recursos se va probar. Esto se hace en la planificacion del proyecto para saber cuanto se va a costar. Por ejemplo: un pran de pruebas:
		1. Probar la funcionalidad de cupones en navegadores, herramientas postman, riesgos la sincronizacion, cronograma 2 dias manuales y 1 dia 
3. Desarrollo de casos de pruebas
	1. Se crean y verifican y reelavoran los casos y scripts de prueba
	2. Objetivo: crear casos de prueba detallados y sus scripts automatizacion
		1. Caso 1: aplicar cupon valido, pasos ir al checkout etc y verificar el descuento
		2. Caso 2: ingresar upon expirado y verificar el mensaje de error
4. Configuracion del entorno de prueba
	1. Objetivo preparar el entorno para simular la realidad
	2. Ejemplo:
		1. **Base de datos** de prueba con cosas reales que no sean asfd
		2. Desplegar una version de prueba del backend **servidor**
		3. Configurar emuladores de android por ejemplo para probar en **dispositivos**
		4. Usar selenium para automatizar el flujo del checkout en navegadores
5. Ejecucion de pruebas
	1. Ahora si se hacen las pruebas y se regisran los resultados y se comparan con resultados esperados. 
	2. El objetivo es ejecutar las pruebas y documentar los resutlados
		1. Por ejemplo resultados:  caso 1 exitoso
		2. Resultados tambien Caso 2 fallo el sistema aplica el descuento aunque esta expirado. Es un error
		3. El reporte
6. Cierre del ciclo de prueba
	1. Se termina la ejecucion 
	2. Objetivo evaluar los resultados documentar lecciones y cerrar el ciclo
		1. Por ejemplo informe final: 80% de casos exitosso, 2 defectos alta prioridad corregidos
		2. Hallazgos clave, el error e ncupones expirados se debio a un fallo en la api
		3. Post ciclo se arhcivan los casos de prueba, Actualizar el plan de pruebas para incluir validaciones de fechas en futuros ciclos osea parender de los errores
		4. Leccion aprenidda: incluir pruebas de integracion api frontend en cada script

## Los 7 fundamentos segun el ISTQB
Son los principios que gian las paracticas de pruebas de software.

- El Testing demuestra la presencia de defectos
	- Nunca podemos decir que el producto esta libre de defectos
- El Testing exhaustivo no existe
	- Probar todas las combinaciones posibles no es factible excepto en un caso basico. Por ejemplo no podes probar si una api te dice bien la temperatura en ttodas las ciudades de l mundo, es demasiado costoso
	- Por eso hay que decidir cuales pruebas hacer
- Las pruebas tempranas ahorran tiempo y dinero
	- Los shift left se llaman, se empiezan las pruebas al principio del ciclo de vida del desarrollo. 
	- Un defecto encontrado en post produccion cuesta 30 veces mas que si lo encontras en la etapa de diseño
- Agrupación de defectos
	- La mayoria de los defectos se encuentran en pocos modulos
	- Si agrupoamos los defectos por modulos vamos a encontrar la solucion mas rapida para todos los defectos
	- (no entendi muy bien que seria un modulo)
- Paradoja del pesticida
	- El uso frecuente de pruebas identicas a lo largo del tiempo disminuye la eficacia para encontrar nuevos fallos. Si repetimos las mismas pruebas una y otra vez eventualmente dejaran de detectar nuevos defectos
	- Hay que actualizar los datos y las pruebas existentes y hacer pruebas nuevas
- El testing depende del contexto
	- Cada proyecto es distinto, los enfoques en las pruebas se tiene uqe adaptar a las necesidades especificas del proyectos
	- Con mas riesgo hay que invertir mas en pruebas
- Falacia de la ausencia de errores
	- Hay organizaciones que bueno vamos a armar un equipo de testing y despues si hay un error en la implementacion ehh que hicieron los testers
	- Encontrar todos los defectos es imposible
	- Encontrar y solucionar un gran numero de errores no asegura el exito

## Fases del testing
Los pasos estructurados para asgurar que el sistema cumple con los requisitos

Muy parecidas al desarrollo
`// Comentario danosqui: es mas de lo mismo de software y agaile y todo literalmente`
1. Planificacion
	1. Que, quien, como cuando
	2. Estrategias y estimaciones, roles y recursos, se seleccionan herramientas
2. Analisis
	1. Detectan requerimientos testeables, condiciones de prueba, revisa la documentacion funcional
3. Diseño
	1. Se hacen los casos de prueba, se definen datos y scripts, se preparan cripterios de aceptacion
4. Implementacion
	1. Se construyen los scripts , se revisan y completan casos, se prepara el entorno tecnico de prueba
	2. Se arma todo el secenario copmleto para poder ejecutar el testing
5. Ejecucion
	1. Se ejecutan los casos de prueba
	2. Se documentan los bugs
6. Evaluacion de criterios de salida y reporte
	1. Se analizan los resultados, se comparan ocn los criterios de salida definidos. Se decide si ocntinuar o cerrar la prueba. Hay veces uqe los errores so ninfimos y alguien puede decidir continuar. Por ejemplo en un navegador avris el f12 y esta lleno de errores
7. Cierre
	1. Informe final
	2. Evaluacion del proceso
	3. Archivar artefactos y aprendizaje


## Mentalidad del tester

- Tiene uqe descubrir por que podria fallar un software. 
- Intenta atniciparse,
- Mas alla de lo que le pase
- El objetivo de un tester no es ver que no ande isno que ande mejor

- El objetivo no es romper sino mejorar
- Estan contentos cuando hay un error no porque haya un error sino porque se descurbio y se puede arreglar.
- El objetivo es mejorar no romper. El objetivo es mejrora no criticar al personal
- No busca culpas bulca soluciones (dificil mas que nada en entornos muy corporativos)

Caristicas clave de la mentalidad
- **Cursioso**
	- Tiene que probar cosas nuevas¿ tipo a ver uqe tan fuerte es este sistema
	- Y si el usuario hace clic aqui sin haber completado formulario?. Se hace preguntas constantement
- **Pensamiento lateral**
	-  que pasa si cambio el idioma mientras estoy copmrando
	- Encontrar fallos pensando de forma cretia
- **Esceptisismo sano**
	- El sistema me dico que lo hizo bien pero realmente lo hizo?
	- Error no me dio en ningun lado, pero esta 
- **Empatía**
	- Los abuelos son excelentes tester
	- Es claro, amigable accesible?
- Actitud constructiva
	- Un tester efectivo comunica los errores con respeto y claridad
	- Propone soluciones cuando puede. Tiene una idea de como arreglarlo
	- Documenta bien para facilitar correccion
- **observacion**
- **comunicacion** es el 50% menos del problema
- Asertividad
	- Decir lo que hay que decir de manera respetuosa. "el desarrollador se equivoco otra vez ❌"
	- El foco esta en el hecho tecnico no la persona
- Resiliencia
	- Seguir aportando valor aunqeu las cosas salgan como no se espera
	- Puede ser que reciban reacciones negativas o defensivas de otros miembros del equipo
- Trabajo en equipo
	- Colabora. La imagen del tester para el programador es ahi viene la plolicia porque claro te delata los errores
	- Es parte del equipo
- Objetividad
	- Siepmre que digo algo esta mal lo tengo que demostrar, nunca "esta mal hehco" si "segun el requisito x el sistema deberia hacer y pero actualmente hace z"
	- Un bug bien documentado y con pasos claros tiene mas posibilidad de ser resuelto rapido

Muy pocas veces el tester va decir esta todo bien

## Comunicacion efectiva

- En sistemas nos cuesta mucho hablar y es muy importante

- Un tester trabaja con muchas personas diferentes entonces hay un codigo de comunicacion para que se entiendan entre todos.
- No alcanca con decir "esto no funciona" hay que explicar que pasa, odnde pasa y como se puede reproducir

El bug tien que estar bien comunicado
Ya lo vimos, que paso como reproducirlo etc.
Capturas de pantalla

Otra vez  lo de evitar juicios personales

Depdende con quien hablas tenes cierto lenguaje, tecnico o no, puede ser qa y puede ser cliente etc


