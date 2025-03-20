# Solicitar al usuario un número entero positivo
while True:
    try:
        num = int(input("Ingresa un número entero positivo: "))
        if num > 0:
            break  # Si el número es positivo, salimos del bucle
        else:
            print("Por favor, ingresa un número mayor que 0.")
    except ValueError:
        print("Eso no parece un número entero. Inténtalo de nuevo.")

# Imprimir los números impares desde 1 hasta el número ingresado
print(f"\nNúmeros impares del 1 al {num}:\n")

i = 1 
while i <= num:
    print(i)
    i += 2
print("\nFin del programa")
