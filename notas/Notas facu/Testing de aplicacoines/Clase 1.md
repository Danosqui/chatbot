
### ciclo de vida de desarrollo de software

es un procesos par diseñar software de alta calidad.
###### objetivo: reducir riesgos, cumplir explectativas del cliente
###### se divide en fases
![[Pasted image 20250314204129.png]]

**Gestoin del proyecto**: no importa el rol todo es transparente
**Gestion del recursos**: muchos o pocos recursos para el desarrollo
(la cantidad de programadores no es directamente proporcional al tiempo que se tarda)
**Reduccion de riesgos**: identificar y minimizar los errores, evitando problemas en produccion
**Entrega sistematica**: entregar recurrentemente para satisfacer al cliente. Cuando entregas menos genera mas como que desfonfianza?

Fases del SDLC (software development life cycle)
**Planificacion**. La mas dificil, nunca te dice el cliente de una todo lo que necesita pero despues te pide lo que necesita
**Diseño**. Se elige la tecnologia a usar, se definen las herramientas, se planifica la integracoin en el sistema de la empresa.
**Implementación**: se hace se codifica, se dividen las tareas en pequeñas. Aca adentro esta el ==testing==
**despliegue**: se lleva a produccion
mantenimiento: el soporte, si hay un problema. dentro del soporte
	los niveles de los problemas, nivel 1 me olvide la clave, nivel 2 no se, nivel 3 no anda algo que hay uqe cambiar


#### Modelos SDLG
las metodologias

cascada. lo peor. odio cascada. Es secuencial, hay que terminar cada fase antes de pasar a la siguiente. es adecuada cuando no hay cambios en las etapas anteriores. hoy en dia nunca pasa eso.

iterativo. por modulo voy creando, voy llendo de modulo a modulo. las entregas. investigar. voy relevando y haciendo, se hacen mejoras y cambios cada vez que hago una entrega. osea voy haciendo iteraciones y vas cambiando con cada releveamiento. yo te veo todas las semanas

espiral. lo mejor de los dos. Se desarrolla en ciclos repetitivos. esta bueno para proyectos grandes. son muchos periodos cortos. 

agil, metodologias agiles. Se basa en entrega incremental, voy relevando. se centra en entregar el valor al usuario de forma rapida y eficiente, todas las semanas te voy mostrando rapido. sprint de 15 dias mas o menos. Es importante que el cliente participe del equipo agil. si el cliente es pasivo no se puede. detecta errores temprano porque son entregas chicas y rapidas.

### que es la calidad

es subjetivo
garvin definio cinco enfoques principales

**Basado en la trascendencia.** algo que se reconoce de inemdiato, no se mide, se percibe.

**Basado en el producto.** la calidad tiene que ver con las caracteristicas del producto. mas funcionalidades, mejor. por ejemplo un editor de texto con IA

**Basado en el usuario**. Segun el usuario final. Si un producto satisface tiene calidad, vos no sabes si es bueno pero capaz solo le gusto, con que le guste es calidad.

**Basado en el fabricante**. Segun las especificaciones. Por ejemplo si un software no tiene bugs y esta bien documentado es de calidad, aunque no tenga muchas funcionalidades.

**Basado en el valor**. la calidad depende de cuanto esta dispuesto a pagar el cliente. Un producto es de calidad si su beneficio cjustifica su costo

### la calidad de software

Proceso eficaz de software que es util y funciona

Dimensiones de la claidad de garvin:
	**Rendimiento**. Que tan bien cumple su funcion principal
	**Caracteristicas**, atributos que complementan. Ej. gps en el telefono que me complementa me sirve
	**Confiabilidad**. funciona correctamente durante un periodo sin fallas
	**Conformidad**. que tanto cumple con las espifecificaciones establecidas
	**Durabilidad**. El tiempo de vida util antes de reemplazarlo
	**Capacidad de servicio**. Quien esta atras del producto que compro. El soporte ofrecido, la asistencia tecnica.
	**Estetica**. Que tan lindo es el producto. Si un producto es feo no es agradable no da sensacion de calidad
	**Calidad percibida**. Impresion subjetva del cliente segun la calidad basado en sus experiencias. Cuantas cosas compraron porque les dijeron que estaba bueno, muchas veces les preguntas a otros

