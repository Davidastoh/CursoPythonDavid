# ## Pedir a un usuario una lista de elementos 
# ## Si en la lista contiene la palabra disco 
# ## Mostrar la palabra y la ubicacion de su indice positivo

# lista = []

# for i in range(5):
#     elemento = input("Ingresa un elemento: ")
#     lista.append(elemento)

# if "disco" in lista:
#     indices = [i for i, x in enumerate(lista) if x == "disco"]
#     print("La palabra 'disco' se encuentra en los siguientes índices positivos:")
#     for indice in indices:
#         print(f"Índice: {indice}, Palabra: {lista[indice]}")
# else:
#     print("La palabra 'disco' no se encuentra en la lista.")

# ## lista de elementos

# lista=[]
# while len (lista) < 5:
#     IngresaDato=input("ingresa un dato: ")
#     lista.append(IngresaDato)
# indice=lista.index("disco")
# print(lista[indice])
# print("se encuentra en el indice numero: ",indice)

# lista de elementos

lista=[]
indice= 0
palabra=""
while len(lista) <5:
    dato = input("ingresa un dato:")
    lista.append(dato)
for texto in range(0,len(lista)):
    if lista[texto] == 'disco':
        palabra=lista[texto]
        indice=texto
print(f"""el texto disco se encuentra en el indice {indice} y el texto es {palabra}""")

 


