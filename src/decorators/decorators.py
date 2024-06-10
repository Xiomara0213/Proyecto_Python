import time #Importar para medir el tiempo de ejeciucion
import logging #Importar para registrar mensajes

#Configura el Logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def timeit(func):
    """
    Decorador para medir el tiempo de ejecución de una función

    Args:
        func (function): La función a decorar

    Returns:
        function: La función decorada
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f"{func.__name__} ejecutada en {elapsed_time:.4f} seconds")
        return result
    return wrapper

def logit(func):
    """
    Decorador para registrar el inicio y el fin de la ejecución de una función

    Args:
        func (function): La función a decorar

    Returns:
        function: La función decorada
    """
    def wrapper(*args, **kwargs):
        logging.info(f"Corriendo {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Completado {func.__name__}")
        return result
    return wrapper

def retry(max_attempts=3, delay=1):
    """
    Decorador para reintentar ejecutar una función en caso de fallo

    Args:
        max_attempts (int): El número máximo de intentos
        delay (int): El tiempo de espera entre intentos, en segundos

    Returns:
        function: La función decorada
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    logging.warning(f"Error en {func.__name__}: {e}. Reintentando {attempts}/{max_attempts}...")
                    time.sleep(delay)
            logging.error(f"{func.__name__} falló después de {max_attempts} intentos.")
            raise
        return wrapper
    return decorator