#### Otras dimensiones de calidad, 
factores que pueden medirse en forma directa
puede correr crisis?
cantidad de bugs detectados luego de pruebas
Factores que se miden de forma indirecta
la prercepcion del usuario o analisis cualitativos
por ejemplo la usabilida del sistema que se mide mediante necuestas alos usuarios.
depende de los usuarios, si les gusta o no.


#### El modelo de calidad de McCall
Son formas y metricas para evaluar calidad de un software

Los factores del señor macol
	Revision del producto, facilidad de recibir mantenimiento, flexibilidad y que yo lo pueda probar bien y que no se me rompa.
	Transicion del producto. Que sea portable, no anda en mi maquina. nos queremos pasar a linux y no podemos por la base de datos.
	Operacion del producto. del lado del usuario, sea confiable se pueda corregir, usabilidad, eficiente

#### ISO 9126

Estandar de la iso para evaluar la calidad de un software. Establece seis caracteristicas principales para medir la calidad de un software

- Funcionalidad
	- adecuacion, cumple las necesidades del usuario
	- Exactitud, resultados correctos
	- Interoperabilidad, se puede integrar con otros sistemas
	- Seguridad, protege los datos y el acceso
	- Cumplimiento Sigue las normativas y estandares
- Confiabilidad. capacidad par afuncionar sin fallas
	- Madurez, minimiza los errores y fallos
	- Tolerancia a fallos. isque funcionando a pesar de los problemas. pasa si los problemas no son los principales
	- Recuperabilidad, se puede restaurar despues de una falla.
- Usabilidad
	- facil de entender, aprender usar, comodo, diseño amigable
- Eficcienica
	- que sea rapido, el uso de recursos sea que consuma poco
- Facil de recibir mantenimiento
	- que se pueda modificar sin modificar el funcionamiento. facil de cambiar, no genera errores al actualizarse, facil de testear. que se identifiquen errores o mejoras
- Portabilidad
	- que sea trasladable a diferentes entornos
	- por que triunfaron las aplicaciones web, porque en todos lados funciona igual se inplementa igual.

### dilema de la calidad

si haces algo de mala calidad nadie te lo copmra
si haces algo demasiado bueno es muy caro y tardas mucho y nadie te lo compra

Software suficientemente nuevo. muchas emprezan priorizan la velocidad de lanzamiento que los errores los arreglen despues. Como windows que hicieron windowses muy malos como el 2000, que era un lio porque era malisimo y tenias que ir a buscar el parche y todo.
La metodologia de microsoft era. venia la de marketing decia por donde vamos? bueno termina eso y ta

Costo de la calidad. La calidad tiene un costo. pruebas, revisiones, mantenimiento  mejoras incrementan el presupuesto.

Riesgos. un software de baja calidad puede generar fallos crieticos

Negiligencia. Cuando un software tiene una falla grave se busca un responsable
quien fue?

Calidad y seguridad. el sofwtare malo es vulnerable.

Las decisiones de directivos influyen en la calidad del  software. si hago el lanzamiento rapido va tener menos pruebas y por ende menos calidad.


## OBJETIVO DEL TESTING
Encontrar la mayor cantidad de fallos que mas claidad le agregen al prroducto, aquellos que mas le molestaran la cliente

#### QA vs QC

Quality assurance, objetivo garantizar que producto cumpla con los estandares. lo que dice que hay que hacer. **prevenir** defectos

Quality conttrol es probar en si. identificar y corregir los defetos


el qa es el que establece un plan de pruebas.
define los estandares de codificacion y metodologia
revisiones de codigo para detectar errores antes de que lleguen a prod

Asegura que los procesos de desarrollo tengan los menor errores

QC.
aca esta el testing. los testers ejecutan pruebas funcionales. se reportan defectos en un documento.
Qc encuentra y documenta errores que hay que corregirse antes del lanzamiento.