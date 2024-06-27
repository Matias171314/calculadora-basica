import sys

# Menú de la calculadora
print("Bienvenido a la calculadora básica")
print("----------------------------------")
print("Seleccione una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("\n0. Salir")

# Lista de operaciones válidas
operaciones=["Salir","Suma","Resta","Multiplicación","División"]

# Función para pedir la opción del usuario con manejo de errores
def pedir_opcion(operaciones):
    """list -> int
    OBJ: Solicita al usuario una opción válida de operación.
    PRE: 'operaciones' es una lista definida con 5 operaciones."""
    while True:
        try:
            opcion=int(input("\nInserte el número de la operación  que desea realizar: "))
            if opcion not in range(len(operaciones)):
                print("\nError: Inserte una opción de operación válida.")
                continue # Vuelve al inicio del bucle para solicitar la opción nuevamente
            break # Sale del bucle si la opción es válida
        except ValueError:
            print("\nError!: Inserte un valor válido (número entero).")
        except KeyboardInterrupt:
            print("\nOperación interrumpida por el usuario.")
            sys.exit() # Termina el programa si el usuario interrumpe la operación (Ctrl+C)
    return opcion

# Función para pedir los números a operar con manejo de errores
def pedir_numeros():
    """None -> tuple
    OBJ: Solicita al usuario dos números enteros para operar.
    PRE: No hay precondiciones específicas."""
    while True:
        try:
            primero_numero=int(input("Inserte un número: "))
            segundo_numero=int(input("Inserte otro número: "))
            break # Sale del bucle si la opción es válida
        except ValueError:
            print("\nError!: Inserte un valor válido (número entero).")
        except KeyboardInterrupt:
            print("\nOperación interrumpida por el usuario.")
            sys.exit() # Termina el programa si el usuario interrumpe la operación (Ctrl+C)
    return primero_numero, segundo_numero

# Función para calcular operaciones con dos números
def calcular_operacion(opcion, numero1, numero2):
    """int, int, int -> None
    OBJ: Realiza la operación matemática seleccionada por el usuario e imprime el resultado.
    PRE: 'opcion' es un entero que representa la operación seleccionada ('1' para suma, '2' para resta, etc.)."""
    if opcion == 1:
        resultado = numero1 + numero2
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == 2:
        resultado = numero1 - numero2
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == 3:
        resultado = numero1 * numero2
        print(f"El resultado de la multiplicación es: {resultado}")
    elif opcion == 4:
        if numero2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            resultado = numero1 / numero2
            print(f"El resultado de la división es: {resultado:.2f}")  # Mostrar la división con 2 decimales


# Utilizamos las funciones para pedir los valores
opcion=pedir_opcion(operaciones)

# Salir si la opción es 0
if opcion == 0:
    sys.exit()
else:    
    # Imprimir el rótulo de la operación centrado entre guiones
    operacion_rotulo = f"{operaciones[opcion]}".center(34, "-")
    print(operacion_rotulo)

# Si la opción no es salir, pedimos los números y realizamos la operación
numero1, numero2=pedir_numeros()

# Realizar la operación seleccionada
print("----------------------------------")
calcular_operacion(opcion, numero1, numero2)