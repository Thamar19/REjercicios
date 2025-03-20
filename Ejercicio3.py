#Cuantos digitos tiene un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))
n = numero
if n < 0:
    n = n * -1
    print("El número es negativo")
else:
    print("El número es positivo")
contador = 0
while n != 0:
    n = n // 10
    contador += 1
print("El número tiene", contador, "dígitos")