#Autor: Joseph DATE-MASSE
#src/funnel_analysis_functions.py

"""
Wrapper simplifié autour de funnel_metrics.py
Conservé pour compatibilité avec le code existant
"""

import pandas as pd
from funnel_metrics import calculate_funnel_metrics as _calculate_funnel_metrics

def get_funnel_stages(df: pd.DataFrame) -> dict:
    """Retourne un dictionnaire avec les étapes du funnel."""
    return {
        'Impressions': len(df),
        'Contacted': len(df[df['duration'] > 0]),
        'Engaged': len(df[df['duration'] > 60]),
        'Converted': int(df['converted'].sum())
    }


def get_funnel_metrics(stages: dict) -> dict:
    """
    Wrapper autour de calculate_funnel_metrics().
    
    Note: Cette fonction existe pour rétrocompatibilité.
    Pour de nouvelles analyses, nous pouvons utiliser directement:
        from src.funnel_metrics import calculate_funnel_metrics
    """
    # Pour une vraie analyse, il faut le DataFrame complet
    # Ici on fait au mieux avec seulement les stages
    metrics = {
        'contact_rate': (stages.get('Contacted', 0) / stages.get('Impressions', 1)) * 100,
        'engagement_rate': (stages.get('Engaged', 0) / stages.get('Contacted', 1)) * 100 if stages.get('Contacted', 0) > 0 else 0,
        'conversion_rate': (stages.get('Converted', 0) / stages.get('Engaged', 1)) * 100 if stages.get('Engaged', 0) > 0 else 0,
        'global_conversion_rate': (stages.get('Converted', 0) / stages.get('Impressions', 1)) * 100
    }
    return {k: round(v, 2) for k, v in metrics.items()}