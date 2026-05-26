"""
CORRECTION DE L'ATELIER 01 - DASHBOARD ANALYTIQUE COMPLET
Accès protégé par mot de passe
"""

import getpass

def verifier_mot_de_passe():
    """Vérifie le mot de passe avant d'afficher la correction"""
    mot_de_passe = getpass.getpass("Entrez le mot de passe pour accéder à la correction : ")
    if mot_de_passe == "Abidexercice123":
        return True
    else:
        print("Mot de passe incorrect. Accès refusé.")
        return False

if not verifier_mot_de_passe():
    exit()

print("\n" + "="*60)
print("CORRECTION DE L'ATELIER 01 - DASHBOARD ANALYTIQUE COMPLET")
print("="*60 + "\n")

print("""
GUIDE COMPLET - DASHBOARD ANALYTIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. STRUCTURE DU PROJET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Organiser le code en modules (data_preparation, analysis, visualizations)
- Séparer les données (raw, processed, final)
- Créer des notebooks pour l'exploration
- Structurer le dashboard par pages/thèmes

2. PRÉPARATION DES DONNÉES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Pipeline reproductible avec fonctions modulaires
- Gestion des valeurs manquantes et outliers
- Création de métriques calculées
- Segmentation des clients
- Calcul de KPIs métier

3. ANALYSES EXPLORATOIRES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Statistiques descriptives complètes
- Analyses univariées et multivariées
- Corrélations entre variables
- Analyses métier (ventes, clients, produits)
- Identification d'insights actionnables

4. VISUALISATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Au moins 10 visualisations variées
- Choix approprié du type de graphique
- Couleurs cohérentes et accessibles
- Annotations et titres clairs
- Interactivité (filtres, drill-down)

5. DASHBOARD INTERACTIF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Structure multi-pages (Streamlit/Dash)
- Filtres interactifs fonctionnels
- Mise à jour dynamique des graphiques
- Design responsive
- Export des données

6. DOCUMENTATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- README complet avec instructions
- Documentation du code
- Présentation métier (slides)
- Rapport d'analyse détaillé
- Storytelling des données

BONNES PRATIQUES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Code modulaire et réutilisable
- Tests avec utilisateurs réels
- UX pensée pour les utilisateurs finaux
- Documentation claire et complète
- Présentation professionnelle
""")

print("\n" + "="*60)
print("FIN DE LA CORRECTION")
print("="*60)
print("\nNote : Cet atelier est un projet complet, adaptez-le à vos besoins.\n")

