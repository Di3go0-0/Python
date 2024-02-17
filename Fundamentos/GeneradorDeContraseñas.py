import string
import random

def generarContrasena(longitud, caracteresEspeciales):
    caracteres = string.ascii_letters + string.digits
    # string.ascci_letters son todas las letras del alfabeto, string.digits son todos los dígitos
    if caracteresEspeciales:
        caracteres += string.punctuation
        # si el usuario quiere caracteres especiales, se añaden a la lista de caracteres
    return ''.join(random.choice(caracteres) for _ in range(longitud))
    # se elige un caracter aleatorio de la lista de caracteres, se repite la cantidad de veces de la longitud de la contraseña

# Funcion main del ejercicio

def generadorContrasenas():
    longitud = int(input("Ingrese la longitud de la contraseña: "))
    caracteres_especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'
    contrasena = generarContrasena(longitud, caracteres_especiales)
    print(f"Su contraseña generada es: {contrasena}")

# Llamada a la funcion main
generadorContrasenas()