nombre_archivo = "./Archivos/texto.txt"
ubicacion = "C:\\Users\\B09S202est\\Desktop\\Archivos"
with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    #Leer todas las lineas dentro de una lista
    lista = archivo.readlines()
for c in lista:
    print(c)
