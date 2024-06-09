import pandas as pd 
import os #Imoportar para interactuar con el SO
from ..decorators.decorators import timeit, logit, retry #Importar decoradores personalizados

@logit #Añade el loggin a la funcion
@timeit #Mide el tiempo de ejecucion de la funcion
@retry(max_attempts=5, delay=2) #Reintento en caso de fallo
def load_data(data_path):
      #Cargar datos de un archivo CSV
    if data_path.endswith('.csv'): 
        df = pd.read_csv(data_path) #Carga los datos CSV
    elif data_path.endswith('.xlsx'): 
        df = pd.read_excel(data_path) #Carga los datos XLSX
    else:
        raise ValueError("Unsupported file format") #Error si el formato no es compatible
    print("Data loaded successfully") #Imprime SMS indicando que se cargo correctamente
    return df #Devuelve el DataFrame con los datos

@logit #Añade el loggin a la funcion
@timeit #Mide el tiempo de ejecucion de la funcion
def clean_data(df):
      #Limpiar los datos
    df["price"] = df["price"].replace(r"[\$,]", "", regex = True).astype(float) #Limpiar y convertir los precios a "tipo float"
    print("Data cleaned successfully")
    return df #Devuelve los datos formateados

@logit #Añade el loggin a la funcion
@timeit #Mide el tiempo de ejecucion de la funcion
def analyze_data(df):
      #Realiza analisis basicode datos
    print("Basic Data Analysis:") #Imprime encabezado para el analisis
    print(df. describe()) #Imprime resumen estadistico
    print("\nProducts with highest prices: ") #Imprime encabezado con los precios de prodcutos mas altos
    highestPrices = df.nlargest(5, "price") 
    print(highestPrices) #Imprime los 5 precios mas altos
    return highestPrices

@logit #Añade el loggin a la funcion
@timeit #Mide el tiempo de ejecucion de la funcion    
def save_clean_data(df, outputh_path):
      #Guarda datos en un archivo CSV
    if outputh_path.endswith('.csv'):
        df.to_csv(outputh_path, index = False) #Guarda datos en un archivo CSV
    elif outputh_path.endswith('.xlsx'):
        df. to_excel(outputh_path, index = False) #Guarda datos en un archivo XLSX
    else:
        raise ValueError("Unsupported file format") #Error de compatibilidad en el formato de archivo
    print(f"Clean data saved to {outputh_path}")
    
def update_csv(df, output_path):
    df.to_csv(output_path, index=False)  # Guarda el DataFrame en el mismo archivo CSV, sobrescribiendo los datos existentes
    print(f"Updated CSV saved to {output_path}")
    
if __name__ == "__main__": #Permite que el script se ejecute solo en este archivo
    data_path = "data/raw/products.csv" #Define la ruta del archivo con datos sin procesar
    outputh_path = "data/processed/cleaned_products.csv" #Define la ruta del archivo con datos procesados
    
    df = load_data(data_path) #Carga los datos en un archivo especifico
    df = clean_data(df) #Limpia datos cargados
    analyze_data(df) #Realiza analisis basico de datos
    os.makedirs("data/processed", exist_ok = True) #Crea el directorio del archivo con datos procesados
    save_clean_data(df, outputh_path) #Guarda los datos limpios
    update_csv(df, data_path) #Actualiza el archivo CSV 