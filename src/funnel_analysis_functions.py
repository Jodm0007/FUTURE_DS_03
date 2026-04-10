#Autor: Joseph DATE-MASSE
#src\funnel_analysis_functions.py

import pandas as pd



def get_funnel_stages(df: pd.DataFrame) -> dict:
    """Retourne un dictionnaire avec les étapes du funnel."""
    stages = {
        'Impressions': len(df),
        'Contacted': len(df[df['duration'] > 0]),
        'Engaged': len(df[(df['duration'] > 60) & (df['poutcome'] != 'failure')]),
        'Converted': df['converted'].sum()
    }
    return stages

def get_funnel_metrics(stages: dict) -> dict:
    """Retourne un dictionnaire avec les métriques du funnel."""
    impressions = stages.get('Impressions', 0)
    contacted = stages.get('Contacted', 0)
    engaged = stages.get('Engaged', 0)
    converted = stages.get('Converted', 0)
    
    metrics = {
        'contact_rate': (contacted / impressions) * 100 if impressions > 0 else 0,
        'engagement_rate': (engaged / contacted) * 100 if contacted > 0 else 0,
        'conversion_rate': (converted / engaged) * 100 if engaged > 0 else 0,
        'global_conversion_rate': (converted / impressions) * 100 if impressions > 0 else 0,
    }
    return metrics