"""
CORRECTION DE L'ATELIER 02 - PIPELINE MACHINE LEARNING
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
print("CORRECTION DE L'ATELIER 02 - PIPELINE MACHINE LEARNING")
print("="*60 + "\n")

print("""
GUIDE COMPLET - PIPELINE ML
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. DÉFINITION DU PROBLÈME
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Choix d'un problème métier concret
- Définition de la variable cible
- Sélection des métriques de succès appropriées
- Documentation du contexte métier

2. EXPLORATION ET PRÉPARATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- EDA approfondie (univariée, multivariée)
- Détection et gestion des outliers
- Feature engineering créatif
- Encodage des variables catégorielles
- Normalisation/standardisation
- Gestion des valeurs manquantes
- Sélection de features

3. MODÉLISATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Baseline simple (régression linéaire, arbre simple)
- Test de plusieurs algorithmes (3+)
- Hyperparameter tuning (GridSearch/RandomSearch)
- Validation croisée
- Optimisation des métriques

4. ÉVALUATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Métriques appropriées (accuracy, precision, recall, F1, ROC-AUC)
- Validation sur ensemble de test
- Analyse des erreurs
- Interprétabilité (feature importance, SHAP)
- Comparaison des modèles

5. PIPELINE DE PRODUCTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Pipeline sklearn complet (preprocessing + model)
- Sauvegarde/chargement du modèle
- API REST (Flask/FastAPI)
- Validation des inputs
- Gestion d'erreurs
- Tests unitaires et d'intégration

6. DOCUMENTATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Documentation du modèle (méthodologie, performances)
- Guide d'utilisation de l'API
- README complet
- Limitations et améliorations futures

BONNES PRATIQUES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Code modulaire et testé
- Feature engineering documenté
- Validation rigoureuse
- Penser à la production dès le début
- Métriques métier en plus des métriques techniques
""")

print("\n" + "="*60)
print("FIN DE LA CORRECTION")
print("="*60)
print("\nNote : Cet atelier est un projet complet, adaptez-le à votre problème.\n")

