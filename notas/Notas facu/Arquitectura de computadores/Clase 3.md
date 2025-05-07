Hay varias formas de almacenar datos. Digital != Binario

Tipos de informacion:
- Externa (personas)
	- Sistema numerico decimal
	- Escritura
	- Sonido
	- Imagen
- Interna (compu)
	- Digital
		- Numeros
		- Caracteres 
		- Etc
	- Analogica
		- Ej. Sensores 


En los registros se codifica donde esta el bit mas significante

Ademas yo no puedo saber que significa el bit si no me dicen en que esta codificado

Por ejemplo microsoft tiene byte, word, double word, quadruple word


El sistema digital decimal es el seven segment
El sistema analogico es el velocimetro

Codigo de bloque es un codigo en el que distintas palabras tienen el mismo numero de simbolos 

Estandares:
1. Cambio unico
	1. (parece que son comandos para manejamiento de datos algo asi)
2. Caracteres alfanumericos
	1. (ascii)
3. Numeros
4. Decetctores / correctores de errores


Codigos de cambio continuo:
Son codigos que solo cambia un bit
Codigo ciclico: tambien¿


Codigos de caracteres alfanumericos:
Se asignan codigos a cada caracter mediante una tabal

Caracteristaicas: 
	Numero de bits en el codigo (fijo o variable)
	Numero de caracteres representable
	Asignacion de codigos a cada caracter ( the table)

Cuestiones de la codificacion:
Internazionalizacion
Cambia el pais el idioma la distribucion del teclado la fecha etc


National language support
Las bases de datos tienen una region para elegir o multiples

Importante: el ascii
Las minusculas en hexa son 20 mas que las mayusculas
Ademas estan en un rango las letras minusculas y las mayuscu en otro

El codigo ansi que usa windows
Es compatible con ascii
Y sirve para pasar por ejemplo la ñ a Ñ con el misom algoritmo


Despues estan los UTF
UTF-16 UFT-8 UTF-32
Es compatible con ascii
La A por ej es U+0041


Ahora si

Codificacion de numeros:
Naturales, enteros, reales, complejos, enteros y reales, cadena de caracteres

Magnitudes binarias (numeros naturales): se representan igual que en binario, en 8 bits tengo 2^8
Enteros binarios: codigo de signo, osea usas un bit para el signo entonces en 8 bits tengo la mitad de alcance

Parece q hay distintas codificaciones para el entero binario?
- Signo y magnitud: el MSB most significant bit representa el signo. 0 positivo 1 negativo y tiene 2 representaciones del 0
- Complemento a 1: hace lo mismo pero los numeros negativos se generan dando vuelta el valor de lnumoro positivo. El 1 y el -1 son el mismo numero dado vuelta se hace un NOT
- Complemento a 2: este no tiene doble representacion del 0.  Sse representan por el complemento a 2 de la magnitud. Parece q este es el q se usa.
- Binario desplazado: el objetiov es tener el 0 en el medio. Osea esta desplazado desde el -7 como 0. Lo q tiene es que es asimetrico


- Los reales hay muchisimas variantes. Esl mas comun es punto flotante: 
	- ![[Pasted image 20250325203929.png]]
	- Bit para el signo, parte significativa (mantisa), base, elevado a un epxonente que tiene su signo
	- Nosotro usamo IEEE 754
	- Ej. 
	- El exponente esta en binario desplazado
	- Por alguna razon hay un 1 implicito que no entendi muy bien por que
	- La fraccion se escribe 1/2, 1/4, y asi en binario
	- Osea ocmo que en binario pasas cada un?'9 t 4208 t 1567
	- En binario pasas tipo 3,5 es 11,1 porque el 3 es 11 y el 0,5 es 1 

No entendi nada la verdad wacho
Como que es fraccion osea 1, fraccion * 2 a la exponente

Nota: por alguna razon para pasar de decimal a octal se agarran de a 3 digitos
Como que el octal es grupos de tres bits

Me confunde porque nunca en mi vida vi binario , binario ni octal es lo mas raro del mundo


