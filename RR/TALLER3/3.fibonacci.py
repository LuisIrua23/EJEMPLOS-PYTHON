numero = int(input("digite un numero: "))
a = 1 
b = 0
f = 0
i = 1
for i in range(numero):
    f = a+b
    a = b
    b=f
    print(f)