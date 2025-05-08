import csv

print("Hola! Soy un chatbot de informacion sobre pokemon o no se")

print("¿En que puedo ayudarte? Si queres salir, solo di 'salir'")

pregunta = input()


while pregunta != "salir":
      with open('preguntas.csv', mode ='r') as archivo:
            csvFile = csv.DictReader(archivo)

            preguntaEsta = False
            for filas in csvFile:
                  if (pregunta == filas["pregunta"]):
                        print(filas["respuesta"])
                        preguntaEsta = True
            if preguntaEsta == False:
                  print("No tengo la respuesta a esa pregunta! Me la anoto para la proxima vez.")
                  # writer = csv.writer(archivo)
                  # writer.writerow([pregunta, "No tengo la respuesta a esa pregunta!"])


            print("¿En que puedo ayudarte? Si queres salir, solo di 'salir'")
            pregunta = input()
           

print("Gracias por usar el chatbot! Hasta luego!")