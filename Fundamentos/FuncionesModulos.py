import ModuloMatematico

# 1. Funcion de conversion de divisa
# Funcion para convertir divisa
def convertirDivisa(cantidad, tasa):
    return cantidad * tasa

# Funcion main del punto

def conversorDivisa():
    cantidad = float(input('Ingrese la cantidad de dinero a convertir: '))
    tasaCambio = float(input('Ingrese la tasa de cambio: '))
    resultado = convertirDivisa(cantidad, tasaCambio)
    print(f'La cantidad convertida es: {resultado}')
    main()

# 2. Modulo de Operaciones Matematicas
# crearmos el archivo moduloMatematico.py

def operacionesMatematicas():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    print(f"La suma de {a} y {b} es {ModuloMatematico.suma(a, b)}")
    print(f"La resta de {a} y {b} es {ModuloMatematico.resta(a, b)}")
    print(f"La multiplicación de {a} y {b} es {ModuloMatematico.multiplicacion(a, b)}")
    if b != 0:
        print(f"La división de {a} y {b} es {ModuloMatematico.division(a, b)}")
    else:
        print("Error: División por cero no está permitida.")
    main()
    
# 3. Funcion Recursiva de Fibonacci
# Funcion para calcular el número de Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# Funcion main del punto

def Fibonacci():
    n = int(input("Ingrese un número entero: "))
    print(f"El número de Fibonacci para {n} es {fibonacci(n)}")
    main()

# Funcion principal del codigo
def main():
    print("1. Función de Conversión de Divisas")
    print("2. Módulo de Operaciones Matemáticas")
    print("3. Función Recursiva de Fibonacci")
    print("4. Salir")

    opcion = int(input("Seleccione una opción (1, 2, 3 o 4): "))
    
    if opcion == 1:
        conversorDivisa()
    elif opcion == 2:
        operacionesMatematicas()
    elif opcion == 3:
        Fibonacci()
    elif opcion == 4:
        print("Gracias por utilizar el programa.")
    else:
        print("Opción no válida. Por favor seleccione 1, 2, 3 o 4.")
        main()
        
main()