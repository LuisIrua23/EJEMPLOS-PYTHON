import random

def generar_numeros_hasta_negativo():
    contador_pares = 0

    while True:
        numero = random.randint(-9, 9)
        print(f"Número generado: {numero}")

        if numero < 0:
            break

        if numero % 2 == 0:
            contador_pares += 1

    print(f"Cantidad de números pares generados: {contador_pares}")

generar_numeros_hasta_negativo()