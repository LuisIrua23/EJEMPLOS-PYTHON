puntos = float(input("digite sus puntos: "))
puntos == 0.0 or puntos ==0.4 or puntos >= 0.6
if puntos == 0.0:
    print("el beneficio es cero")
    print("nivel inaceptable")
elif puntos == 0.4:
    print("su beneficio es: ", puntos*2400)
    print("nivel aceptable")
elif puntos >= 0.6:
    print("su beneficio es: ", puntos*2400)
    print("nivel meritorio")
else:
    print("valor no valido")
