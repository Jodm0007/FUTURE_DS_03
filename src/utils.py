#Autor: Joseph DATE-MASSE

from pathlib import Path
import logging

def setup_logger(log_file: str = None):
    """ logger Configuration """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_file) if log_file else None
        ]
    )
    return logging.getLogger(__name__)

def ensure_directory_exists(path: str):
    """ Crée un dossier s'il n'existe pas """
    Path(path).mkdir(parents=True, exist_ok=True)