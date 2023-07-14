# frutas=[]
# while len(frutas)<5:
#     nuevaFruta=input("ingresa una fruta: ")
#     frutas.append(nuevaFruta)
# print(frutas)

# def textoLargo(array):
#     longitudTexto=0
#     mostrarFruta=""
#     for index in range(0,len(array)):
#         if len(array[index]) > longitudTexto:
#             longitudTexto=len(array[index])
# textoLargo(frutas)


# frutas=[]
# while len(frutas)<5:
#     nuevaFruta=input("ingresa una fruta: ")
#     if nuevaFruta in frutas:
#         print("esta fruta ya existe, huevonaso, ingresa otro pendejo")
#     else:
#         frutas.append(nuevaFruta)

# def textoLargo(array):
#     longitudTexto=0
#     mostrarFruta=""
#     for index in range(0,len(array)):
#         if len(array[index]) > longitudTexto:
#             longitudTexto=len(array[index])
#             mostrarFruta=array[index]
#     return mostrarFruta

# print(textoLargo(frutas))


# frutas=[]
# while len(frutas)<5:
#     nuevaFruta=input("ingresa una fruta: ")
#     for fruta in frutas:
#         if len(nuevaFruta) == len(fruta):
#             print("misma longitud gilaso, ingrese otro: ")
#     if nuevaFruta in frutas:
#         print("esta fruta ya existe, huevonaso, ingresa otro pendejo")

#     else:
#         frutas.append(nuevaFruta)

# def textoLargo(array):
#     longitudTexto=0
#     mostrarFruta=""
#     for index in range(0,len(array)):
#         if len(array[index]) > longitudTexto:
#             longitudTexto=len(array[index])
#             mostrarFruta=array[index]
#     return mostrarFruta

# print(textoLargo(frutas))


###continue
# frutas=[]
# while len(frutas)<5:
#     nuevaFruta=input("ingresa una fruta: ")
#     for fruta in frutas:
#         if len(nuevaFruta) == len(fruta):
#             print("misma longitud gilaso, ingrese otro: ")
#             continue
#     if nuevaFruta in frutas:
#         print("esta fruta ya existe, huevonaso, ingresa otro pendejo")
#         continue
#     frutas.append(nuevaFruta)

# def textoLargo(array):
#     longitudTexto=0
#     mostrarFruta=""
#     for index in range(0,len(array)):
#         if len(array[index]) > longitudTexto:
#             longitudTexto=len(array[index])
#             mostrarFruta=array[index]
#     return mostrarFruta

# print(textoLargo(frutas))



frutas=[]
contador=0
while contador<5:
    nuevaFruta=input("ingresa una fruta: ")
    for fruta in frutas:
        if len(nuevaFruta) == len(fruta):
            print("misma longitud gilaso, ingrese otro: ")
            continue
    if nuevaFruta in frutas:
        print("esta fruta ya existe, huevonaso, ingresa otro pendejo")
else:
    frutas.append(nuevaFruta)
    contador = contador + 1

def textoLargo(array):
    longitudTexto=0
    mostrarFruta=""
    for index in range(0,len(array)):
        if len(array[index]) > longitudTexto:
            longitudTexto=len(array[index])
            mostrarFruta=array[index]
    return mostrarFruta

print(textoLargo(frutas))

##identificar el indice 


