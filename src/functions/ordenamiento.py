def imprimir_tabla(paises):
    print(f"{'NOMBRE':<35} {'CONTINENTE':<12} {'POBLACION':<12} {'SUPERFICIE (km2)':<18}")
    print("-" * 74)

    for pais in paises:
        nombre = str(pais['nombre'])[:35]
        continente = str(pais['continente'])[:12]
        poblacion = int(float(str(pais['poblacion']).replace(",", ".")))
        superficie = float(str(pais['superficie']).replace(",", "."))
        print(f"{nombre:<35} {continente:<12} {poblacion:<12} {superficie:<18.2f}")



def ordenar_paises(paises):
    print("Opciones de ordenamiento:")
    print("1. Por nombre")
    print("2. Por población")
    print("3. Por superficie")
    print("4. Por continente")
    
    opcion = input("Seleccione una opción de ordenamiento: ").strip()

    
    if opcion == '1':
        paises.sort(key=lambda p: p['nombre'])
        print("Países ordenados por nombre:")
        imprimir_tabla(paises)
    
    elif opcion == '2':
        paises.sort(key=lambda p: int(p['poblacion']))
        print("Países ordenados por población (ascendente):")
        imprimir_tabla(paises)
    
    elif opcion == '3':
        paises.sort(key=lambda p: float(p['superficie']))
        print("Países ordenados por superficie (ascendente):")
        imprimir_tabla(paises)
    
    elif opcion == '4':
        paises.sort(key=lambda p: p['continente'])
        print("Países ordenados por continente:")
        imprimir_tabla(paises)
    
    else:
        print("Opción de ordenamiento inválida.")

