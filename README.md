# DATOS
Alexandra Xiomara Montaño Apolo

alexandra130255@gmail.com

# Proyecto de Análisis de Datos
Este proyecto consiste en un conjunto de herramientas para el análisis de datos utilizando Python.

# Características
- Carga de Datos: La herramienta "load_data" permite cargar datos desde archivos CSV o Excel de datos de productos individuales y de todas las páginas de un sitio web de comercio electrónico.

- Limpieza de Datos: La herramienta "clean_data" limpia los datos eliminando caracteres no deseados y convirtiendo el precio a tipo float.

- Análisis de Datos: La herramienta "analyze_data" realiza un análisis básico de los datos, incluyendo un resumen estadístico y la identificación de los productos con los precios más altos.

- Guardado de Datos: La herramienta "save_clean_data" guarda los datos limpios en archivos CSV o Excel.

# Requisitos
- Python 3.7+
- pandas
- beautifulsoup4
- requests
- matplotlib
- seaborn
- plotly
- nbformat

# Arquitectura de las Carpetas
````bash
Proyecto_Python/
│
├── data/
│   ├── processed/
│   │   ├── cleaned_products.csv
│   │   └── cleaned_all_pages.csv
│   │
│   └── raw/
│       ├── products.csv
│       └── scraped_all_pages.csv
├── notebooks/
│   ├── exploration.ipynb
│   └── scatter_plot.html
├── src/
│   ├── analysis/
│   │   ├── __init__.py
│   │   └── analysis.py
│   │
│   ├── decorators/
│   │   ├── __init__.py
│   │   └── decorators.py
│   │
│   ├── main/
│   │   ├── __init__.py
│   │   └── main.py
│   │
│   └── scraping/
│       ├── __init__.py
│       └── scraper.py
│
├── README.md
└── dependencies.txt
````

# Instalación
Para instalar las dependencias creamos un archivo TXT en el cual guardamos todas las dependencias para una instalacion mas rapida. Su metodo de instalacion es utilizando "PIP":
````bash
pip install -r dependencies.txt
````

# Uso
## Ejecucion del Scraper
Para la ejecucion del scraper lo que se realiza es
````bash
python .\src\scraping\scraper.py
````
Esto genera los archivos CSV/XLSX en la carpeta RAW ubicada dentro de la carpeta DATA

## Ejecucion del Analisis de Datos
Para la ejecucion del Analisis de Datos lo que se realiza es
````bash
python .\src\analysis\analysis.py
````
Esto genera los archivos CSV/XLSX en la carpeta PROCESSED ubicada dentro de la carpeta DATA

## Decoradores Personalizados
El archivo "decorators.py" contiene una serie de decoradores que se utilizan en este proyecto para realizar algunas tareas.

- "timeit": Decorador que mide el tiempo de ejecución de una función.
- "logit": Decorador que registra eventos antes y después de la ejecución de una función.
- "retry": Decorador que reintenta automáticamente una función un número configurable de veces si falla.

Estos decoradores se importan y aplican a las funciones relevantes en otros archivos del proyecto como "main.py" y "analysis.py", para agregar funcionalidades adicionales.

## Interfaz de Usuario
Contiene la lógica principal para ejecutar el proyecto, ya sea a través de la línea de comandos (CLI) o mediante una interfaz gráfica de usuario (GUI).

La función que maneja la ejecución de la herramienta a través de la línea de comandos es: "run_cli"

La función que maneja la ejecución de la herramienta a través de la interfaz gráfica de usuario es: "run_gui"

Para ejecutar la herramienta desde la línea de comandos, se puede utilizar el siguiente comando:

````bash
python src/main/main.py data/raw/products.csv --output_path data/processed/cleaned_products.csv
````
Para ejecutar la herramienta utilizando la interfaz gráfica de usuario, se puede utilizar el siguiente comando:
````bash
python main.py --gui
````
## Analisis Exploratorio de Datos
El archivo "exploration.ipynb" es un cuaderno de "Jupyter" que contiene la exploración de datos. En este cuaderno, se realizan diversas operaciones de análisis exploratorio de datos para comprender mejor la naturaleza y la distribución de los datos.

Para ejecutar el cuaderno y revisar la exploración de datos, simplemente abre el archivo en un entorno de "Jupyter" Notebook.

```bash
jupyter notebook exploration.ipynb
````