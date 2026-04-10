# Autor: Joseph DATE-MASSE

import pandas as pd 
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def load_data(file_path: str) -> pd.DataFrame:
    """ Load data from CSV file """
    try:
        df = pd.read_csv(file_path)
        logger.info(f"|==> Data loaded successfully from {file_path}")
        return df
    except FileNotFoundError:
        logger.error(f"|==> File not found: {file_path}")
        return None

def load_excel_data(file_path: str) -> pd.DataFrame:
    """ Load data from Excel file """
    try:
        df = pd.read_excel(file_path)
        logger.info(f"|==> Data loaded successfully from {file_path}")
        return df
    except FileNotFoundError:
        logger.error(f"|==> File not found: {file_path}")
        return None
 