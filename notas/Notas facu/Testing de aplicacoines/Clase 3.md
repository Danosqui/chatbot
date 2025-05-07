(unidad 2 parte 2)

### El proceso del testing

- Planificación
	- Objetivos, requisitos, horarios y entornos de prueba. (o sea hay entorno de desarrollo, testing, pre-productivo y productivo)
- Diseño
	- Crear escenario y caso de prueba
- Ejecucion
	- Poner en practica
- Evaluacion
	- Como salieron las pruebas, determinar si se cumplen los requisitos. Dependiendo de esto viene la etapa de
- Corrección
	- Arreglar los defectos encontrados
- Documentacion
	- Hacer un informe con los responsables de las pruebas.
- Aceptacion
	- Decidir si cumple con las espeficiaciones y esta listo para la entrega

En el ciclo de vida del proyecto el testing puede corregir errores desde el inicio del diseño.
Tener testers al final del dia va salir mas barto que no tenerlo porque los errores se terminan pagando

El proceso del testing son las actividades especificas para planificar, diseñar ejecutar y reportar pruebas.
El testing es un subproyecto dentro del proyecto

#### Marco tradicional

Es terrible malisimo malardo el infame cascada

Bien
- Es predecible, trazable y sirve para bancos
- Mas que nada se usa en bancos
Mal
- Detecta tarde los errores
- Si el tiempo se acorta la fase de testing es la mas afectada
- Poca flexibilidad

#### El marco agile
El bueno

Osea como q es estos marcos pero en testing

En el testing:
- Continuo e integrado
	- Las pruebas se hacen en **cada sprint** o con kanban de forma **continua**


####  El scrum
Ciclo o etapas de desarrollo (una semana mas o menos parece) conocidos como sprint
Todo los dias se hace el scrum, la daily como en efsi para sincronizar las actividades y planificar la jornada

#### El kanban

El tablero 
#### El extreme programming
- Foco en la comuncacion, simplicidad, feedback
- Todos corriendo para todos lados gritando
- Alta productividad todo el tiempo
- Confianza 
- Ejemplo de microsoft
- Lo importante es mantener al cliente conento
Ventajas
- Simplicaidad del codigo 
	- Como es re rapidisimo tiene q ser re simple cosa de q si se rompe algo sea facil de arreglar
- Desarrollo mas agil y tiene pruebas constantes todo el tiempo
Desventaja
- No le dan bola al diseño
- Si todos los miembros del equipo no estan presencial no sirve
- No siempre hay registro de posibles errores


Ventaja del agile
- Deteccion temprana de bugs
- Constante feedback
	-  se hace sprint review con el cliente cada 1 semana o 15 dias 
- Adaptabilidad
	- Como cada 15 dias las historias de usuario van cambiando se adaptan
Contras
- Como es mas rapido hay mas presion y tenemos menos tiempo para probar
- Riesgo de deuda tecnica
	- Si no se hace mantenimiento vamo a tener problema
- Dependencia de automatizacion
	- Es muy importante el testing de automatización

#### El Marco hibrido

En las fases iniciales se hace un enfoque tradicional (documentacion detallada)
En las fases de desarrollo y testing son agiles (sprint con pruebas continuas)

Beneficio
- Balance entre cobertura en velocidad
- Se adapta a contextos complejos
	- Sirve en proyectos legacy
Contras
- Doble esfuerzo
	- Tenemo q hacer la documentacion tradicional y la automatizacion agil
	- Si no esta bien bien claro el equipo de testin se confunde

