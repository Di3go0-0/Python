# 1 Convertir grados Celsius a Fahrenheit y viceversa

# Funcion que convierte de celsius a fahrenheit
def celsius_a_fahrenheit(celsius): 
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
# Funcion que convierte de fahrenheit a celsius
def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
# Funcion main del ejercicio
def conversorDeTemperatura():
    print("Conversor de Temperatura")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    opcion = int(input("Seleccione una opción (1 o 2): "))

    if opcion == 1:
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.")
        main()
    elif opcion == 2:
        fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
        celsius = fahrenheit_a_celsius(fahrenheit)
        print(f"{fahrenheit} grados Fahrenheit equivalen a {celsius} grados Celsius.")
        main()
    else:
        print("Opción no válida. Por favor seleccione 1 o 2.")
        conversorDeTemperatura()

# 2 Calculadora de IMC

# Funcion para calcular el IMC
def indiceMasaCorporal(peso, altura):
    IMC = peso / (altura ** 2)
    return IMC
# Funcion main del ejercicio
def calculadoraDeIMC():
    print('Calculadora de IMC')
    peso = float(input('Ingrese su peso en Kilogramos: '))
    altura = float(input('Ingrese su altura en metros: '))
    IMC = indiceMasaCorporal(peso, altura)
    print(f'Su IMC es {IMC:.2f}')
    main()

# 3 Generador de Nombre de Usuario

# Funcion para generar el nombre de usuario
def nombreDeUsuario(nombre, apellido, anoNacimiento):
    partesNombre = nombre.split() #Divide el nombre en partes
    primerNombre = partesNombre[0] #Obtiene el primer nombre
    partesApellido = apellido.split() #Convierte el apellido a partes
    primerApellido = partesApellido[0] #Obtiene el primer apellido
    nombreUsuario = primerNombre.capitalize() + primerApellido.capitalize() + str(anoNacimiento)

    return nombreUsuario
# Funcion main para el ejercicio
def generadorDeNombreDeUsuario():
    print('Generador de Nombre de Usuario')
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    anoNacimiento = input('Ingrese su ano de nacimiento: ')
    if anoNacimiento.isdigit(): #Retorna true si todos los digitos son numeros
        nombreUsuario = nombreDeUsuario(nombre, apellido, int(anoNacimiento))
        print('Su nombre de usuario es: ' + nombreUsuario)
        main()
    else:
        print("El año de nacimiento debe ser un número.")
        generadorDeNombreDeUsuario()

def main():
    print('1. Conversor de Temperatura')
    print('2. Calculadora de IMC')
    print('3. Generador de Nombre de Usuario')
    print('4. Salir')

    opcion = int(input('Seleccione una opcion: '))
    if opcion == 1:
        conversorDeTemperatura()
    elif opcion == 2:
        calculadoraDeIMC()
    elif opcion == 3:
        generadorDeNombreDeUsuario()
    elif opcion == 4:
        print('Gracias vuelva pronto!')
    else :
        print('Opción no válida. Por favor seleccione 1, 2, 3 o 4.')
        main()

if __name__ == "__main__":
    main()