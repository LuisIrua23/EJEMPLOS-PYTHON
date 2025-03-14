edad = int(input("ingrese su edad: "))
if edad < 4:
    print(" entra gratis")
elif edad >= 4 and edad <= 18:
    print("paga 5 euros")
elif edad > 18:
    print("paga 10 euros")