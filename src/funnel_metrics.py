#Autor: Joseph DATE-MASSE

import pandas as pd
import numpy as np
from typing import Dict, List, Optional 


def calculate_funnel_metrics(df: pd.DataFrame, stages: Dict[str, int]) -> Dict[str, float]:
    total = stages.get('Impressions', 0)
    contacted = stages.get('Contacted', 0)
    engaged = stages.get('Engaged', 0)
    converted = stages.get('Converted', 0)
    
    metrics = {
        'contact_rate': (contacted / total) * 100 if total > 0 else 0,
        'engagement_rate': (engaged / total) * 100 if total > 0 else 0,
        'conversion_rate': (converted / total) * 100 if total > 0 else 0,
        'contact_to_engaged_dropoff': ((contacted - engaged) / contacted) * 100 if contacted > 0 else 0,
        'engaged_to_converted_dropoff': ((engaged - converted) / engaged) * 100 if engaged > 0 else 0,
        'avg_duration_sec': round(df['duration'].mean(), 2),
        'conversion_by_interest_pct': round(df[df['showed_interest'] == 1]['converted'].mean() * 100, 2)
    }
    return metrics


def calculate_conversion_by_dimension(
    df: pd.DataFrame, 
    dimension: str, 
    top_n: Optional[int] = None
) -> pd.DataFrame:
    """
    Calcule le taux de conversion agrégé par dimension catégorielle.

    Args:
        df: DataFrame avec colonne 'converted' (0/1)
        dimension: Nom de la colonne à agréger (ex: 'month', 'job', 'contact')
        top_n: Si spécifié, ne garde que les N meilleures catégories

    Returns:
        DataFrame avec taux de conversion par catégorie

    Raises:
        ValueError: Si la colonne 'converted' ou la dimension n'existe pas
    """
    if 'converted' not in df.columns:
        raise ValueError("Colonne 'converted' non trouvée. Exécutez d'abord convert_target_to_binary()")

    if dimension not in df.columns:
        raise ValueError(f"Colonne '{dimension}' non trouvée dans le dataset")

    agg_df = df.groupby(dimension, dropna=False).agg(
        total_contacts=('converted', 'count'),
        converted=('converted', 'sum'),
        conversion_rate=('converted', lambda x: round(x.mean() * 100, 2))
    ).sort_values('conversion_rate', ascending=False)

    if top_n:
        agg_df = agg_df.head(top_n)

    return agg_df.reset_index()


def calculate_conversion_by_segment(
    df: pd.DataFrame, 
    segment_col: str, 
    metric_col: str = 'duration'
) -> pd.DataFrame:
    """
    Compare les métriques entre convertis et non-convertis.

    Args:
        df: DataFrame avec colonne 'converted'
        segment_col: Colonne à analyser (ex: 'job', 'education')
        metric_col: Colonne métrique à comparer (ex: 'duration', 'age')

    Returns:
        DataFrame avec statistiques comparatives
    """
    if segment_col not in df.columns:
        raise ValueError(f"Colonne '{segment_col}' non trouvée")

    comparison = df.groupby(['converted', segment_col])[metric_col].agg(
        ['mean', 'median', 'count']
    ).round(2)

    return comparison
