try:
    from .tabla import imprimir_tabla
except ImportError:
    from tabla import imprimir_tabla


# Funcion para ordenar los paises por diferentes criterios (columnas)
def ordenar_paises(paises):
    print("Opciones de ordenamiento:")
    print("A. Por nombre")
    print("B. Por población")
    print("C. Por superficie")
    print("D. Por continente")
    
    opcion = input("Seleccione una opción de ordenamiento: ").strip().upper()

    
    if opcion == 'A':
        paises.sort(key=lambda p: p['nombre'])
        print("Países ordenados por nombre:")
        imprimir_tabla(paises)
    
    elif opcion == 'B':
        paises.sort(key=lambda p: int(p['poblacion']))
        print("Países ordenados por población (ascendente):")
        imprimir_tabla(paises)
    
    elif opcion == 'C':
        paises.sort(key=lambda p: float(p['superficie']))
        print("Países ordenados por superficie (ascendente):")
        imprimir_tabla(paises)
    
    elif opcion == 'D':
        paises.sort(key=lambda p: p['continente'])
        print("Países ordenados por continente:")
        imprimir_tabla(paises)
    
    else:
        print("Opción de ordenamiento inválida.")


# Se uso la funcion "sort" ya que por detras usa el algoritmo Timsort, a diferencia de otros algoritmos de ordenamiento su complejidad es O(n log n) en el peor caso.
# Se le paso una función anónima "Lambda" para especificar el criterio de ordenamiento según la opción seleccionada por el usuario.
# Se creó una función adicional para imprimir los paises en formato de tabla.