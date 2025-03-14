numero = float(input("ingrese el numero: "))
entero = int(numero)
decimal=  numero - entero

if decimal >= 0.5:
    entero_mas_cercano = entero + 1
else:
    entero_mas_cercano = entero
print("el numero mas cercano al entero es: ",entero_mas_cercano)

