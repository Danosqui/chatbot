import csv

print("hola")

pregunta = input("pone tu pregunta: ")

with open('preguntas.csv', mode ='r') as file:    

       csvFile = csv.DictReader(file)

       for filas in csvFile:
            if (pregunta == filas["pregunta"]):
                  print(filas["respuesta"])