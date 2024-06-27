# Menú de la calculadora
print("Bienvenido a la calculadora básica")
print("----------------------------------")
print("Seleccione una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# Lista de operaciones válidas
operaciones=[1,2,3,4]

# Pedir la opción del usuario
opcion=int(input("\nInserte el número de la operación  que desea realizar: "))

# Verificar si la opción es válida
if opcion not in operaciones:
    print("Error: Inserte un número válido.")
else:
    # Solicitar los números para operar
    primero_numero=int(input("\nInserte un número: "))
    segundo_numero=int(input("Inserte otro número: "))

    # Realizar la operación seleccionada
    if opcion==1:
        resultado=primero_numero+segundo_numero
        print(f"El resultado es: {resultado}")
    elif opcion==2:
        resultado=primero_numero-segundo_numero
        print(f"El resultado es: {resultado}")
    elif opcion==3:
        resultado=primero_numero*segundo_numero
        print(f"El resultado es: {resultado}")
    elif opcion==4:
        if segundo_numero==0:
            print("Error: No se puede dividir entre cero.")
        else:
            resultado=primero_numero/segundo_numero
            print(f"El resultado es: {resultado:2.f}") # Mostrar la división solo con 2 decimales