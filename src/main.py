
import csv
import os

from functions.gestion import agregar_pais, actualizar_pais
from functions.buscador import buscar_pais
from functions.filtros import filtrar_paises
from functions.ordenamiento import ordenar_paises
from functions.estadisticas import mostrar_estadisticas

# Función para cargar países desde el archivo CSV
# Usando la clase DictReader para leer el archivo como un diccionario en cada fila
def cargar_paises():
    paises = []
    if os.path.exists('data/paises.csv'):
        with open('data/paises.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                paises.append(row)
    return paises

# --------------------------------------------------------------------


# Menu principal
def menu():
    paises = cargar_paises()
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar un país")
        print("2. Actualizar datos de un país")
        print("3. Buscar un país por nombre")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas")
        print("7. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            agregar_pais(paises)
        elif opcion == '2':
            actualizar_pais(paises)
        elif opcion == '3':
            buscar_pais(paises)
        elif opcion == '4':
            filtrar_paises(paises)
        elif opcion == '5':
            ordenar_paises(paises)
        elif opcion == '6':
            mostrar_estadisticas(paises)
        elif opcion == '7':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción del menú.")

# verifico que el programa se ejecute solo si es el archivo principal
if __name__ == "__main__":
    menu()