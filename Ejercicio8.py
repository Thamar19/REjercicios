# imprima la serie de Fibonacci hasta el enésimo término
n = int(input("Ingresa el número de términos de la serie de Fibonacci: "))
while n <= 0:
    n = int(input("Por favor, ingresa un número entero positivo: "))

# Inicializar los dos primeros términos de la serie
a, b = 0, 1

# Imprimir la serie de Fibonacci
print(f"\nSerie de Fibonacci hasta el término {n}:\n")

for _ in range(n):
    print(a, end=" ") 
    a, b = b, a + b  
