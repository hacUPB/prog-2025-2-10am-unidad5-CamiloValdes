fp = open("./Archivos/ejercicio1.txt","r")
fp.seek(10)
datos = fp.readline()
fp.close()
print(datos)


#datos = fp.read(34)
#print(datos)
#datos = fp.read(5)
#print(datos)
#datos = fp.read(25)
#print(datos)
#fp.close()