def calcular_promedio(lista_numeros):
    ac = 0
    k = 0
    p = 0
    
    for numero in lista_numeros:
        if numero < 0:
            p = ac / k
            return p
            
            
        if numero == 0:
            return p
            
            
        else:
            ac = ac + numero
            k += 1
    return p

# Recolectar datos
numeros = []  # Creamos una lista para almacenar los números
for i in range(0, 100):
    numero = int(input("Ingrese un numero: "))
    numeros.append(numero)  # Agregamos cada número a la lista
    if numero <= 0:  # Si es 0 o negativo, terminamos de pedir números
        break

resultado = calcular_promedio(numeros)  # Pasamos la lista completa
print("El promedio es: ", resultado)



