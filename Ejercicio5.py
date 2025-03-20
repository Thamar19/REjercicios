# Solicitar al usuario un número entero
while True:
    try:
        num = int(input("Ingresa un número entero positivo: "))
        if num < 0:
            print("Ingresa un número entero positivo.")
        else:
            break  # Salir del bucle si la entrada es válida
    except ValueError:
        print("Error: Debes ingresar un número entero válido.")

# Imprimir los números en orden descendente hasta 0
print("\nContando desde", num, "hasta 0:")

while num >= 0:
    print(num)
    num -= 1  # Reducir el número en 1 en cada iteración

print("Fin del conteo.")