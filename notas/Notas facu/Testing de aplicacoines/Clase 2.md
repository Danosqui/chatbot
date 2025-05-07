### ¿Qué es el QA y que es el Testing?

#### QA
- Es prevenir
- Proactivo
- Viene antes del desarrollo
- Desarrollar manteniendo la menor cantidad de defectos en la aplicación
- Diseña un buen proceso de desarrollo
#### QC (Testing) 
- Revisa el producto terminado
- Reactivo
- Buscar identificar errores y corregirlos
- Validar que cumpla con los requisitos establecidos

Ambos son esenciales para que la calidad de software sea buena;
- Minimizar errores
- Optimizar la satisfacción del cliente.

### Importancia del testing


- Reducir costos al detectar errores temprano
	- El costo de arreglar un bug es más caro cuanto mas tiempo pasa
	- Identificar y corregir error es al principio del desarrollo
- Mejorar la experiencia de usuario
	- Un software probado garantiza funcionamiento fluido y intuitivo
	- Asegura que cumpla con las expectativas y necesidades
- Evita fallos críticos en producción
	- [ ] Que es prod📅 2025-03-24 
- Mayor masticación del cliente
	- Si está sin fallos el cliente le va a gustar más  y seguro te llama de nuevo
- Cumplimiento de estándares de la calidad
	- El qa y testing aseguran q el software cumpla con los estandares de calidad.
	- Es especialmente crítico en industrias reguladas, como la banca la salud la aviacion donde hay consecuencias fuertes
- Reducción de riesgos
	- Identifica y mitiga riesgos **antes** de que el software llegue a prod, evitando fallos que podrian afetar el negocio
- No solo garantiza el producto de alta calidad sino que protege al negocio, cumple con regulaciones y asegura que los clientes tengan una experiencia positiva.

### Actividades del analista de QA/tester


1. Analisis de los requerimiento. (analista qa)
	1. Entender las especificaciones del software, hasta donde van a llegar el alcance
	2. Identificar los criterios de acepcation
2. Diseñar casos de pruebas (analista qa)
	1. Prioriza las pruebas segun que tan critico es
	2. Crear pruebas manuales y automatizadas
3. Ejecutar las pruebas (tester)
	1. Realiza las pruebas funcionales y no funcionales. Importante que las haga el tester antes de que se llegue osea que ya este ncuando hay que hacerlas. Se diseñan junto al cliente
	2. Prueba en distintos entornos
4. Reporte y seguimiento de defectos (tester)
5. Pruebas de regresion
	1. Yo tengo que hacer una modificacion en un sistema. La prueba de regresion implica hacer la prueba del circuito completo. Muchas veces se modifica algo en el desarrollo y puede impactar en algo que pasa algo. Osea se prueba todo cambiando algo chiquito
	2. Tambien se valida que las correcciones que se hacen no generen nuevos errores
6. Automatizacion de pruebas
	1. Scripts de automatizacion para automatizar pruebas. Pro ejemplo emular que entran un monton de personas
	2. Implementar esto mientras se esta trabajando
7. Colaboracion con equipos de desarroyo y producto
	1. El qa y el tester participan en reuniones de lpanificacion
	2. Asegurar la calidad desde las primeras etapas
8. Revision de documentacion y cumplimiento de normas


### Validacion vs verificación

La validacion es un conjunto de actividades que asegura que el software desarrollado drespeta los requisitos del cliente. Validaciones de negocio y validaciones tecnicas, por ejemplo cuando yo ingreso datos el numero de cuit, valida los digitos del cuit. Eso es de sistema. Si no puedo vender en una zona en particular es una validacion de negocio, una regla de negocio, el viejo service. ==Depende de lo que necesita el cliente==

¿estamos construyendo el producto correcto? Lo que hago

La verificacion se asegura de que una funcion especifica esta bien implementada. Esta bien programado la tecnologia. Se construyo correctamente

Estamos cosntruyendolo correctamente? Como lo hago.

![[Pasted image 20250321190801.png]]

### Ciclo de demming
Es un metodo para la mejora continua
Esta compuesto por 4 etapas

Inportancia en el qa y el testing: permite identificar problema y optimizar pruebas
Esta metodologia es buscar los problemas a medio de metodos
Y otimiza estos procesos de prueba.

Las etapas:
- Planificacion
	- Definir los objetivos y se identifican los riesgos potenciales
	- Planificar las pruebas
	- El area de QA tiene que tener la vision de cuales son los riesgos que podemos llegar a tener con esta aplicacion. Cuanta gente lo va usar, uqe tipo de usuairo voy a tener
	- Como lo vamos a probar cual va ser la estrategia, como se va medir 