| Aspecto             | Tradicional                                       | Agile                                      | Híbrido                                      |
|---------------------|------------------------------------------------|--------------------------------------------|---------------------------------------------|
| **Momento de testing**  | Fase final del proyecto.                       | Continuo (durante cada iteración).         | Según el componente (fase final o continua). |
| **Automatización**      | Opcional, enfocada en regresión.              | Crítica (para velocidad y cobertura).      | Mixta (automatización en módulos ágiles).   |
| **Documentación**      | Casos de prueba detallados y estáticos.        | Casos de prueba dinámicos (ajustables).    | Documentación crítica + casos ágiles.       |
| **Rol del tester**     | Ejecutor de planes predefinidos.               | Colaborador activo en diseño de features.  | Adaptable (ej.: tester técnico + analista de QA). |
Caundo usarlos
Tradicoinal: ISO te pide el tradicional por la documentacion para la certificaciones
Agile: hay requisito alto de velocidad
Hibrido: regulaciones parciales, como un fintech porque es parte regulada y parte software

### Equipo de gestion

##### Product owner
- Prioriza el backlog del producto. Define la prioridad del backlog
- Define los criterios de aceptacion
- Valida el producto final
##### Gerente de proyecto
- Gestiona todo el rpyoecto
- Planifica hitos asigna recursos
- Facilita la colaboracion entre equipos
##### Desarrollador
- Construye el producto
- Corrige los bugs q reporta testing
- Participa en revisiones de codigo para estandares
##### Lider tecnico
- Creo q seria el senior, es el guia que te guia tecnologicamente
- Decide la tecnologia correcta
- Revisa problemas complejos y revisa codigo critico
- Mentoriza al equipo de desarrollo

#### Equipo de testing

#####  Diseñador
- Arqiutecta la claidad
- Hace los casos de prueba
##### Tester
- Suele ser lam aquina
- Hace las pruebas manuales
- Reporta los defectos
##### Automatizador
- Hace los scripts de automatizacion
- Framework de las pruebas automatizadas


### Herramientas de testing

- Software para todas las fases del testing
- Centraliza la inforamcion de pruebas
- Colaboracion entre qa dev y po
- Automatizar cosas repetitivas 

Tipos de amigos
El enojado

Herramientas de testin
- Gestion de casos de prueba con jila
- Segimiento de defectos con jira o bugzilla
- Automatizacion de pruebas con selenium cypress 

Tipos de herramientas de gestion
- Integracion continuous integrations jenkins o gitlab
- Colaboracion con slack
- Pruebas de rendimiento con jmeter loadrunner gatling
- Accesibilidad axe wave lighthouse (ese lo conozco) cuplimientos de standares

Elementos clave del registro de bugs

| Campo                     | Descripción                                         | Ejemplo                                                                         |
| ------------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Título**                | Breve y descriptivo.                                | "Error 404 al acceder al perfil de usuario".                                    |
| **Descripción**           | Explicación detallada del problema.                 | "Al hacer clic en 'Mi Perfil', se muestra un error 404 en lugar del contenido". |
| **Pasos para Reproducir** | Secuencia exacta de acciones para replicar el bug.  | 1. Iniciar sesión. 2. Hacer clic en "Mi Perfil".                                |
| **Resultado Esperado**    | Comportamiento correcto según requisitos.           | "Debería mostrarse el perfil del usuario".                                      |
| Entorno                   | Donde ocurrio el bug                                | Windows 10 Chrome v 115                                                         |
| Severidad                 | Critico, alto, medio, bajo                          | Alto: bloquea funcionalidad principal                                           |
| Prioridad                 | Urgencia de correccion (urgente, alta, media, baja) | Urgente                                                                         |

**Título:** "Error al procesar pago con tarjeta de crédito".

**Pasos:**  
1. Agregar producto al carrito.  
2. Ingresar datos de tarjeta válidos.  
3. Hacer clic en "Pagar".  

**Resultado Esperado:** "Confirmación de compra exitosa".  

**Resultado Actual:** "Mensaje: 'Error en el servidor, intente más tarde'".  

**Adjuntos:** Captura de pantalla del error + logs de la consola.  

**Severidad:** Crítico.  


Errores comunes
- Reportar bugs duplicados
- Asignar prioridades incorrectas
- No inclur pasos correctos para reproducir