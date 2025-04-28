
def digitos(num):
    c = 0

# Si el número es 0, tiene 1 dígito
    if num == 0:
        c = 1
    else:
    # Mientras el número sea mayor que 0
        while num > 0:
            num = num // 10  # Elimina el último dígito
            c = c + 1  # Incrementa el contador
    return c  # Devuelve la cantidad de dígitos


numero = int(input("Digite un número: "))
resultado = digitos(numero)
print(f"La cantidad de dígitos  es:",resultado)

