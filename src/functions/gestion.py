import csv


# --------------------------------------------------------------------
def guardar_paises(paises):
    with open('data/paises.csv', mode='w', encoding='utf-8', newline='') as file:
        fieldnames = ['nombre', 'continente', 'poblacion', 'superficie']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for pais in paises:
            writer.writerow(pais)


def agregar_pais(paises):
    nombre = input("Ingrese el nombre del pais: ").strip()
    continente = input("Ingrese el continente del pais: ").strip()
    poblacion = input("Ingrese la poblacion del pais: ").strip()
    superficie = input("Ingrese la superficie del pais (en km2): ").strip()

    if not nombre or not continente or not poblacion or not superficie: # Vertifica que no haya ninguna variable vacia
        print("Error: Todos los campos son obligatorios.")
        return

    try:
        poblacion = int(poblacion)
        superficie = float(superficie)
    except ValueError:
        print("Error: Poblacion y superficie deben ser numeros.") # verifica que poblacion sea un numero entero y superficie un numero decimal
        return

    nuevo_pais = {
        'nombre': nombre,
        'continente': continente,
        'poblacion': poblacion,          #  Guardamos la informacion de los nuevos paises
        'superficie': superficie
    }
    paises.append(nuevo_pais)            # Los agregamos a paises
    guardar_paises(paises)
    print("Pais '" + nombre + "' agregado exitosamente.")


def actualizar_pais(paises):
    nombre = input("Ingrese el nombre del pais a actualizar: ").strip()

    pais = None
    for p in paises:
        if p['nombre'].lower() == nombre.lower():
            pais = p
            break

    if not pais:
        print("Error: Pais '" + nombre + "' no encontrado.")
        return

    poblacion = input("Ingrese la nueva poblacion del pais: ").strip()
    superficie = input("Ingrese la nueva superficie del pais (en km2): ").strip()

    try:
        poblacion = int(poblacion)
        superficie = float(superficie)
    except ValueError:
        print("Error: Poblacion y superficie deben ser numeros.")
        return

    pais['poblacion'] = poblacion
    pais['superficie'] = superficie
    guardar_paises(paises)
    print("Pais '" + nombre + "' actualizado exitosamente.")