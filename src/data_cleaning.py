#Autor: JosephDATE-MASSE

import logging
from numpy import nan
import pandas as pd 
import numpy as np 
from pathlib import Path 
import logging

logger = logging.getLogger(__name__)

def clean_unknown_values(df: pd.DataFrame) -> pd.DataFrame:
    """Remplacer les valueurs 'unknown' par NaN dans les colonnes categorielles"""
    logger.info("|==> Nettoyage des valeurs 'unknown'...")
    cols_cat = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'poutcome']
    for col in cols_cat:
        if col in df.columns:
            df[col] = df[col].replace('unknown', nan)
    return df


def clean_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Supprimer les lignes contenant des valeurs manquantes...."""
    logger.info("|==> Suppression des valeurs manquantes...")
    before = df.isnull().sum().sum()
    df = df.dropna()
    after = df.isnull().sum().sum()
    logger.info(f" {before - after} miss-values drop")
    return df


def clean_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Supprimer les lignes dupliquees...."""
    logger.info("|==> Suppression des lignes dupliquees...")
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    logger.info(f" {before - after} duplicates drop")
    return df


def clean_numeric_types(df: pd.DataFrame) -> pd.DataFrame:
    """Convertion de 'age' en numérique tout en supprimant les valeurs invalides."""
    logger.info("|==> Nettoyage des types numeriques...")
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df = df.dropna(subset=['age'])
    return df


def convert_target_to_binary(df: pd.DataFrame) -> pd.DataFrame:
    """Conversion de la colone 'y'(yes/no) en binaire (1/0)"""
    logger.info("|==> Conversion of target in binary...")
    df['converted'] = df['y'].map({'yes':1, 'no':0})
    return df


def add_funnel_stage(df: pd.DataFrame) -> pd.DataFrame:
    """Ajout de la colonne 'funnel_stage' pour le suivi du parcours client"""
    logger.info("|==> Ajout de la colonne 'funnel_stage'...")
    df['funnel_stage'] = pd.cut(
        df['duration'],
        bins=[-1, 0, 60, 180, np.inf],
        labels=['No_Contact', 'Brief_Contaact', 'Engaged', 'Highly_Engaged']
    )
    return df


def add_showed_interest(df: pd.DataFrame) -> pd.DataFrame:
    """Ajout de la colone binaire indiquant si l'appel a ete repondu (duration > 0)"""
    logger.info("|==> Ajout de l'indicateur d'interet...")
    df['showed_interest'] = (df['duration'] > 0).astype(int)
    return df


