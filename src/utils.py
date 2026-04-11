#Autor: Joseph DATE-MASSE

from pathlib import Path
import logging
import sys

def setup_logger(log_file: str = None):
    """ logger Configuration """
    handlers = [logging.StreamHandler(sys.stdout)] # Force l'envoi sur la sortie standard (fond blanc)
    if log_file:
        handlers.append(logging.FileHandler(log_file, encoding='utf-8'))
        
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=handlers,
        force=True # Force la réinitialisation du logger dans Jupyter
    )
    return logging.getLogger(__name__)

def ensure_directory_exists(path: str):
    """ Crée un dossier s'il n'existe pas """
    Path(path).mkdir(parents=True, exist_ok=True)