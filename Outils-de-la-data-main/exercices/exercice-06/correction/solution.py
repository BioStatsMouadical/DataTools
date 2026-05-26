"""
CORRECTION DE L'EXERCICE 06 - APACHE AIRFLOW
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
print("CORRECTION DE L'EXERCICE 06 - APACHE AIRFLOW")
print("="*60 + "\n")

# Le contenu complet est dans le fichier original correction.py
print("""
GUIDE COMPLET APACHE AIRFLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Voir le fichier correction.py original pour les exemples complets de DAGs.
Les points clés sont :
- Structure d'un DAG simple
- DAGs complexes avec dépendances parallèles
- Gestion d'erreurs et retries
- Variables et connexions
- Scheduling avec cron
- Utilisation de XCom pour passer des données
""")

print("\n" + "="*60)
print("FIN DE LA CORRECTION")
print("="*60)
print("\nNote : Adaptez ces exemples à vos besoins spécifiques.\n")

