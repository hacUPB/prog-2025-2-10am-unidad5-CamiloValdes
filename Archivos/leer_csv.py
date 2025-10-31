'''
import csv

with open('C:\\Users\\B09S202est\\Desktop\\variables.csv', 'r') as csvfile:   #usamos el manejador de contexto
    lector = csv.reader(csvfile, delimiter=";") #se utiliza el método reader    # delimiter=";" para cambiar el delimitador 
    encabezado = next(lector)           #
    presion = []
    print(encabezado)
    for fila in lector:          #con el for se itera sobre el objeto para leer
        dato = int(fila[0])
        presion.append(dato)
print(presion)
''' 


import csv

with open('C:\\Users\\B09S202est\\Desktop\\variables.csv', 'r') as csvfile:   #usamos el manejador de contexto
    lector = csv.reader(csvfile, delimiter=";") #se utiliza el método reader    # delimiter=";" para cambiar el delimitador 
    encabezado = next(lector)           #
    presion = []
    print(encabezado[3])
    for fila in lector:          #con el for se itera sobre el objeto para leer
        fila[3] = fila[3].replace(',', '.') #Para cambiar la coma por punto en la fila 3          
        dato = float(fila[3])
        presion.append(dato)
print(presion)
        