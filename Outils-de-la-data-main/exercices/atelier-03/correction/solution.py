"""
CORRECTION DE L'ATELIER 03 - STACK MODERNE DE DONNÉES
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
print("CORRECTION DE L'ATELIER 03 - STACK MODERNE DE DONNÉES")
print("="*60 + "\n")

print("""
GUIDE COMPLET - STACK MODERNE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ARCHITECTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Schéma complet du système
- Flux de données documentés
- Technologies choisies et justifiées
- Points d'intégration entre composants

2. INFRASTRUCTURE DOCKER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- docker-compose.yml complet
- Configuration de tous les services
- Volumes persistants
- Réseaux Docker
- Variables d'environnement

3. COLLECTE DE DONNÉES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Générateur de données en temps réel
- Ingestion dans PostgreSQL
- Validation de l'ingestion

4. TRANSFORMATION DBT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Modèles staging
- Modèles intermediate
- Modèles marts
- Tests de qualité
- Documentation

5. ORCHESTRATION AIRFLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- DAGs pour orchestrer dbt
- Dépendances configurées
- Gestion d'erreurs
- Monitoring

6. MONITORING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Grafana avec dashboards opérationnels
- Métriques de pipeline
- Métriques de données
- Métriques business
- Alertes configurées

7. DASHBOARD ANALYTIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Superset connecté au data warehouse
- Visualisations basées sur modèles dbt
- Dashboard métier organisé

8. DOCUMENTATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Architecture documentée
- Guide d'installation
- Guide d'utilisation
- Troubleshooting

BONNES PRATIQUES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Déployer un service à la fois
- Tester chaque composant individuellement
- Documenter au fur et à mesure
- Penser à la scalabilité
- Configuration production-ready
""")

print("\n" + "="*60)
print("FIN DE LA CORRECTION")
print("="*60)
print("\nNote : Cet atelier est un projet complet, adaptez-le à vos besoins.\n")

