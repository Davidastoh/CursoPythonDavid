lista = []

for i in range(5):
    elemento = input("Ingresa un elemento: ")
    lista.append(elemento)

if "disco" in lista:
    indices = [i for i, x in enumerate(lista) if x == "disco"]
    print("La palabra 'disco' se encuentra en los siguientes índices positivos:")
    for indice in indices:
        print(f"Índice: {indice}, Palabra: {lista[indice]}")
else:
    print("La palabra 'disco' no se encuentra en la lista.")
