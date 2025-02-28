import logging
import os

def configure_logger():
    logger = logging.getLogger('login_attempts')
    logger.setLevel(logging.INFO)

    # Define o caminho absoluto para o arquivo de log
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(BASE_DIR, '..', 'login_attempts.log')

    # Cria um handler para escrever logs em um arquivo
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.INFO)

    # Define o formato dos logs
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Adiciona o handler ao logger
    logger.addHandler(file_handler)

    return logger
