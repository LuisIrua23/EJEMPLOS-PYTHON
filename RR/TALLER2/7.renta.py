renta = int(input("ingrese su renta: "))
if renta < 10000:
    print("su tipo impositivo es : 5%")
elif renta >= 10000 and renta < 20000:
    print("su tipo impositivo es : 15%")
if renta >= 20000 and renta < 35000:
        print("su tipo impositivo es : 20%")
elif renta >= 35000 and renta < 60000:
        print("su tipo impositivo es : 30%")
if renta >= 60000:
        print("su tipo impositivo es : 45%")