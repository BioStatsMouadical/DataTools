# M2 Développement Informatique - Outils de la Data

## Bienvenue dans cette formation !

Bonjour et bienvenue dans ce cours sur les **Outils de la Data** !

Je suis **Abid Hamza**, votre formateur, et je suis ravi de vous accompagner dans cette formation. Ce dépôt contient toutes les ressources nécessaires pour maîtriser les outils essentiels de la data science et du traitement de données.

**Cette formation est conçue pour être entièrement autonome.** Vous pouvez travailler à votre rythme, suivre les instructions détaillées dans chaque exercice, et progresser étape par étape.

## Contenu du cours

Ce dépôt contient :

- **Slides de cours** : Présentation complète sur les outils de la data (format PowerPoint, HTML et Markdown)
- **Exercices pratiques** : 7 exercices progressifs utilisant de vrais outils open source
- **Ressources** : Documentation et liens utiles pour approfondir vos connaissances

## Objectifs de ce cours

À la fin de cette formation, vous serez capable de :

- Comprendre l'écosystème complet des outils de données
- Maîtriser les outils essentiels pour le traitement et l'analyse de données
- Installer et configurer des outils open source professionnels
- Créer des dashboards, visualisations et pipelines de données
- Choisir les bons outils selon le contexte de votre projet

## Structure du dépôt

```
.
├── slides/                          # Présentations du cours
│   ├── cours-outils-data.pptx      # Version PowerPoint (à utiliser)
│   ├── index.html                   # Version HTML interactive
│   └── cours-outils-data-format-word.md  # Version Markdown
├── exercices/                       # Exercices pratiques (autonomes)
│   ├── exercice-01/                 # Apache Superset - Business Intelligence
│   ├── exercice-02/                 # Metabase - Self-Service BI
│   ├── exercice-03/                 # ELK Stack - Analyse de logs
│   ├── exercice-04/                 # Apache Spark - Big Data
│   ├── exercice-05/                 # Grafana + Prometheus - Monitoring
│   ├── exercice-06/                 # Apache Airflow - Orchestration
│   ├── exercice-07/                 # dbt - Transformation SQL
│   └── README.md                    # Guide général des exercices
├── ressources/                      # Documentation et ressources
└── README.md                        # Ce fichier
```

## Comment commencer ?

### Étape 1 : Consulter les slides

1. **Ouvrez le fichier PowerPoint** : `slides/cours-outils-data-complet.pptx`
   - **Version recommandée** : 60 slides détaillés avec schémas
   - Contenu complet et bien expliqué
   - Prêt pour projection ou étude personnelle

2. **Alternatives** :
   - `slides/cours-outils-data.pptx` : Version précédente
   - `slides/index.html` : Version interactive dans un navigateur
   - `slides/cours-complet-50-slides.md` : Version Markdown source

3. **Lisez attentivement les slides** pour comprendre les concepts

### Étape 2 : Faire les exercices

1. **Commencez par l'exercice 01** dans l'ordre
2. **Lisez le README** de chaque exercice - il contient toutes les instructions
3. **Suivez les étapes** une par une
4. **Générez les données** si nécessaire avec les scripts fournis
5. **Testez régulièrement** votre travail

### Étape 3 : Soumettre vos solutions

Chaque exercice contient des instructions détaillées pour soumettre votre travail. En général :

1. Créez un dossier `solutions/votre-nom/` dans l'exercice
2. Placez tous vos fichiers de solution dedans
3. Suivez les instructions Git pour pousser votre travail

**Important** : Remplacez "votre-nom" par votre vrai nom (ex: `solutions/jean-dupont/`)

## Technologies et outils utilisés

Cette formation vous fera découvrir et utiliser :

- **Apache Superset** : Business Intelligence open source
- **Metabase** : Self-Service BI
- **ELK Stack** : Elasticsearch, Logstash, Kibana pour l'analyse de logs
- **Apache Spark** : Traitement Big Data distribué
- **Grafana + Prometheus** : Monitoring et observabilité
- **Apache Airflow** : Orchestration de workflows
- **dbt** : Transformation de données moderne

Tous ces outils sont **open source et gratuits**.

## Chaque exercice est autonome

Tous les exercices sont conçus pour être complétés de manière indépendante :

- Instructions détaillées étape par étape
- Scripts pour générer les données nécessaires
- Guide d'installation pour chaque outil
- Exemples et conseils
- Corrections disponibles (protégées par mot de passe)

## Corrections des exercices

Les corrections sont disponibles pour chaque exercice dans le fichier `correction.py`.

**Mot de passe pour accéder aux corrections : `Abidexercice123`**

Pour utiliser une correction :
```bash
cd exercice-XX
python correction.py
# Entrez le mot de passe lorsque demandé
```

**Conseil** : Essayez d'abord de faire l'exercice par vous-même, puis consultez la correction pour comparer votre approche.

## Comment soumettre vos réponses

### Méthode recommandée : Fork et Pull Request

1. **Forker le dépôt** :
   - Cliquez sur le bouton "Fork" en haut à droite de cette page GitHub
   - Cela crée une copie du dépôt dans votre compte

2. **Cloner votre fork** :
   ```bash
   git clone https://github.com/VOTRE_USERNAME/M2_DI_Outils-de-la-data.git
   cd M2_DI_Outils-de-la-data
   ```

3. **Créer une branche pour votre travail** :
   ```bash
   git checkout -b nom-prenom-exercice-01
   ```

4. **Travailler sur l'exercice** :
   - Allez dans le dossier de l'exercice
   - Créez un dossier `solutions/votre-nom/`
   - Placez vos fichiers de solution dedans
   - Suivez les instructions dans le README de l'exercice

5. **Ajouter et commiter** :
   ```bash
   git add .
   git commit -m "Solution exercice 01 - Votre Nom"
   git push origin nom-prenom-exercice-01
   ```

6. **Créer une Pull Request** sur GitHub

### Structure de soumission

Pour chaque exercice, créez un dossier avec votre nom :

```
exercices/
└── exercice-01/
    ├── README.md
    ├── donnees/
    └── solutions/
        └── votre-nom/
            ├── solution.py (ou autres fichiers)
            ├── resultats.md
            └── README.md (optionnel)
```

## Checklist avant de soumettre

Avant de pousser votre solution, vérifiez que :

- [ ] J'ai lu et compris toutes les instructions de l'exercice
- [ ] Mon code fonctionne sans erreur
- [ ] Mon code est commenté et lisible
- [ ] J'ai créé un dossier avec mon nom dans `solutions/`
- [ ] J'ai ajouté un fichier `resultats.md` expliquant ma solution
- [ ] Tous les fichiers demandés sont présents
- [ ] Mon commit message est clair et contient mon nom

## Besoin d'aide ?

Si vous êtes bloqué :

1. **Relisez attentivement le README** de l'exercice
2. **Consultez la documentation** dans le dossier `ressources/`
3. **Ouvrez une issue** sur ce dépôt GitHub pour poser votre question
4. **Consultez la correction** (après avoir essayé) avec le mot de passe

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Contact

Pour toute question, n'hésitez pas à ouvrir une issue sur ce dépôt GitHub.

---

**Bon courage et bon apprentissage !**

*Abid Hamza - Formateur*
