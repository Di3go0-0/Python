

# 1. Registro de Usuarios
# Creamos una funcion para registrar usuarios 

def registrarUsuarios():
    nombre = input('Ingrese su nombre: ')
    edad = int(input('Ingrese su edad: '))
    with open("registro.txt", "a") as archivos:
        archivos.write(f'{nombre} {edad}\n')
        # open crea un archivo si no existe, si existe, abre el archivo
        # "a" es el modo de apertura, que es para agregar al final del archivo
        # write escribe en el archivo

# Funcion main del punto
def registroUsuarios():
    while True:
        registrarUsuarios()
        continuar = input('Desea registrar otro usuario? (s/n): ')
        if continuar.lower() == 'n':
            break
    print('Usuarios registrados correctamente')
    main()

# 2. Lector de poemas
def leerPoema():
    with open("poema.txt", "r") as archivo:
        for linea in archivo:
            print(linea, end="")

# Funcion main del ejercicio

def lectorPoemas():
    print("\nLeyendo poema:\n")
    leerPoema()
    main()

# 3. Analizador de log
def analizarLog():
    with open("registro.log", "r") as archivo:
        lineas = archivo.readlines()
    errores = [linea for linea in lineas if "ERROR" in linea]
    print(f"Se encontraron {len(errores)} errores en el registro.")
    for error in errores:
        print(error)
        main()

# Funcion main del ejercicio

def analizadorLogs():
    print("\nAnalizando registro:\n")
    analizarLog()
    main()

# Creamos la funcion main
def main():
    print("1. Registro de Usuarios")
    print("2. Lector de Poemas")
    print("3. Analizador de Log")
    print("4. Salir")
    opcion = int(input("Seleccione una opción (1, 2, 3 o 4): "))
    if opcion == 1:
        registroUsuarios()
    elif opcion == 2:
        lectorPoemas()
    elif opcion == 3:
        analizadorLogs()
    elif opcion == 4:
        print("Hasta luego")
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        main()


main()
