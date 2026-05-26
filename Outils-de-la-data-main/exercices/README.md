# Exercices et Ateliers - Outils de la Data

## Vue d'ensemble

Ce dossier contient tous les exercices et ateliers pratiques pour le cours. Chaque exercice est **autonome** et contient toutes les données et instructions nécessaires.

## Structure des exercices

Chaque exercice suit cette structure :

```
exercice-XX/
├── README.md              # Instructions complètes et détaillées
├── generer_donnees.py     # Script pour générer les données (si applicable)
├── donnees/               # Dossier pour les données générées
└── solutions/             # Dossier pour vos solutions
    └── votre-nom/         # Créez un dossier avec votre nom
```

## Liste des exercices

### Exercices de base

| Exercice | Sujet | Durée | Outils principaux | Données |
|----------|-------|-------|-------------------|---------|
| [Exercice 01](exercice-01/) | Manipulation Pandas | 1h | Pandas, Matplotlib | Générées |
| [Exercice 02](exercice-02/) | Analyse SQL | 1h | SQLite, Python | Générées |
| [Exercice 03](exercice-03/) | Pipeline ETL | 2h | Python, Classes | À créer |
| [Exercice 04](exercice-04/) | Apache Spark | 2h | PySpark | Générées |

### Exercices outils open source

| Exercice | Sujet | Durée | Outils principaux | Installation |
|----------|-------|-------|-------------------|-------------|
| [Exercice 05](exercice-05/) | Grafana | 8h | Grafana, Docker | Instructions incluses |
| [Exercice 06](exercice-06/) | Apache Airflow | 10h | Airflow, Docker | Instructions incluses |
| [Exercice 07](exercice-07/) | dbt | 11h | dbt, PostgreSQL | Instructions incluses |

### Ateliers projets complets

| Atelier | Sujet | Durée | Description |
|---------|-------|-------|-------------|
| [Atelier 01](atelier-01/) | Dashboard analytique | 14-16h | Projet complet de bout en bout |
| [Atelier 02](atelier-02/) | ML Pipeline | 15-17h | Pipeline ML de production |
| [Atelier 03](atelier-03/) | Stack moderne | 15h | Intégration complète d'outils |

**Total estimé : 40-42 heures**

## Comment utiliser les exercices

### 1. Préparation

1. **Lire le README** de l'exercice pour comprendre les objectifs
2. **Installer les dépendances** nécessaires (voir section Installation)
3. **Générer les données** si un script `generer_donnees.py` est fourni :
   ```bash
   cd exercice-XX
   python generer_donnees.py
   ```

### 2. Travail sur l'exercice

1. **Créer votre dossier de solution** :
   ```bash
   mkdir -p solutions/votre-nom
   cd solutions/votre-nom
   ```

2. **Suivre les instructions** étape par étape dans le README
3. **Tester régulièrement** votre code
4. **Documenter** votre approche dans un fichier `resultats.md`

### 3. Soumission

Suivez les instructions dans le README principal du dépôt pour soumettre vos solutions.

## Installation des outils open source

### Grafana (Exercice 05)

**Avec Docker** (recommandé) :
```bash
docker run -d -p 3000:3000 --name=grafana grafana/grafana:latest
```

**Installation native** : Voir les instructions dans `exercice-05/README.md`

### Apache Airflow (Exercice 06)

**Avec Docker** (recommandé) :
```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.7.0/docker-compose.yaml'
docker-compose up airflow-init
docker-compose up -d
```

**Installation native** : Voir les instructions dans `exercice-06/README.md`

### dbt (Exercice 07)

```bash
pip install dbt-postgres  # Pour PostgreSQL
# ou
pip install dbt-sqlite    # Pour SQLite
```

Voir les instructions détaillées dans `exercice-07/README.md`

## Progression recommandée

### Semaine 1-2 : Fondamentaux
- Exercice 01 : Pandas (1h)
- Exercice 02 : SQL (1h)
- Exercice 03 : Pipeline ETL (2h)
- Exercice 04 : Spark (2h)

### Semaine 3-4 : Outils open source
- Exercice 05 : Grafana (8h)
- Exercice 06 : Airflow (10h)

### Semaine 5-6 : Transformation et projets
- Exercice 07 : dbt (11h)
- Atelier 01 : Dashboard (14-16h)

### Semaine 7-8 : Projets avancés
- Atelier 02 : ML Pipeline (15-17h)
- Atelier 03 : Stack moderne (15h)

## Conseils généraux

1. **Commencez simple** : Faites les exercices dans l'ordre
2. **Lisez attentivement** : Les README contiennent toutes les informations
3. **Testez régulièrement** : Ne pas attendre la fin pour tester
4. **Documentez** : Prenez des notes sur votre approche
5. **Demandez de l'aide** : Ouvrez une issue si vous êtes bloqué

## Ressources

- Documentation des outils dans `../ressources/README.md`
- Guide du formateur dans `../GUIDE_FORMATEUR.md`
- Instructions de soumission dans `../README.md`

## Support

Pour toute question :
1. Consultez le README de l'exercice
2. Consultez la documentation dans `ressources/`
3. Ouvrez une issue sur GitHub

---

**Bon courage avec les exercices !**

