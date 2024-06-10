import requests #Importar para hacer las soluciones HTTP
from bs4 import BeautifulSoup #Importar para analizar los documentos HTML
import pandas as pd #Importar para manejar datosen los DataFrames 
import logging
import time

def fetch_page(url):
    """
    Obtiene el contenido de una pagina
    
    Args:
        url (str): La URL de la página web a obtener

    Returns:
        bytes: El contenido de la página web en formato binario
    """
    max_retries = 5
    retry_delay = 2
    for attempt in range(max_retries):
        try:
            response = requests.get(url) #Solicitud GET a la url proporcionada
            if response.status_code == 200:
                return response.content #Devuelve el contenido de la pagina
            else:
                logging.error(f"Failed to fetch page: {url} with status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
        logging.info(f"Retrying... (attempt {attempt + 1}/{max_retries})")
        time.sleep(retry_delay)
    raise Exception(f"Failed to fetch page after {max_retries} attempts: {url}")

def parse_product(product):
    """
    Analiza detalles de un producto de una pagina web

    Args:
        product (BeautifulSoup.element.Tag): El elemento HTML que representa un producto

    Returns:
        dict: Un diccionario con el título, descripción y precio del producto
    """      
    title = product.find("a", class_="title").text.strip() #Encuentra y obtiene el titulo del producto
    description = product.find("p", class_="description").text.strip() #Encuentra y obtiene la descripcion del producto
    price = product.find("h4", class_="price").text.strip() #Encuentra y obtiene el precio del producto
    return { #Obtenemos un diccionario con el titulo, descripcion y precio del prodcuto
        "title": title,
        "description": description,
        "price": price,
    }
    
def scrape(url):
    """
    Realiza el scraping de una página web para obtener los datos de productos

    Args:
        url (str): La URL de la página web a escrapear

    Returns:
        pandas.DataFrame: Un DataFrame de pandas con los datos de los productos
    """
    page_content = fetch_page(url) #Otiene el codigo de la pagina
    if page_content is not None:
        soup = BeautifulSoup(page_content, 'html.parser') #Analiza el contenido de la pagina
        products = soup.find_all("div", class_="thumbnail") #Encuentra los elementos div que representan productos
        products_data = []
        
        for product in products:
            product_info = parse_product(product) #Analiza cada producto encontrado
            products_data.append(product_info) #Agrega datos del producto a la lista
            
        return pd.DataFrame(products_data)
    else:
        logging.error("Failed to scrape data, page content is None.")
        return pd.DataFrame() 
    
def scrape_all_pages(base_url, num_pages):
    """
    Realiza el scraping de múltiples páginas web para obtener los datos de productos

    Args:
        base_url (str): La URL base de la tienda en línea
        num_pages (int): El número total de páginas a escrapear

    Returns:
        pandas.DataFrame: Un DataFrame de pandas con los datos de los productos de todas las páginas
    """
    all_products = pd.DataFrame() #Crea un DataFrame para almacenar los datos
    for page_number in range(1, num_pages + 1):
          #Construccion de la URL de la pagina
        page_url = f"{base_url}?page={page_number}"
        logging.info(f"Scraping page {page_number}...")
        df = scrape(page_url)
        all_products = pd.concat([all_products, df], ignore_index=True) #Concatenar datos en el DataFrame
        time.sleep(2)  # Espera de cortesía para evitar bloqueos
    return all_products

if __name__ == "__main__":
    # URL de la tienda en línea
    base_url = "https://webscraper.io/test-sites/e-commerce/allinone"

    #Numero de paginas
    num_pages = 3

    #Llamamos a SCRAPE para obtener los datos
    df = scrape_all_pages(base_url, num_pages)

    #Imprime el resultado
    print(df.head())

    #Guardar los datos en CSV sin el indice
    df.to_csv('data/raw/products.csv', index = False)
    df.to_csv('data/raw/scraped_all_pages.csv', index = False)