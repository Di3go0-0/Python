import random

# 1 Adivina el Número funcion para adivinar el numero
def adivinaNumero():
    print('Adivina el número')
    numeroAleatorio = random.randint(1, 10)
    numero = int(input('Ingrese un número entre 1 y 10: '))
    while(numero != numeroAleatorio):
        if numero > numeroAleatorio:
            print('Muy alto')
        else:
            print('Muy bajo')
        numero = int(input('Ingrese un número entre 1 y 10: '))
    print('Felicidades, adivinaste el número!')
    main()
    
# 2 Calculadora de Factorial

# Funcion para calcular el factorial
def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero -1)
    
def factorialParaNiños(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado
    
# Funcion main del ejercicio

def calculadoraDeFactorial():
    print('Calcualdora de Factorial')
    numero = int(input('Ingrese un número: '))
    print(f'El factorial de {numero} es {factorial(numero)}')
    main()
    
# 3 Contador de Vocales

# Funcion para contar vocales

def contarVocales(palabra):
    contador = 0
    for letra in palabra:
        if letra in 'aeiou':
            contador += 1
    return contador

# Funcion main del ejercicio

def contadorVocales():
    print('Contador de Vocales')
    palabra = input('Ingrese una palabra: ')
    print(f'La palabra {palabra} tiene {contarVocales(palabra)} vocales')
    main()


# Funcion main
def main():
    print('1. Adivina el Número')
    print('2. Calculadora de Factorial')
    print('3. Contador de Vocales:')
    print('4. Salir')
    
    opcion = int(input('Seleccione una opción: '))
    
    if opcion == 1:
        adivinaNumero()
    elif opcion == 2:
        calculadoraDeFactorial()
    elif opcion == 3:
        contadorVocales()
    elif opcion == 4:
        print('Gracias por jugar!')
    else: 
        print('Opción no válida. Por favor seleccione 1, 2, 3 o 4.')
        main()
    
#Punto de arranque
main()