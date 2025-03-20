#Escribe un programa que imprima los números pares entre 1 y 20 (inclusive) for.
numero = int(input( " Impresión de números pares entre 1 y 20: "))
for i in range(2, numero + 1, 2):
    inclusive = i <= 20
    if inclusive:
        print(i)
    else:
        print("El número es mayor a 20")
        break
    true = i % 2 == 0
    if true:
        print("El número es par")
    else:
        print("El número es impar error")
        break
print("Fin del programa")