numero = float(input("digite el numero: "))
parte_entera=int(numero)
parte_decimal=int((numero-parte_entera)*1000)
i1=parte_entera//100
i2=(parte_entera%100)//10
i3=(parte_entera%100)%10
d1=parte_decimal//100
d2=(parte_decimal%100)//10
d3=(parte_decimal%100)%10
ri=i1+i2+i3
rd=d1+d2+d3
print("la suma de la parte entera es: ",ri)
print("la suma de la parte decimal es: ",rd)
if(ri>rd):
    print("la parte entera es mayor que la parte decimal")
elif(rd==ri):
    print("la parte entera y la parte decimal son iguales")
else:
    print("la parte decimal es mayor que la parte entera")