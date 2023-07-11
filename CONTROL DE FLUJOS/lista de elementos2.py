## Pedir a un usuario una lista de elementos 
## Si en la lista contiene la palabra disco 
## Mostrar la palabra y la ubicacion de su indice positivo
lista=[]
while len (lista) < 5:
    IngresaDato=input("ingresa un dato: ")
    lista.append(IngresaDato)
indice=lista.index("disco")
print(lista[indice])
print("se encuentra en el indice numero: ",indice)