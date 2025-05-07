
'''la respuesta comienza como un SI hardcodeado para que se ejecute el
while la primera vez.'''
respuesta = "SI"

#las variables declaradas fuera del while son aquellas que se necesitan al final
cantCarreras = 0

cantCarreras5Km = 0

longitudRecorridoCorto = 999999999
nombreRecorridoCorto = ""
tiempoRecorridoCorto = 0

#hasta que el usuario lo indique, se ingresan carreras
while respuesta=="SI":
    
    #se cuenta la carrera para la cantidad y se ingresan los primeros datos
    cantCarreras +=1
    print("---------------------------------")
    print("Carrera " + str(cantCarreras))
    nombreColegio = input("Ingrese el nombre del colegio: ")
    longitudKilometros = int(input("Ingrese la longitud del recorrido en Km: "))
    
    # si es mas larga que 5 km se cuenta para el total
    if longitudKilometros > 5:
        cantCarreras5Km += 1
    
    
    #se ingresa la velocidad promedio de cada participante y se define que el ganador es quien tiene corrio mas rapido
    velocidadGanadorKmH = 0
    velocidadCorredor = 1
    while velocidadCorredor > 0:
        velocidadCorredor = int( input("Ingrese la velocidad en kilometros por hora de los participantes (0 para terminar): "))   
        if velocidadCorredor > velocidadGanadorKmH:
            velocidadGanadorKmH = velocidadCorredor
    
    # se calcula el tiempo (en horas) que tarda el ganador en dar la vuelta al circuito
    tiempoGanadorHoras = longitudKilometros / velocidadGanadorKmH
    
    #se verifica si es la carrera mas corta una vez calculado el tiempo ya que es un dato que se pide
    if longitudKilometros<longitudRecorridoCorto:
        longitudRecorridoCorto = longitudKilometros
        nombreRecorridoCorto = nombreColegio
        tiempoRecorridoCorto = tiempoGanadorHoras
    
    respuesta = input("Ingreso de datos finalizado. Desea ingresar otra carrera? (SI/NO): ")
    
                      
#salida de todos los datos correspondientes
print("-------------------------------------------")
print ("Ingreso de carreras finalizado")
print ("Hay "+str(cantCarreras5Km) + " carreras mas largas que 5km")
print("la carrera mas corta fue la del colegio " + nombreRecorridoCorto + ", con " + str(longitudRecorridoCorto) + " km. El tiempo estimado que tardo su ganador es: " + str(tiempoRecorridoCorto) + " horas")
print("en total se ingresaron " + str(cantCarreras) + " carreras")