- Hacer
	- Ejectuar las pruebas segun el plan
	- Implementar soluciones y estrategias de mejoras
	- Que hacemos cuando explota con esta infraestructura
	- La estrategia de mejora es eso de gmail, como vamos a mejorar cuando empiece a crecer 
- Verificar
	- Se verifica que los objetivos planeados se cumplan
	- Se comparan las metricas con los objetivo establecidos
- Actuar
	- Aplicar las correcciones 
	- Ajustar las estrategias de pruebas
	- Repetir el ciclo

Pdca plan do check act

#### Beneficios del circulo

- Mejora el proceso del testing
- Prevencion de defectos. Toodl oque se puead salvar antes que se detecte mejora el prodcuto
- Optimiza el tiempo y recursos de las pruebas

#### Ejemplo practico

	Plan: diseñar pruebas automatizadas para reducir defectos en produccion
	do: implementar y ejectuar los scripts
	Check: revisar la tasa de errores y compararla con versiones anteriores
	act: mejorar los casos de prueba y ajustar el proceso de testing

Si mi tasa de errores crece mi entonces calidad de desarroyo es peor

### Testing

¿Que es el testing?

- Es escencial en desarrollo y mantenimiento de sistemas. El software con mas testing tiene menos probabilidad de errores.
- El objetivo es evaluar la calidad del software y reducir el riesgo de fallso
- Lai dea del tester es romper, detectar problemas
- Y si comple con los requisitos del usario que me lo pidio

#### Objetivos del testing
- Garatnizar calidad
- Corregir errores lo ams temprano posible para que no le lleguen al usuario. Los errores duelen al usuario. Si no hay errores desde temprano el usuario va estar tranquilo y mejor para nosotros
- Validar los requerimientos. Probablemente los requerimientos cambien.
- Mejorar fiabilidad del software. Tiene que ser fiable, tiene que hacer lo qeu el usuario queiere que haga
- Reducir el reisgo de fallos

#### Beneficios del testing
- Menos costos
- Mejor imagen de la empresa
- Mejor claidad del software
- Mas astisfaccion del cliente
- Reducen los riesgor

### Errores, defectos y fallas

- El error es del programador
	- Accion humana que produce resulta do incorrecto. Diseño, codificacion o incluso requisitos.
	- El usuario siempre va a decir "el sistema no anda", para el el sistema no anda, sea com osea si no arranca o calcula mal
	- El programador hace un error
- El defecto es que no se contemplo algo, es un bug, tenemos un problema de datos. Es algo que no se ve hasta cierta circunstancia
	- Es un bug
	- Imperfeccion en el  codigo
	- Surge durante cualquier etapa de desarroyo
	- Se identifican mediante pruebas de software
	- El rpogramador no conempla algo
- El fallo del sistema es, se actualizo una libreria de la coneccionde la base de datos por el sitema operativo y rompe el programa. Hay que salvarlo antes de que pase.
	- Manifestacion visible. La falla se ve se palpa cuando se ejecuta
	- No se copmorta como lo espera el usuairo
	- Las fallas es lo que llega ver el usuario final
	- Son el resultado de los defectos que no se detectaron a atiempo y no se corrigieron antes de que el software se ponga en produccion
	- Externo, en el sistema y no el software


#### Ejemplos

Interrupcion masivas de los sistemas de delta air lines
Causa: 
	actualizacion fallida del software proporcionado por crowdstrike. Un parche de seguridad y se rompio todo
	No se realizo la verificacoin antes
Impacto:
	Perdidas economicas
	Daño a la reputacion
Leccion:
	Importancia de las pruebas
	Plan de contingencia (el rollback tiene que estar bien aceitado)
	Supervision de proveedores externos

### Normas y estandares de calidad

Las norams aseguran la consistencia y confiabilidad de los productos

- ISO 9001
	- Estandar de calidad para **TODO**
	- Muy generico 
- ISO/IEC 25000
	- Software
	- Metricas de calidad 
- ISTQB
- CMMI
	- Nievles de madurez como va creciendo ese desarrollo. 
	- Mejoras progresivas en cada iteracion
- IEEE 829
	- Planes de prueba detallados, registro estructurado de defectos

Beneficios de usar estandar
- Reduccion en defectos criticos
- Confianza de los usuarios
- Normas tipo de los bancos

#### Ejemplo de reporte de defectos de un e-commerce

- Informacion general
	- Id del efecto
	- Rpotyecto
	- Modulo: afectado el pago
	- Fecha
	- Reportado por juan
	- Prioridad alta
	- Severidad critica
- Despues la descripcion: 
	- Resumen
	- Como reproducir
	- Resultado esperado
	- Resultado observado
- Despues el analisis y la posible causa
- Evidencia adjunta
- Estado
	- Estado abierto
	- Asignado a equipo de desarrolo
	- Modulo afectado
	- Fecha estimada
- Comentarios adicionales