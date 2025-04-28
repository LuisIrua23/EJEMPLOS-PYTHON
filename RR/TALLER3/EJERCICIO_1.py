def promedio():
    ac = 0
    k = 0
    p = 0
    for i in range(0, 100):
        numero = int(input(" ingrese un numero: "))
        if numero < 0:
            p = ac / k
            return p
        if numero == 0:
            return p
        else:
            ac = ac + numero
            k = k + 1
    return p

r= promedio()
print("el promedio es: ", r)