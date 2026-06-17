# Gestión de Datos de Países

Sistema interactivo para gestionar, consultar y analizar información de países del mundo. Permite agregar, actualizar, buscar, filtrar y ordenar países según diversos criterios.

- **Gestión de Datos**: Agregar nuevos países y actualizar información existente
- **Búsqueda Avanzada**: Buscar países por nombre con búsqueda parcial y tolerancia a acentos
- **Filtrado Flexible**: 
  - Por continente
  - Por población (rango mínimo-máximo)
  - Por superficie (rango mínimo-máximo)
- **Ordenamiento**: Ordenar por nombre, población, superficie o continente
- **Estadísticas**: Visualizar datos agregados (máximos, mínimos, promedios por continente)
- **Persistencia**: Los datos se guardan automáticamente en formato CSV

## 🗂️ Estructura del Proyecto

```
tpi-gestion-de-datos-de-pa-ses/
├── README.md
├── data/
│   └── paises.csv           # Base de datos de países
├── src/
│   ├── main.py              # Menú principal e interfaz
│   └── functions/
│       ├── __init__.py
│       ├── gestion.py       # Agregar y actualizar países
│       ├── buscador.py      # Búsqueda por nombre
│       ├── filtros.py       # Filtrado por continente, población, superficie
│       ├── ordenamiento.py  # Ordenamiento de países
│       ├── estadisticas.py  # Cálculos y análisis
│       └── tabla.py         # Formateo e impresión de tablas
```

## 🚀 Instalación

### Pasos

1. Clonar o descargar el repositorio:
```bash
git clone https://github.com/usuario/tpi-gestion-de-datos-de-pa-ses.git
cd tpi-gestion-de-datos-de-pa-ses
```

2. Ejecutar el programa:
```bash
python src/main.py
```

## 📊 Formato de Datos

El archivo `data/paises.csv` contiene los siguientes campos:
```csv
nombre,poblacion,superficie,continente
Argentina,46233344,2780400,América
España,47351567,505990,Europa
Japón,123294513,377975,Asia
```

## 📖 Uso

Al ejecutar el programa, se mostrará el menú principal con las siguientes opciones:

```
Menú de opciones:
==============================
1. Agregar un país
2. Actualizar datos de un país
3. Buscar un país por nombre
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
7. Salir
```

### Ejemplos de Uso

#### 1. Agregar un País
```
Seleccione una opción: 1
Ingrese el nombre del pais: España
Ingrese el continente del pais: Europa
Ingrese la poblacion del pais: 47351567
Ingrese la superficie del pais (en km2): 505990
```

#### 2. Actualizar Datos
```
Seleccione una opción: 2
Ingrese el nombre del pais a actualizar: España
Ingrese la nueva poblacion del pais: 47500000
Ingrese la nueva superficie del pais (en km2): 505990
```

#### 3. Buscar un País
```
Seleccione una opción: 3
Ingrese el nombre del país a buscar: Arg
```
Muestra todos los países que comienzan con "Arg" (tolerancia a acentos).

#### 4. Filtrar Países

**Por Continente:**
```
Seleccione una opción: 4
Seleccione una opción de filtrado: A
Continentes disponibles:
1. África
2. América
3. Asia
4. Europa
5. Oceanía
Seleccione un continente por número: 4
```

**Por Población o Superficie:**
```
Seleccione una opción: 4
Seleccione una opción de filtrado: B
Ingrese el valor mínimo de poblacion: 1000000
Ingrese el valor máximo de poblacion: 50000000
```

#### 5. Ordenar Países
```
Seleccione una opción: 5
Opciones de ordenamiento:
A. Por nombre
B. Por población
C. Por superficie
D. Por continente
Seleccione una opción de ordenamiento: B
```

#### 6. Mostrar Estadísticas
```
Seleccione una opción: 6
```
Muestra:
- País con mayor población
- País con menor población
- Promedio de población
- Promedio de superficie
- Cantidad de países por continente


## 📝 Notas

- Los valores de población se convierten a enteros (sin decimales)
- Los valores de superficie se convierten a decimales
- Se acepta "," o "." como separador decimal en las entradas
- La búsqueda y filtrado por continente no diferencian mayúsculas/minúsculas
- Todos los cambios se guardan automáticamente en el CSV


## 👨‍💻 Autor

Proyecto de gestión de datos de países.

## 🎞️ Videos Explicativo


---