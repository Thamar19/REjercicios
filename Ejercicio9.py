# Solicitar al usuario un número entero positivo
while True:
    try:
        num = int(input("Ingresa un número entero positivo para calcular su factorial: "))
        if num >= 0:
            break  # Si la entrada es válida, salir del bucle
        else:
            print("Por favor, ingresa un número igual o mayor a 0.")
    except ValueError:
        print("Eso no parece un número entero. Inténtalo de nuevo.")

# Calcular el factorial con un bucle while
factorial = 1
i = num
while i > 1:
    factorial *= i 
    i -= 1  

print(f"\nEl factorial de {num} es: {factorial}")