#NUMEROS AMIGOS 220 Y 284
vec_a = []
vec_b = []
num1 = 0
num2 = 0
sum_1 = 0
sum_b = 0
num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un numero: ")) 
for i in range(1,num1):
    if num1 % i == 0:
        vec_a.append(i)
        print(i)

print("------------")

for i in range(1,num2):
    if num2 % i == 0:
        vec_b.append(i)
        print(i,)


for k in vec_a:
    sum_1 = sum_1 + k
for k in vec_b:
    sum_b = sum_b + k

if sum_1 == num2 and sum_b == num1:
    print("son numeros amigos")
else:
    print("no son numeros amigos")



# print(i, end=" ")




    