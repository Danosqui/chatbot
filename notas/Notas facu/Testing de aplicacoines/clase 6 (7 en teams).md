[probablemnete no anote miucho si lee del ppt]

# Diseño de escenarios - casos de prueba

Es hacer los pasos para verificar que el sitema funcione co respecto a los requerimientos de negocio.
Requisitos funcionales son los que relevan los analistas
Los no funcionales son los tecnicos

Escenario de limite es decir cuantos usuarios vamos a tener en una aplicacion  como de limite
Escenarios de error y escenarios de pruebas de seguridad

## Los casos deprueba

Es los pasos entradas y condiciones, sabiendo que resultados tenemos que obtener y que estan diseñados para verificar una funcionalidad
Por ejemplo ingresar un numero de cuit, como se tiene que comportar el sistema? Cual es la respuesta esperada? Eso melo tiene que decir el tester

![[Pasted image 20250425190922.png]]
Ejemplo de caso de prueba

No se debe asumir, pero tampoco tiene que tener cosas que nada que ver
Por mas que sea redundante, no se debe asumir siempre hay que indicar.

Los casos de prueba la idea que sirvan para mas de una funcionalidad

El estado de la aplicacion (dentro de condiciones inciales) es tipo version beta y asi
Porque se soportan mas erroes ahi que en una release

[y yo no se si a tu perro le gusta bailar a lo bobo]

Hay que indicarle al tester absolutamente todo.

Tipos de casos de prueba: ( lo vimos)
Las funcionales 
No funcionales}
seguridad
Rendimiento
Regresion

A veces se puede automatizar los casos de prueba

El escenario de error es error para el cliente que le muestra error

Ah osea un escenario principal y tiene sus escenarios especificos de limite error y /o seguridad
Pero todo es 1 caso de prueba

Un requerimiento funcional describe las acciones y funciones que un sistema debe realizar para con el usuario y otros sistemas
Por ejemplo" el sistema debe permitir a los usuarios registrarse con nombre contraseña y email" " al hacer click en enviar la pagina redirecciona al usuario a la pagina de confirmacion" "el sistema deb ser capaz de alamcenar y recuparar informacion de los usuarios " "al ingresar datos invalidos el sistema dice error"
Lso requerimientos son la base para las pruebas funcionales  y dice n lo que el sistema debe hacer, y las pruebas verifican que el sistema funcione cumpla con los requerimientos

Muchas veces no solo esta lo que necsita el usuario sino lo que espera el usuario, lo que pretende el usuario que haga.
Que es lo que espera y **como** lo espera

# Como diseñar casos de prueba 


# Tecnicas de analisis funcional aplicado a causistica

La tabla modela combianciones de condiciones y sus acciones, lo veo todo en una tabla, cuando una funcionalidad depende de muchas reglas

El arbol de decision que no se entiende que tiene que ver con el testing es eso, un arbol pero con decisiones para resultados segun varibales
Ayuda a visualizar las decisiones para saber que probar
**Osea segun los valores de entrada lo que deberia pasar**.

## Clases de equivalencias

Clasificacion de los posibles casos de prueba en distintos grupos.
Grupos de casos de prueba, del mismo estilo
Casos que son similares prueban lo mismo o llegan al mismo tipo de error. Casos de pruebas **equivalentes** 
Por ejemplo, estamos probando una calculadora y sale bien 1+1, vale la pena 2+2? No

"esto es el analisis funcional"" mostrando un cuadro de texto (para tenre en cuenta cuando estudie de la ppt)

No se si esto es lo mismo pero esta mostrando como extraer los requerimientos de distintas frases separandolas de un testo
Y en base a cada caso o cada requermiento en cada caso hay un valido o no valido / cada condicion tiene sus casos, eso quise decir
Todas las clases de qeuivalencia validas tienen que estar cubiertas en el caso de prueba, tiene uqe incluir la mayor cantidad de clases posible

### Valores limite

Los errores pasan en los bordes del dominio de la entrada
En lugar de probar cualquier elemento de una clase, se prueba los bordes. 
Justo en los limites, apenas encima o debajo de los limites
(imagen ppt con los numeros)

Enfoque en los limites de entrada donde suelen fallar los sistemas

# Casos de uso  y de prueba

Son las descripciones de cosas que hace el usuario, de los que se derivan los casos de prueba [ por que no vimos esto antes que casos de prueba no lo se]
El caso de prueba dice ocmo tengo que hacer para obtener esto (caso de uso)
El caso de uso sirve para netender la logica de la aplicacion, y los caso de prueba esp ara identificar errores y asegurar que comple con los requis 

# Diagrama entidad relacion de caso de prueba 


# Matriz de trazabilidad

Trazabilidad es capacidad de hacer el recorrido inverso y optener el origen
La matriz es una reramienta para asegurarse que todos los requisitos estan cubiertos por los casos de prueba. E
# mejores practicas

