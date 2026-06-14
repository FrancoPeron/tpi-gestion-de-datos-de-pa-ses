def mostrar_estadisticas(paises):
    if not paises:
        print("No hay países registrados para mostrar estadísticas.")
        return

    pais_mayor_poblacion = pais_mayor_poblacion = paises[0]
    for pais in paises:
            if pais['poblacion'] > pais_mayor_poblacion['poblacion']:
                pais_mayor_poblacion = pais
                
                
    pais_menor_poblacion = pais_mayor_poblacion = paises[0]
    for pais in paises:
        if pais['poblacion'] < pais_menor_poblacion['poblacion']:
                pais_menor_poblacion = pais
                            
    
    promedio_poblacion = total_poblacion = 0
    for pais in paises:
        total_poblacion = total_poblacion + float(pais['poblacion'])
    promedio_poblacion = total_poblacion / len(paises)
    
    
    promedio_superficie = total_superficie = 0 
    for pais in paises:
        total_superficie = total_superficie + float(pais['superficie'])
    promedio_superficie = total_superficie / len(paises)

    print(f"País con mayor población: {pais_mayor_poblacion['nombre']} ({pais_mayor_poblacion['poblacion']} habitantes)")
    print(f"País con menor población: {pais_menor_poblacion['nombre']} ({pais_menor_poblacion['poblacion']} habitantes)")
    print(f"Promedio de población: {promedio_poblacion:.2f} habitantes")
    print(f"Promedio de superficie: {promedio_superficie:.2f} km²")

    continentes = {}
    for pais in paises:
        continente = pais['continente']
        if continente in continentes:
            continentes[continente] = continentes[continente] + 1
        else:
            continentes[continente] = 1

    print("Cantidad de países por continente:")
    for continente, cantidad in continentes.items():
        print(f"- {continente}: {cantidad} países")