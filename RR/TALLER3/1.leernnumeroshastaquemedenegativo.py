ac = 0
k = 0
p = 0
for i in range(0, 1000):
    numero = int(input(" ingrese un numero: "))
    if numero < 0:
        p = ac / k
        print("el promedio es: ", p)
    if numero == 0:
        print("el promedio es: ", p)
    else:
        ac = ac + numero
        k = k + 1