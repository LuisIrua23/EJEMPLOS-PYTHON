


import random
x = random.randint(5, 25)  # Generar número aleatorio entre 5 y 25
print("Número generado:", x)

def sumatoria(x):
    k = 1  # Inicializar k en 1
    ac = 0  # Inicializar acumulador en 0
    ac = ac + k  # Sumar k a la acumulación
    k += 1  # Incrementar k en 1
    while k <= x:  # Mientras k sea menor o igual a x
        ac = ac + k  # Sumar k a la acumulación
        k += 1  # Incrementar k en 1
    return ac  # Devolver el resultado de la sumatoria
print("La sumatoria de los números desde 1 hasta", x, "es:", sumatoria(x))  # Imprimir el resultado de la sumatoria


