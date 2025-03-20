# Definir la contraseña correcta
contraseña_correcta = "segura123"

# Solicitar al usuario que ingrese la contraseña
while True:
    contraseña_ingresada = input("Ingrese la contraseña: ")

    if contraseña_ingresada == contraseña_correcta:
        print("Contraseña correcta. Acceso concedido.")
        break # Si la contraseña es correcta, salir del bucle
    else:
        print("Contraseña incorrecta. Inténtelo de nuevo.")
