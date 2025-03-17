print("numeros primos")
#numetros divisibles por 1 y por si mismos
#los que solo tienen 2 divisores
#entero y positivo y mayor que 1
#ejemplo 2,3,5,7,11,13,17,19
#6
# 6 % 2 = 0
# 6 % 3 = 0
# 6 % 4 = 2
# 6 % 5 = 1
# 6 No es numero primo
#7
# 7 % 2 = 1
# 7 % 3 = 1
# 7 % 4 = 3
# 7 % 5 = 2
# 7 % 6 = 1
# 7  es numero primo
#num = int(input("ingrese un numero: "))


def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True

numero = int(input("ingrese un numero: "))
#for numero in range(2,10):
if es_primo(numero):
        print(numero , "es primo: ")
else:
        print(numero , "no es primo: ")
