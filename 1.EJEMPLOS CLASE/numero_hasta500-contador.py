import random
t = x= random.randint(10,99)
km = 0
while (t % 3!= 0):
    t += 1
km = 1
while (t < 500):
    km += 1
    t += 3
print("Numero generado:",x)
print("Multiplos de 3 entre: " ,x, " y 500: ", km)
