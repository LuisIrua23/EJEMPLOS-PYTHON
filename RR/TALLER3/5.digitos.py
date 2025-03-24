numero = int(input("digite un numero: "))
c = 0
for i in range(numero):
    if numero > 0:
       numero = numero // 10
       c = c + 1
else:
    print("la cantidad de digitos es: ", c)
    