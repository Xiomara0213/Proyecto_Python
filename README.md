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
- Python 3.7
- pandas
- beautifulsoup4
- requests
- matplotlib
- seaborn
- plotly
- nbformat

# Arquitectura de las Carpetas
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
│   └── scraping/
│       ├── __init__.py
│       └── scraper.py
│
├── README.md
└── dependencies.txt

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