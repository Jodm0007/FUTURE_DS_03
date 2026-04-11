"""
#Autor: Joseph DATE-MASSE
src/visualization_utils.py
Fonctions de visualisation pour l'analyse du funnel marketing.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, Optional, List
from funnel_metrics import calculate_conversion_by_dimension

# Style professionnel
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("viridis")

def plot_funnel_chart(stages: Dict[str, int], save_path: Optional[str] = None):
    """
    Dessine un funnel chart pour visualiser les drop-offs.
    
    Args:
        stages: Dictionnaire {étape: nombre de leads}
        save_path: Chemin pour sauvegarder l'image (optionnel)
    """
    stages_df = pd.DataFrame({
        'stage': list(stages.keys()),
        'count': list(stages.values())
    })
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Barres horizontales avec dégradé
    colors = plt.cm.Blues(np.linspace(0.4, 0.9, len(stages_df)))
    bars = ax.barh(stages_df['stage'], stages_df['count'], color=colors)
    
    # Ajouter les valeurs sur les barres
    for bar, count in zip(bars, stages_df['count']):
        ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, 
                f'{count:,}', va='center', fontsize=10)
    
    # Calculer et afficher les drop-offs
    for i in range(len(stages_df) - 1):
        current = stages_df.iloc[i]['count']
        next_ = stages_df.iloc[i + 1]['count']
        dropoff = ((current - next_) / current) * 100
        ax.text(current / 2, stages_df.iloc[i]['stage'], 
                f'⬇️ {dropoff:.1f}%', ha='center', va='bottom', fontsize=9)
    
    ax.set_xlabel('Nombre de leads', fontsize=12)
    ax.set_title('Marketing Funnel - Analyse des Drop-offs', fontsize=14, fontweight='bold')
    ax.invert_yaxis()
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"✅ Funnel chart sauvegardé : {save_path}")
    
    plt.show()


def plot_conversion_by_dimension(
    df: pd.DataFrame, 
    dimension: str, 
    top_n: int = 10,
    save_path: Optional[str] = None
):
    """
    Affiche les taux de conversion par dimension catégorielle.
    
    Args:
        df: DataFrame avec colonne 'converted'
        dimension: Colonne à analyser (ex: 'job', 'contact', 'month')
        top_n: Nombre de catégories à afficher
        save_path: Chemin pour sauvegarder l'image
    """
    from funnel_metrics import calculate_conversion_by_dimension

    conv_df = calculate_conversion_by_dimension(df, dimension, top_n)
    
    fig, ax = plt.subplots(figsize=(12, max(6, top_n * 0.4)))
    
    # Déterminer la couleur selon performance
    colors = ['green' if x >= 15 else 'orange' if x >= 10 else 'red' 
              for x in conv_df['conversion_rate']]
    
    bars = ax.barh(conv_df[dimension], conv_df['conversion_rate'], color=colors)
    
    # Ajouter les labels
    for bar, rate, total in zip(bars, conv_df['conversion_rate'], conv_df['total_contacts']):
        ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
                f'{rate:.1f}% (n={total})', va='center', fontsize=9)
    
    ax.axvline(x=df['converted'].mean() * 100, color='blue', linestyle='--', 
               label=f'Moyenne globale: {df["converted"].mean() * 100:.1f}%')
    
    ax.set_xlabel('Taux de conversion (%)', fontsize=12)
    ax.set_title(f'Taux de conversion par {dimension}', fontsize=14, fontweight='bold')
    ax.legend()
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"✅ Graphique sauvegardé : {save_path}")
    
    plt.show()


def plot_dropoff_analysis(stages: Dict[str, int], save_path: Optional[str] = None):
    """
    Visualise les drop-offs entre chaque étape du funnel.
    """
    stages_list = list(stages.keys())
    dropoffs = []
    
    for i in range(len(stages_list) - 1):
        current = stages[stages_list[i]]
        next_ = stages[stages_list[i + 1]]
        dropoff = ((current - next_) / current) * 100
        dropoffs.append(dropoff)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    stages_pair = [f"{stages_list[i]} → {stages_list[i+1]}" for i in range(len(stages_list)-1)]
    colors = ['red' if d > 50 else 'orange' if d > 30 else 'yellowgreen' for d in dropoffs]
    
    bars = ax.bar(stages_pair, dropoffs, color=colors)
    
    # Ajouter les valeurs sur les barres
    for bar, dropoff in zip(bars, dropoffs):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{dropoff:.1f}%', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    ax.set_ylabel('Taux de drop-off (%)', fontsize=12)
    ax.set_title('Analyse des points de friction dans le funnel', fontsize=14, fontweight='bold')
    ax.set_ylim(0, 100)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    
    plt.show()


def plot_conversion_vs_duration(df: pd.DataFrame, save_path: Optional[str] = None):
    """
    Analyse la relation entre durée d'appel et conversion.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Boxplot
    sns.boxplot(data=df, x='converted', y='duration', ax=axes[0])
    axes[0].set_xticklabels(['Non-convertis', 'Convertis'])
    axes[0].set_ylabel('Durée d\'appel (secondes)')
    axes[0].set_title('Distribution de la durée selon conversion')
    
    # Histogramme superposé
    for converted in [0, 1]:
        subset = df[df['converted'] == converted]
        label = 'Convertis' if converted == 1 else 'Non-convertis'
        axes[1].hist(subset['duration'], bins=30, alpha=0.5, label=label)
    
    axes[1].set_xlabel('Durée d\'appel (secondes)')
    axes[1].set_ylabel('Fréquence')
    axes[1].set_title('Distribution des durées par statut')
    axes[1].legend()
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    
    plt.show()