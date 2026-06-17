def imprimir_tabla(paises):
    print(f"{'NOMBRE':<35} {'CONTINENTE':<12} {'POBLACION':<12} {'SUPERFICIE (km2)':<18}")
    print("-" * 74)

    for pais in paises:
        nombre = str(pais['nombre'])[:35]
        continente = str(pais['continente'])[:12]
        poblacion = int(float(str(pais['poblacion']).replace(",", ".")))
        superficie = float(str(pais['superficie']).replace(",", "."))
        print(f"{nombre:<35} {continente:<12} {poblacion:<12} {superficie:<18.2f}")
