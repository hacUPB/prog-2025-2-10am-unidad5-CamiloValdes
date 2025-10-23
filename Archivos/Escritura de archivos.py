

nombre = ['Camilo','Rogelio','Carlos']
edad = [18, 19, 20]
ciudad = ['Los Angeles', 'Medellín', 'Villagarzon']


import csv

with open('salida.csv', 'w',) as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['Nombre', 'Edad', 'Ciudad'])  # Escribe la fila de encabezados
    escritor.writerow(['John', 25, 'Nueva York'])
    escritor.writerow(['Jane', 30, 'Los Ángeles'])
    escritor.writerow(nombre)
    escritor.writerow(edad)
    escritor.writerow(ciudad)