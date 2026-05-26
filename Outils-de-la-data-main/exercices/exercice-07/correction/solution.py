"""
CORRECTION DE L'EXERCICE 07 - DBT
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
print("CORRECTION DE L'EXERCICE 07 - DBT")
print("="*60 + "\n")

# Le contenu complet est dans le fichier original correction.py
print("""
GUIDE COMPLET DBT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Voir le fichier correction.py original pour les exemples complets.
Les points clés sont :
- Structure des modèles (staging, intermediate, marts)
- Utilisation de ref() et source()
- Macros personnalisées
- Tests de qualité des données
- Documentation automatique
- Commandes dbt principales
""")

print("\n" + "="*60)
print("FIN DE LA CORRECTION")
print("="*60)
print("\nNote : Adaptez ces exemples à votre structure de données.\n")

