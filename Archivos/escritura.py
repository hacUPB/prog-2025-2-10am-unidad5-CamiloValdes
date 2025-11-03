ubicacion = "C:\\Users\\B09S202est\\Desktop\\Archivos"
nombre_archivo = "frutas2.txt"
modo = "x" #Solo escritura - sobreescribe                                   
fp = open(ubicacion+"\\"+nombre_archivo, modo, encoding="utf-8")
frase = input("Por favor ingresa una frase: ")
fp.write(frase)
fp.write("\n")
#Solicitar una variable entera y una float al usuario y la escriben en el archivo 
edad = int(input("Ingrese su edad: "))
fp.write(str(edad))
fp.write("\n")
estatura = float(input("Ingrese su estatura: "))
fp.write(str(estatura)) #Para escribir lo que ingresó el usuario en el archivo
fp.write("\n")     #Para que las cosas aparezcan ordenadas 
fp.close()
