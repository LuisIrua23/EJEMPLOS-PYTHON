def imprimir_divisores(numero):
    
    for i in range(1, numero + 1):
        if numero % i == 0:  # Si el resto de la división es 0, es un divisor
            print(i)

# Leer el número del usuario
num = int(input("Ingrese un número: "))
print(f"Los divisores de {num} son:")
# Llamar a la función
imprimir_divisores(num)
