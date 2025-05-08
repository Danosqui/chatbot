import csv

print("Hola! Soy un chatbot de informacion sobre pokemon o no se")

print("¿En que puedo ayudarte? Si queres salir, solo di 'salir'")

pregunta = input()


while pregunta != "salir":

      preguntaEsta = False
      with open('preguntas.csv', mode ='r') as archivo:
            archivoCsv = csv.DictReader(archivo)

            for fila in archivoCsv:
                  if (pregunta == fila["pregunta"]):
                        print(fila["respuesta"])
                        preguntaEsta = True
                        break
      
      if preguntaEsta == False:
      
            print("No tengo la respuesta a esa pregunta! Me la anoto para la proxima vez.")
            with open('preguntas.csv', mode='a') as archivo:

                  writer = csv.writer(archivo)
                  writer.writerow([pregunta, "Aun no tengo la respuesta a esta pregunta pero estamos trabajando en eso."])

      print("¿En que puedo ayudarte? Si queres salir, solo di 'salir'")
      pregunta = input()
           

print("Gracias por usar el chatbot! Hasta luego!")