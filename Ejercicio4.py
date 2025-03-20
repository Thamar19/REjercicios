#Calcula la suma de todos los numeros pares del 1 al 100
numero = int(input("Ingresa un numero par:"))
suma = 0
i = 1
for i in range(1, 101):
    if i % 2 == 0:
        suma += i
print(suma)
 
true = i  % 2 == 0
if true: 
    print ("El numero ingresado es par")
else: 
    print ("El numero ingresado es impar")
