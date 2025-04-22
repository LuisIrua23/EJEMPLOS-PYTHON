numero = int(input("ingrese un numero: "))
d = 0
nn = 0
# for i in range(numero):
if numero > 0:

    d = numero % 10
    numero = numero // 10
    nn = nn * 10 + d
else:
    numero = nn
    print("mostrar: ",numero)
