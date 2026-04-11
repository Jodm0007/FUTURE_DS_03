# 📄 Rapport d'Analyse : Performance de la Campagne Marketing (Funnel)

**Projet :** FUTURE_DS_03 - Bank Marketing Campaign
**Date :** Avril 2026
**Analyste :** Data Scientist (Intern)



## 1. Contexte et Objectifs
L'objectif de cette analyse est de décortiquer les performances d'une campagne de démarchage téléphonique pour la souscription à un produit bancaire (dépôt à terme / term deposit).
En structurant ces données sous forme d'**Entonnoir de Conversion (Funnel)**, nous cherchons à identifier :

1. Où déperd-on le plus de clients potentiels ?
2. Quels sont les profils socio-démographiques les plus réceptifs ?
3. Quelles actions commerciales mettre en place pour améliorer le ROI.



## 2. Qualité des données (Data Cleaning)
Le jeu de données initial a été nettoyé et préparé pour l'analyse :
* **Valeurs manquantes** : Suppression ou imputation des variables inexploitables.
* **Typage** : Les colonnes de date et les catégories textuelles ont été mises au propre.
* **Création de variables (Feature Engineering)** : 
    * `showed_interest` : client n'ayant pas raccroché immédiatement.
    * `converted` : client ayant souscrit.
    * `funnel_stage` : Classification de chaque individu dans son stade d'évolution.
* **Volume final** : **775** leads qualifiés sur lesquels se base cette analyse.



## 3. Analyse de l'Entonnoir (Funnel Analysis)

### 3.1. Les Métriques Clés (KPIs)
Sur l'ensemble des prospects de cette base :
- 🎯 **Impressions (Ciblage) :** 775
- 📞 **Contacted (Appelés) :** 775 *(Taux de joignabilité : 100%)*
- 🤝 **Engaged (Intéressés) :** 694 *(Taux d'engagement : **89.5%**)*
- 💰 **Converted (Souscrits) :** 173 *(Taux de conversion global : **22.3%**)*

### 3.2. L'Analyse des "Drop-offs" (Points de Friction)
La perte de clients n'est pas linéaire de l'acquisition à la vente finale :
- **Perte très faible (10.5%)** entre le premier contact et l'engagement initial. L'équipe d'appels sait très bien accrocher l'attention.
- **Perte critique (75.1%)** entre l'engagement et la vente. C'est le goulot d'étranglement de la campagne. Les clients écoutent, mais le passage à l'acte échoue dans 3 cas sur 4.


## 4. Analyse Dimensionnelle (Profils et Comportements)

### A. Les segments phares (Par profession)
Bien que les postes de Management et d'Administration fournissent le volume le plus important de contrats, ce ne sont pas eux qui ont le meilleur taux de réussite individuel :
* **Étudiants** : Taux record de **42.1%**.
* **Retraités** : Excellent taux de **31.8%**.

### B. Canaux de communication (Cellular vs Telephone)
Le canal n'apporte **aucune différence** sur le taux de conversion brut (22.4% pour mobile, 22.4% pour fixe). Néanmoins, 90% du volume est fait via téléphone portable. L'achat de bases de données fixes n'est donc plus stratégique à l'heure actuelle.

### C. La durée des appels
Il y a une corrélation extrêmement nette entre le **temps passé au téléphone** et le succès de l'opération :
* Appel non-converti : Médiane ~ **150 secondes** (moins de 3 minutes).
* Appel converti : Médiane ~ **300-350 secondes** (5 à 6 minutes).


## 5. Recommandations Métier & Plan d'Action Stratégique

Pour maximiser le ROI de la prochaine campagne de prospection, nous recommandons la mise en place des actions suivantes :

1. **Ateliers de "Closing" (Conclusion de vente)** : Le taux d'engagement de 89% prouve que l'introduction est bonne. Il faut former les équipes sur les "10 dernières secondes" de vente pour adresser les ultimes freins (prix, engagement). Réduire ce drop-off de 75% à 65% doublerait presque les revenus.
2. **Ciblage Étudiants / Retraités (Micro-Segmenting)** : Créer une offre / campagne spécifique pour ces catégories, afin d'exploiter leur taux de conversion exceptionnel (jusqu'à 42%).
3. **Optimiser la règle des "4 minutes"** : Implémenter un système visuel qui indique au téléprospecteur que son appel dépasse les 4 minutes. Ce lead passe statistiquement du statut "froid" à "très chaud" : le téléprospecteur doit avoir la consigne de faire une concession financière si besoin pour conclure.


*Analyse générée de bout en bout grâce aux pipelines Python d'ETL et de Data Visualization*
