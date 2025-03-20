# Solicitar al usuario un número entero
num = int(input("Ingresa un número para ver su tabla de multiplicar: "))

# Imprimir la tabla de multiplicar del número ingresado
print(f"\nTabla de multiplicar del {num}:")

for i in range(1, 11): 
    resultado = num * i
    print(f"{num} x {i} = {resultado}")