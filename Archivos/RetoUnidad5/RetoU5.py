import os, csv, matplotlib.pyplot as plt        

def listar():
    ruta = input("Ruta (Enter para actual): ")              
    if ruta == "": ruta = os.getcwd()
    for f in os.listdir(ruta):              # Abre la carpeta indicada y mira cada cosa
        print(f)

def procesos_txt():
    ruta = input("Archivo .txt: ")
    print("1. Contar palabras y los caracteres")
    print("2. Reemplazar palabra")
    print("3. Histograma de vocales")
    op = input("Opción: ")

    if not os.path.exists(ruta):        # Verifica si el archivo existe, si no existe, manda un mensaje y regresa al menú
        print("No existe el archivo."); return

    with open(ruta, "r", encoding="utf-8") as a:
        texto = a.read()            # Lee todo el archivo y lo guarda en la variable texto

    if op == "1":
        print("Palabras:", len(texto.split()))
        print("Caracteres con espacios:", len(texto))
        print("Caracteres sin espacios:", len(texto.replace(" ", "")))

    elif op == "2":
        buscarp = input("Palabra que se desea buscar: ")
        nueva = input("Nueva palabra: ")
        nuevo = texto.replace(buscarp, nueva)
        with open(ruta, "w", encoding="utf-8") as a:        # Para reemplazar la palabra
            a.write(nuevo)                          # Guarda los cambios
        print("Palabra reemplazada satisfactoriamente.")

    elif op == "3":
        texto = texto.lower()
        vocales = ["a","e","i","o","u"]
        conteo = []
        for v in vocales:
            cantidadv = texto.count(v)       # Veces en el texto
            conteo.append(cantidadv)
        plt.bar(vocales, conteo, color="orange")        #Uso  de IA para la grafica
        plt.title("Histograma de Vocales")
        plt.show()

def calcular_promedio(datos):
    return sum(datos) / len(datos)

def calcular_mediana(datos):        #IA para calcular la mediana
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    if n % 2 == 0:
        return (datos_ordenados[n//2-1] + datos_ordenados[n//2]) / 2
    else:
        return datos_ordenados[n//2]

def calcular_desviacion(datos, promedio):
    suma_cuadrados = 0
    for dato in datos:
        suma_cuadrados += (dato - promedio) ** 2
    return (suma_cuadrados / (len(datos) - 1)) ** 0.5

def procesar_csv():
    ruta = input("Archivo .csv: ")
    print("1. Mostrar primeras 15 filas")
    print("2. Calcular estadísticas de una columna")
    print("3. Graficar columna")
    op = input("Opción: ")

    if not os.path.exists(ruta):
        print("No existe el archivo."); return

    with open(ruta, newline="", encoding="utf-8") as a:
        lector = list(csv.reader(a))

    if op == "1":
        for fila in lector[:15]:
            print(fila)

    elif op == "2":
        col = int(input("Número de columna: "))
        datos = []
        for fila in lector[1:]:
            try: datos.append(float(fila[col])) #Uso de la IA
            except: pass
        if len(datos) > 0:
            promedio = calcular_promedio(datos)
            print("Cantidad:", len(datos))
            print("Promedio:", promedio)
            print("Mediana:", calcular_mediana(datos))
            print("Máximo:", max(datos))
            print("Mínimo:", min(datos))
            if len(datos)>1: 
                print("Desv.Est:", calcular_desviacion(datos, promedio))
        else:
            print("No hay datos numéricos válidos.")

    elif op == "3":
        colu = int(input("Número de columna: "))
        datos = []
        for fila in lector[1:]:
            try:
                datos.append(float(fila[colu]))
            except:
                pass

        if len(datos) > 0:
            plt.scatter(range(len(datos)), datos, color="blue")
            plt.title("Gráfico de Dispersión de la Columna")
            plt.xlabel("Índice")
            plt.ylabel("Valor")
            plt.show()

            plt.bar(range(len(sorted(datos))), sorted(datos), color="orange")
            plt.title("Gráfico de Barras (Datos Ordenados)")
            plt.xlabel("Índice")
            plt.ylabel("Valor")
            plt.show()
        else:
            print("No hay datos válidos para graficar.")

while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Listar archivos")
    print("2. Procesar .txt")
    print("3. Procesar .csv")
    print("4. Salir")
    op = input("Opción: ")
    if op=="1": listar()
    elif op=="2": procesos_txt()
    elif op=="3": procesar_csv()
    elif op=="4": break
    else: print("Opción no válida.")