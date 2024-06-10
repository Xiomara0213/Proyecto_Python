import sys
import os #Imoportar para interactuar con el Sistema Operativo
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
from decorators.decorators import timeit, logit, retry #Importar decoradores personalizados

@logit #Añade el loggin a la funcion
@timeit #Mide el tiempo de ejecucion de la funcion
@retry(max_attempts=5, delay=2) #Reintento en caso de fallo
def load_data(data_path):
    """
    Cargar datos de un archivo CSV o XLSX
    
    Args:
        data_path (str): Ruta del archivo de datos

    Returns:
        pandas.DataFrame: DataFrame con los datos cargados
    """
    if data_path.endswith('.csv'): 
        df = pd.read_csv(data_path) #Carga los datos CSV
    elif data_path.endswith('.xlsx'): 
        df = pd.read_excel(data_path) #Carga los datos XLSX
    else:
        raise ValueError("Unsupported file format") #Error si el formato no es compatible
    print("Data loaded successfully") #Imprime SMS indicando que se cargo correctamente
    return df #Devuelve el DataFrame con los datos

@logit
@timeit
def clean_data(df):
    """
    Limpia los datos eliminando caracteres no deseados y convirtiendo el precio a tipo float

    Args:
        df (pandas.DataFrame): DataFrame con los datos a limpiar

    Returns:
        pandas.DataFrame: DataFrame con los datos limpios
    """
    df["price"] = df["price"].replace(r"[\$,]", "", regex = True).astype(float) #Limpiar y convertir los precios a "tipo float"
    print("Data cleaned successfully")
    return df #Devuelve los datos formateados

@logit
@timeit
def analyze_data(df):
    """
    Realiza analisis basicode datos
    
    Args:
        df (pandas.DataFrame): DataFrame con los datos a analizar

    Returns:
        pandas.DataFrame: DataFrame con los productos de precios más altos
    """
    print("Basic Data Analysis:") #Imprime encabezado para el analisis
    print(df. describe()) #Imprime resumen estadistico
    print("\nProducts with highest prices: ") #Imprime encabezado con los precios de prodcutos mas altos
    highestPrices = df.nlargest(5, "price") 
    print(highestPrices) #Imprime los 5 precios mas altos
    return highestPrices

@logit
@timeit  
def save_clean_data(df, outputh_path):
    """
    Guarda los datos limpios en un archivo CSV o XLSX

    Args:
        df (pandas.DataFrame): DataFrame con los datos limpios
        output_path (str): Ruta del archivo de salida

    Returns:
        None
    """
    if outputh_path.endswith('.csv'):
        df.to_csv(outputh_path, index = False) #Guarda datos en un archivo CSV
    elif outputh_path.endswith('.xlsx'):
        df. to_excel(outputh_path, index = False) #Guarda datos en un archivo XLSX
    else:
        raise ValueError("Unsupported file format") #Error de compatibilidad en el formato de archivo
    print(f"Clean data saved to {outputh_path}")

@logit
@timeit   
def update_csv(df, output_path):
    """
    Actualiza un archivo CSV existente con el DataFrame dado

    Args:
        df (pandas.DataFrame): DataFrame con los datos a guardar
        output_path (str): Ruta del archivo CSV

    Returns:
        None
    """
    df.to_csv(output_path, index=False)  # Guarda el DataFrame en el mismo archivo CSV, sobrescribiendo los datos existentes
    print(f"Updated CSV saved to {output_path}")

  
if __name__ == "__main__": #Permite que el script se ejecute solo en este archivo
    # Rutas de los archivos de datos
    data_path = "data/raw/products.csv"  # Define la ruta del archivo con datos sin procesar (productos individuales)
    data_path_all_pages = "data/raw/scraped_all_pages.csv"  # Define la ruta del archivo con datos de todas las páginas
    output_path = "data/processed/cleaned_products.csv"  # Define la ruta del archivo con datos procesados (productos individuales)
    output_path_all_pages = "data/processed/cleaned_all_pages.csv"  # Define la ruta del archivo con datos procesados (todas las páginas)

    # Procesamiento de datos de productos individuales
    df_single = load_data(data_path)  # Carga los datos de productos individuales
    df_single = clean_data(df_single)  # Limpia datos cargados
    analyze_data(df_single)  # Realiza análisis básico de datos
    os.makedirs("data/processed", exist_ok=True)  # Crea el directorio del archivo con datos procesados
    save_clean_data(df_single, output_path)  # Guarda los datos limpios de productos individuales
    update_csv(df_single, data_path)  # Actualiza el archivo CSV de productos individuales

    # Procesamiento de datos de todas las páginas
    df_all_pages = load_data(data_path_all_pages)  # Carga los datos de todas las páginas
    df_all_pages = clean_data(df_all_pages)  # Limpia datos cargados
    analyze_data(df_all_pages)  # Realiza análisis básico de datos
    save_clean_data(df_all_pages, output_path_all_pages)  # Guarda los datos limpios de todas las páginas
    update_csv(df_all_pages, data_path_all_pages)  # Actualiza el archivo CSV de todas las páginas
