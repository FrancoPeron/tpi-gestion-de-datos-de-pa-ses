import unicodedata

# Importar la función de filtrado y la función de impresión de tabla desde el módulo correspondiente
try:
    from .filtros import filtrar_paises
    from .tabla import imprimir_tabla
except ImportError:
    from filtros import filtrar_paises
    from tabla import imprimir_tabla

# Función para normalizar texto (eliminar acentos y convertir a minúsculas)
def normalizar_texto(texto):
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII').lower()

# Función para buscar un país por nombre (con búsqueda parcial y sin acentos)
def buscar_pais(paises):
    nombre = normalizar_texto(input("Ingrese el nombre del país a buscar: ").strip())
    resultados = [p for p in paises if normalizar_texto(p['nombre']).startswith(nombre)]

    # Si no se encuentran resultados, mostrar un mensaje indicando que no se encontraron países coincidentes
    if not resultados:
        print(f"No se encontraron países que coincidan con '{nombre}'")
        return

    # Si se encuentran resultados, imprimir la tabla con los resultados
    print(f"Resultados de búsqueda para '{nombre}':")
    imprimir_tabla(resultados)
    
    #=======================================================

    # Preguntar si desea filtrar los resultados
    filtrar = input("\n¿Desea filtrar estos resultados? (s/n): ").strip().lower()
    if filtrar == 's':
        filtrar_paises(resultados)

