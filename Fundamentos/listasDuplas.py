
# 1 Mayores y Menores
# Funcion para llenar una lista
def crearLista():
    lista = []
    while True:
        dato = input("Ingrese un dato (o 'fin' para salir): ")
        if dato.lower() == 'fin':
            break
        lista.append(dato)
    return lista
# Funcion para retornar el mayor y el menor de una lista
def mayorMenor(lista):
    mayor = max(lista)
    menor = min(lista)
    return mayor, menor

# Funcion main del ejercicio
def mayoresMenores():
    lista = crearLista()
    mayor, menor = mayorMenor(lista)
    print(f"El mayor número de la lista es {mayor} y el menor es {menor}")
    main()

# 2 Concatenación de Listas
# Funcion para concatenar dos listas y ordenarlas
def concatenarListas(lista1, lista2):
    lista = lista1 + lista2
    lista.sort()
    return lista

# Funcion main del ejercicio
def concatenacionListas():
    print("Concatenación de Listas")
    print("Lista 1:")
    lista1 = crearLista()
    print("Lista 2:")
    lista2 = crearLista()
    lista = concatenarListas(lista1, lista2)
    print("La lista concatenada y ordenada es:")
    for dato in lista:
        print(dato)
    main()
    
# 3 Inversión de Tupla
# Fuincion para ivertir una tupla
def invertirTupla(tupla):
    return tupla[::-1]

# Funcion main del ejercicio

def inversionTupla():
    tupla = tuple(input('Ingrese los elementos de la tupla, separados por comas: ').split(','))
    tupla_invertida = invertirTupla(tupla)
    print(f'La tupla invertida es: {tupla_invertida}')
    main()





# Funcion main del programa
def main():
    print("1. Mayores y Menores")
    print("2. Concatenación de Listas")
    print("3. Inversión de Tupla")
    print("4. Salir")

    opcion = int(input("Seleccione una opción (1, 2, 3 o 4): "))
    
    if opcion == 1:
        mayoresMenores()
    elif opcion == 2:
        concatenacionListas()
    elif opcion == 3:
        inversionTupla()
    elif opcion == 4:
        print("Gracias por utilizar el programa.")
    else:
        print("Opción no válida. Por favor seleccione 1, 2, 3 o 4.")
        main()
        
main()