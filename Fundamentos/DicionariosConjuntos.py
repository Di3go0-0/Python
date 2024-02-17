
# 1. Contador de Palabras
# Funcion para contar las palabras de un texto
def contarPalabras(texto):
    palabras = texto.split()
    return {palabra: palabras.count(palabra) for palabra in set(palabras)}
    # se crea un conjunto con las palabras únicas del texto, y se cuenta cuántas veces aparece cada una
    

# Funcion main del ejercicio
def contadorPalabras():
    texto = input("Ingrese un texto: ")
    conteo_palabras = contarPalabras(texto)
    print(f"El conteo de palabras es: {conteo_palabras}")

    main()

# 2. Unión e Intersección de Conjuntos
# Funcion para unir dos conjuntos y obtener la intersección
def unionInterseccion(conjunto1, conjunto2):
    union = conjunto1.union(conjunto2)
    interseccion = conjunto1.intersection(conjunto2)
    return union, interseccion
# Funcion main del punto
def conjuntosUnionInterseccion():
    conjunto1 = set(input('Ingrese los elementos del primer conjunto, separados por comas: ').split(','))
    conjunto2 = set(input('Ingrese los elementos del segundo conjunto, separados por comas: ').split(','))
    # set convierte la lista de elementos en un conjunto y split separa los elementos por comas
    union, interseccion = unionInterseccion(conjunto1, conjunto2)
    print(f'La unión de los conjuntos es: {union}')
    print(f'La intersección de los conjuntos es: {interseccion}')
    
# 3. Agenda Telefónica

# Funcion para agregar un contacto a la agenda
def agregarContacto(agenda):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono del contacto: ")
    agenda[nombre] = telefono
    
# Funcion para eliminar un contacto de la agenda
def eliminarContacto(agenda):
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
    else:
        print("El contacto no existe en la agenda.")
        
# Funcion para buscar un contacto en la agenda
def buscarContacto(agenda):
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in agenda:
        print(f"El número de {nombre} es {agenda[nombre]}")
    else:
        print("El contacto no existe en la agenda.")
# Funcion main del punto
def agendaTelefonica():
    agenda = {}
    while True:
        print("\n1. Agregar contacto")
        print("2. Eliminar contacto")
        print("3. Buscar contacto")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregarContacto(agenda)
        elif opcion == '2':
            eliminarContacto(agenda)
        elif opcion == '3':
            buscarContacto(agenda)
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
    print(f"\nLa agenda telefónica es: {agenda}")







# Funcion main del programa
def main():
    print("1. Contador de Palabras")
    print("2. Unión e Intersección de Conjuntos")
    print("3. Agenda Telefónica")
    print("4. Salir")

    opcion = int(input("Seleccione una opción (1, 2, 3 o 4): "))
    
    if opcion == 1:
        contadorPalabras()
    elif opcion == 2:
        conjuntosUnionInterseccion()
    elif opcion == 3:
        agendaTelefonica()
    elif opcion == 4:
        print("Gracias por utilizar el programa.")
    else:
        print("Opción no válida. Por favor seleccione 1, 2, 3 o 4.")
        main()
        
main()