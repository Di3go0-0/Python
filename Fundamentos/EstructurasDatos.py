# 1 Lista de Compra

# Funcion para crear una lista de compra
def crearLista():
    lista = []
    while True:
        producto = input('Ingrese los datos  (o "fin" para terminar): ')
        if producto == 'fin':
            break
        lista.append(producto)
    return lista
# Funcion main para el ejercicio
def listaCompra():
    listaCompra = crearLista()
    print('La lista de compra es:')
    for producto in listaCompra:
        print(producto)
        
        
# 2 Eliminación de Duplicados
# Funcion para eliminar duplicados
def eliminarDuplicado(lista):
    listaSinDuplicados = list(set(lista))
    # Set convierte la lista en un conjunto, eliminando los duplicados, ya que en un conjunto no hay elementos duplicados
    # list convierte el conjunto de vuelta a lista
    return listaSinDuplicados
# Funcion main del punto
def eliminacionDucplicados():
    print('Eliminación de Duplicados')
    lista = crearLista()
    lista = eliminarDuplicado(lista)
    print('La lista sin duplicados es:')
    for producto in lista:
        print(producto)
    main()
    
# 3 Diccionario de Sinónimos
sinonimos = {
        'feliz': ['contento', 'alegre', 'satisfecho'],
        'triste': ['desdichado', 'desgraciado', 'infeliz'],
        'rápido': ['veloz', 'ligero', 'ágil'],
        # Agrega más palabras y sus sinónimos aquí
    }
    
def diccionarioSinonimos():
    palabra = input('Ingrese una palabra: ').lower()
    # lower convierte la palabra a minúsculas
    if palabra in sinonimos:
        print(f'Los sinónimos de {palabra} son: {", ".join(sinonimos[palabra])}')
    else:
        print(f'Lo siento, no tengo sinónimos para {palabra}.')



# Funcion main del program 
def main():
    print('1. Lista de Compra')
    print('2. Eliminación de Duplicados')
    print('3. Diccionario de Sinónimos')
    print('4. Salir')
    
    opcion = int(input('Seleccione una opción: '))
    
    if opcion == 1:
        listaCompra()
    if opcion == 2:
        eliminacionDucplicados()
    if opcion == 3:
        diccionarioSinonimos()
    elif opcion == 4:
        print('Gracias vuelva pronto!')
    else:
        print("Opción no válida. Por favor seleccione 1 o 2.")
        main()
        
        
# Punto de inicio del programa
main()
