import csv

print("Hola! Soy un chatbot de informacion sobre pokemon o no se")

print("¿En que puedo ayudarte? Si queres salir, solo di 'salir'")

pregunta = input()

#El bot sigue preguntando hasta que se le pida salir
while pregunta != "salir":

      preguntaEsta = False

      with open('preguntas.csv', mode ='a+') as archivo: #Abrir el archivo

            archivo.seek(0)
            archivoCsv = csv.DictReader(archivo) #Esto convierte el archivo csv a un diccionario (un json mas o menos)

            #Buscar la pregunta ingresada en el archivo
            for fila in archivoCsv:
                  if (pregunta == fila["pregunta"]):
                        print(fila["respuesta"])
                        preguntaEsta = True
                        break
            if preguntaEsta==False:
                  print("No tengo la respuesta a esa pregunta! Me la anoto para la proxima vez.")
                  writer = csv.writer(archivo)
                  writer.writerow([pregunta, "Aun no tengo la respuesta a esta pregunta pero estamos trabajando en eso."]) #escribir la pregunta en el archivo


      print("¿En que puedo ayudarte? Si queres salir, solo di 'salir'")
      pregunta = input()
           

print("Gracias por usar el chatbot! Hasta luego!")