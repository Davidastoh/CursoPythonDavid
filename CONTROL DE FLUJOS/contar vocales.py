## Y su indice positivo es 1

# lista=["a","e","i"]
# for indice,valor in enumerate(lista):
#     if valor == "i":
#         print(valor, indice)


## crear una lista con los numeros del 1 al 10
##crear una funcion que reciba como parametro dicha lista
#  y que retorne en una lista los numeros pares de la lista 
# ingresada por parametro

# lista=[1,2,3,4,5,6,7,8,9,10]
# def numeros_pares(array):
#     nueva_lista=[]
#     for _,num in enumerate(array):
#         if num%2==0:
#             nueva_lista.append(num)
#     return nueva_lista
# print(numeros_pares(lista))


##
# texto="Hola como estas?"
# print(list(texto))
# print(texto,.split(""))


##hacer un programa que pida al usuario un texto
#y evaluar con una funcion la cantidad de vocales a que tiene el texto:

def contar_vocales_a(texto):
    cantidad_a = 0
    for letra in texto:
        if letra.lower() == 'a':
            cantidad_a += 1
    return cantidad_a 

def main():
    texto = input("ingresa un texto:")
    cantidad_vocales_a = contar_vocales_a(texto)
    print("la cantidad de vocales 'a' en el texto es:",cantidad_vocales_a)

if __name__ == "__main__":
    main()



