def dividir(n1, n2):
    
    if n2 == 0:
        return "Error: Division por cero no permitida"
    else:
        return n1 / n2
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

r = dividir(a, b )
print("La dividion de", a, "y", b, "es:", r)