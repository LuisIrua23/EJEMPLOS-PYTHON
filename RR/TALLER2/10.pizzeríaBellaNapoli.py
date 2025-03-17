# peperoni = 1
# jamos = 2
# salmon = 3
# pimiento = 4
# tofu = 5

# \n\t salto de linea con tabulador

print(" \n\tBienvenido a Pizzería Bella Napoli\n\t")
print(" \n\tSelecciona tu preferncia!! ")
opcion = int(input("\n\t1- pizza vegetariana  \n\t2- pizza no vegetariana:\n\t\n\topcion seleccionada:\n\t"))
if opcion == 1:
    print("Ingredientes de pizza vegetariana\n\t1- Pimiento\n\t2- Tofu\n")
elif opcion == 2:
    print("Pizza no Vegetariana")
    print(" Ingredientes de pizza no vegetariana:\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón")

else:
    print("Opción no válida")
if opcion == 1:
    ingrediente = int(input("selecciona el ingrediente:\n\t"))
    if ingrediente == 1:
        print(" pizza vegetariana con pimiento, mozarrella y tomate\n\t")
    elif ingrediente == 2:
        print("pizza vegetariana con tofu, mozarrella y tomate\n\t")
if opcion == 2:
    ingrediente = int(input("selecciona el ingrediente \n\t"))
    if ingrediente == 1:
        print("pizza no vegetariana con peperoni, mozarrella y tomate\n\t")
    elif ingrediente == 2:
        print("pizza no vegetariana con jamon, mozarrella y tomate\n\t")
    elif ingrediente == 3:
        print("pizza no vegetariana con salmon, mozarrella y tomate\n\t")
    else:
        print("opcion no valida")