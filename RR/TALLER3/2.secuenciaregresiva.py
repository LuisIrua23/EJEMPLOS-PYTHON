numero = int(input("ingrese un numero: "))

invertir = str(numero)[::-1] + "0"
print(invertir)



# secuencia regrsiva
# numero = int(input("ingrese un numero: "))

# for i in range(numero, 0 , -1):
#     print(i)


# import random

# def generar_numero_8_digitos():
#     # Generar número de 8 dígitos entre 10000000 y 99999999
#     return random.randint(10000000, 99999999)

# def contar_digitos_pares_impares(numero):
#     # Convertir el número a cadena para analizar cada dígito
#     numero_str = str(numero)
    
#     # Inicializar contadores
#     pares = 0
#     impares = 0
    
#     # Contar dígitos pares e impares
#     for digito in numero_str:
#         digito_int = int(digito)
#         if digito_int % 2 == 0:
#             pares += 1
#         else:
#             impares += 1
    
#     return pares, impares

# # Generar número y contar dígitos
# numero = generar_numero_8_digitos()
# digitos_pares, digitos_impares = contar_digitos_pares_impares(numero)

# print(f"Número generado: {numero}")
# print(f"Dígitos pares: {digitos_pares}")
# print(f"Dígitos impares: {digitos_impares}")