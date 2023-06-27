##un programa que me pida un numero y me calcule su factorial
#ejemplo si ingreso 5
# de salida me deberia imprimir 120
num = int(input("Ingresa un numero: "))
factorial = 1
if num < 0:
    print("lo siento, el factorial no esta difinido para numeros negativos.")
elif num == 0:
    print("El factorial de 0 es 1.")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("El factorial de",num,"es",factorial)

