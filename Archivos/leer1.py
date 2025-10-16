# 1. Abrir el archivo y definir el modo
archivo = open("./Archivos/texto.txt","r")     #archivo es una variable, no una funcion, la funcion es open()
# 2. Leer el archivo
# datos = archivo.read()
#for i in range(5):
 #   datos = archivo.read()
#for datos in archivo:
#    print(datos[0])
datos = archivo.readlines()
print(datos)
# 3. Cerrar el archivo
archivo.close()
