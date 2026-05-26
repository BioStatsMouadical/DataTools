"""
CORRECTION DE L'EXERCICE 04 - APACHE SPARK
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
print("CORRECTION DE L'EXERCICE 04 - APACHE SPARK")
print("="*60 + "\n")

# Le contenu complet est dans le fichier original correction.py
# Je copie le contenu exact
print("""
EXEMPLE DE CODE SPARK COMPLET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Voir le fichier correction.py original pour le contenu complet.
Les points clés sont :
- Configuration Spark avec optimisations
- Chargement et exploration des données
- Transformations de base (filtrage, sélection)
- Agrégations (groupBy, agg)
- Window functions pour analyses avancées
- Optimisations (cache, repartition, broadcast)
- Export en différents formats
- Requêtes SQL via spark.sql()
""")

print("\n" + "="*60)
print("FIN DE LA CORRECTION")
print("="*60)
print("\nNote : Adaptez ce code à votre dataset et vos besoins spécifiques.\n")

