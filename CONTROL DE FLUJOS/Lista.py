##crear un programa que me deje ingresar datos en una lista vacia
# Creamos una lista vacía
lista =[]
def ingresar_datos():
    while True:
        dato = input("Ingresa un dato (o 'salir' para terminar): ")
        if dato.lower() == "salir":
            break
        lista.append(dato)

ingresar_datos()

print("La lista fcompleta es:", lista)