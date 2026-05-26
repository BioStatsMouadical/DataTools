"""
CORRECTION DE L'EXERCICE 05 - GRAFANA
Accès protégé par mot de passe
"""

import getpass

def verifier_mot_de_passe():
    """Vérifie le mot de passe avant d'afficher la correction"""
    mot_de_passe = getpass.getpass("Entrez le mot de passe pour accéder à la correction : ")
    if mot_de_passe == "Abidexercice123":
        return True
    else:
        print("❌ Mot de passe incorrect. Accès refusé.")
        return False

if not verifier_mot_de_passe():
    exit()

print("\n" + "="*60)
print("CORRECTION DE L'EXERCICE 05 - GRAFANA")
print("="*60 + "\n")

print("""
GUIDE COMPLET GRAFANA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. CONFIGURATION DE LA SOURCE DE DONNÉES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Pour utiliser les métriques CSV :
- Installer le plugin CSV datasource
- Ou convertir CSV en base de données (MySQL/PostgreSQL)
- Ou utiliser InfluxDB pour time-series

Option recommandée : Convertir CSV en SQLite/MySQL

2. CRÉATION DE PANNEAUX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PANNEAU 1 : Graphique de ligne - Évolution CPU
────────────────────────────────────────────────────────────────────────────
Type : Time series
Query :
  SELECT
    timestamp as time,
    cpu_percent as value
  FROM metriques
  WHERE serveur = '$serveur'
  ORDER BY time

PANNEAU 2 : Graphique en barres - Mémoire par serveur
────────────────────────────────────────────────────────────────────────────
Type : Bar chart
Query :
  SELECT
    serveur,
    AVG(memory_percent) as mem_moyenne
  FROM metriques
  GROUP BY serveur
  ORDER BY mem_moyenne DESC

PANNEAU 3 : Gauge - Utilisation disque
────────────────────────────────────────────────────────────────────────────
Type : Gauge
Query :
  SELECT
    AVG(disk_percent) as value
  FROM metriques
  WHERE serveur = '$serveur'

Min : 0
Max : 100
Thresholds :
  - Green : 0-70
  - Yellow : 70-85
  - Red : 85-100

PANNEAU 4 : Stat - Nombre total de requêtes
────────────────────────────────────────────────────────────────────────────
Type : Stat
Query :
  SELECT
    SUM(requests_per_second) as value
  FROM metriques

PANNEAU 5 : Table - Top 10 serveurs par CPU
────────────────────────────────────────────────────────────────────────────
Type : Table
Query :
  SELECT
    serveur,
    AVG(cpu_percent) as cpu_moyen,
    MAX(cpu_percent) as cpu_max,
    AVG(memory_percent) as mem_moyenne
  FROM metriques
  GROUP BY serveur
  ORDER BY cpu_moyen DESC
  LIMIT 10

3. VARIABLES DE DASHBOARD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Variable 1 : serveur
Type : Query
Query : SELECT DISTINCT serveur FROM metriques
Label : Serveur
Multi-value : Oui
Include All : Oui

Variable 2 : periode
Type : Custom
Options :
  - Dernière heure
  - Dernières 24h
  - Dernière semaine
  - Dernier mois

4. ALERTES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ALERTE 1 : CPU > 80%
────────────────────────────────────────────────────────────────────────────
Condition : WHEN avg() OF query(A, 5m, now) IS ABOVE 80
Evaluation : Every 1m for 5m
Message : CPU élevé sur $serveur : {{ $value }}%

ALERTE 2 : Mémoire < 10% disponible
────────────────────────────────────────────────────────────────────────────
Condition : WHEN avg() OF query(A, 5m, now) IS BELOW 10
Evaluation : Every 1m for 5m
Message : Mémoire faible sur $serveur : {{ $value }}%

ALERTE 3 : Disque > 90%
────────────────────────────────────────────────────────────────────────────
Condition : WHEN avg() OF query(A, 5m, now) IS ABOVE 90
Evaluation : Every 1m for 5m
Message : Disque presque plein sur $serveur : {{ $value }}%

5. EXPORT DU DASHBOARD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Dashboard > Settings > JSON Model
- Copier le JSON
- Sauvegarder dans dashboard.json

6. BONNES PRATIQUES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Organiser les panneaux par catégorie (CPU, Mémoire, Disque, Réseau)
✅ Utiliser des couleurs cohérentes
✅ Ajouter des annotations pour les événements importants
✅ Configurer l'auto-refresh (ex: 30s)
✅ Utiliser les variables pour la flexibilité
✅ Documenter chaque panneau avec une description
✅ Tester les alertes avant de les activer

7. STRUCTURE DU DASHBOARD RECOMMANDÉE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Row 1 : Vue d'ensemble
  - Stat : Total requêtes
  - Stat : Serveurs actifs
  - Stat : CPU moyen
  - Stat : Mémoire moyenne

Row 2 : Métriques CPU
  - Time series : CPU par serveur
  - Gauge : CPU moyen global
  - Table : Top serveurs par CPU

Row 3 : Métriques Mémoire
  - Time series : Mémoire par serveur
  - Bar chart : Mémoire moyenne par serveur
  - Gauge : Mémoire moyenne globale

Row 4 : Métriques Disque
  - Time series : Disque par serveur
  - Gauge : Disque moyen
  - Table : Serveurs avec disque élevé

Row 5 : Réseau et Performance
  - Time series : Requêtes par seconde
  - Time series : Latence
  - Time series : Trafic réseau
""")

print("\n" + "="*60)
print("FIN DE LA CORRECTION")
print("="*60)
print("\nNote : Adaptez ces configurations à votre source de données.\n")

