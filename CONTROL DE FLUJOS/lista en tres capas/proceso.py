import entrada
while len(entrada.lista) <5:
    dato = input("ingresa un dato:")
    entrada.lista.append(dato)
for texto in range(0,len(entrada.lista)):
    if entrada.lista[texto] == 'disco':
        entrada.palabra=entrada.lista[texto]
        entrada.indice=texto