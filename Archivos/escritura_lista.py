lista = ["El niagara en bicicleta", "thriller", "smooth criminal", "la travesia", "Oh que sera"]
ubicacion = "C:\\Users\\B09S202est\\Desktop\\Archivos"
modo = "x"

nombre_archivo = "canciones.txt"
fp = open(ubicacion + "\\" + nombre_archivo, modo, encoding="utf-8")
#fp.writelines(lista)
for cancion in lista:
    fp.write(cancion+ "\n")
fp.close()

