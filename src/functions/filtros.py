
# importat la funcion de impresion de tabla desde el modulo correspondiente
try:
    from .tabla import imprimir_tabla
except ImportError:
    from tabla import imprimir_tabla

# ====================================================================================================
# Funciones auxiliares para el filtrado de países por población y superficie.

def _valor_campo_numerico(pais, campo):
    return float(str(pais[campo]).replace(',', '.'))


def _normalizar_numero(valor):
    return float(str(valor).replace(',', '.'))


def _obtener_valores_rango(paises, campo):
    minimo = input(f"Ingrese el valor mínimo de {campo}: ").strip()
    maximo = input(f"Ingrese el valor máximo de {campo}: ").strip()

    try:
        minimo = _normalizar_numero(minimo)
        maximo = _normalizar_numero(maximo)
    except ValueError:
        print(f"Error: El rango de {campo} debe ser numérico.")
        return False

    if minimo > maximo:
        print(f"Error: El valor mínimo de {campo} no puede ser mayor que el valor máximo.")
        return False
    
    resultados = [p for p in paises if minimo <= _valor_campo_numerico(p, campo) <= maximo]

    if not resultados:
        print(f"No se encontraron países en ese rango de {campo}.")
        return
    
    return resultados


#=====================================================================================================

def _filtrar_por_columna_numerica(paises, campo):
    resultados = _obtener_valores_rango(paises, campo)

    if resultados is False:
        return
    
    resultados.sort(key=lambda p: _valor_campo_numerico(p, campo))
    imprimir_tabla(resultados)


# ====================================================================================================

def filtrar_por_continente(paises):
    
    # Mostrar los continentes disponibles y permitir al usuario seleccionar uno
    print("Continentes disponibles:")
    continentes = list(set(p['continente'] for p in paises))
    for i, continente in enumerate(continentes, start=1):
        print(f"{i}. {continente}")
    
    # Validar que la opción ingresada sea un número válido correspondiente a un continente
    opcion = input("Seleccione un continente por número: ").strip()
    if not opcion.isdigit() or int(opcion) not in range(1, len(continentes) + 1):
        print("Opción no válida.")
        return
    
    # Obtener el continente seleccionado por el usuario y filtrar los países que pertenecen a ese continente
    continente = continentes[int(opcion) - 1]
    resultados = [p for p in paises if p['continente'].lower() == continente.lower()]
    
    # Si no se encuentran resultados, mostrar un mensaje indicando que no se encontraron países en ese continente
    if not resultados:
        print(f"No se encontraron países en el continente '{continente}'.")
        return
    
    # Si se encuentran resultados, imprimir la tabla con los resultados
    imprimir_tabla(resultados)

def filtrar_por_poblacion(paises):
    _filtrar_por_columna_numerica(paises, 'poblacion')

def filtrar_por_superficie(paises):
    _filtrar_por_columna_numerica(paises, 'superficie')

# ====================================================================================================

# Función principal para filtrar países según la opción seleccionada por el usuario
def filtrar_paises(paises):
    print("Opciones de filtrado:")
    print("A. Por Continente")
    print("B. Por Población")
    print("C. Por Superficie")

    opcion = input("Seleccione una opción de filtrado: ").strip().upper()

    if opcion == 'A':
        filtrar_por_continente(paises)
    elif opcion == 'B':
        filtrar_por_poblacion(paises)
    elif opcion == 'C':
        filtrar_por_superficie(paises)
    else:
        print("Opción no válida.")
