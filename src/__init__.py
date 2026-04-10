"""
Package `src` pour le projet FUTURE_DS_03.
Contient des modules réutilisables pour le nettoyage, le chargement, les métriques et la visualisation du funnel.
"""

# Importations relatives avec le "." pour un accès direct depuis "import src"
from .data_loading import (
    load_data, 
    load_excel_data
)

from .data_cleaning import (
    clean_unknown_values,
    clean_missing_values,
    clean_duplicates,
    clean_numeric_types,
    convert_target_to_binary,
    add_funnel_stage,
    add_showed_interest
)

from .funnel_metrics import (
    calculate_funnel_metrics,
    calculate_conversion_by_dimension,
    calculate_conversion_by_segment
)

from .funnel_analysis_functions import (
    get_funnel_stages,
    get_funnel_metrics
)

from .visualization_utils import (
    plot_funnel_chart,
    plot_conversion_by_dimension,
    plot_dropoff_analysis,
    plot_conversion_vs_duration
)
from src.utils import setup_logger, ensure_directory_exists

# Définir explicitement ce qui est exporté quand on fait "from src import *"
__all__ = [
    # data_loading
    'load_data', 'load_excel_data',
    
    # data_cleaning
    'clean_unknown_values', 'clean_missing_values', 'clean_duplicates',
    'clean_numeric_types', 'convert_target_to_binary', 'add_funnel_stage',
    'add_showed_interest', 
    
    # funnel_metrics
    'calculate_funnel_metrics', 'calculate_conversion_by_dimension', 'calculate_conversion_by_segment',
    
    # funnel_analysis_functions
    'get_funnel_stages', 'get_funnel_metrics',
    
    # visualization_utils
    'plot_funnel_chart', 'plot_conversion_by_dimension', 'plot_dropoff_analysis', 'plot_conversion_vs_duration'
]
