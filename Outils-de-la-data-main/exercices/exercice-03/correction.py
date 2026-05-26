"""
CORRECTION DE L'EXERCICE 03 - PIPELINE ETL
Accès protégé par mot de passe
"""

import getpass
import os
import sys

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
print("CORRECTION DE L'EXERCICE 03 - PIPELINE ETL")
print("="*60 + "\n")

print("""
STRUCTURE RECOMMANDÉE DU PIPELINE ETL

1. ARCHITECTURE MODULAIRE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

pipeline/
├── __init__.py
├── extractors.py      # Classes pour l'extraction
├── transformers.py     # Classes pour la transformation
├── loaders.py          # Classes pour le chargement
└── pipeline.py         # Classe principale d'orchestration

2. EXTRACTORS (Extraction)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from abc import ABC, abstractmethod
import pandas as pd
import requests
import sqlite3

class Extractor(ABC):
    @abstractmethod
    def extract(self):
        pass

class CSVExtractor(Extractor):
    def __init__(self, file_path):
        self.file_path = file_path
    
    def extract(self):
        return pd.read_csv(self.file_path)

class APIExtractor(Extractor):
    def __init__(self, url, params=None):
        self.url = url
        self.params = params
    
    def extract(self):
        response = requests.get(self.url, params=self.params)
        return pd.DataFrame(response.json())

class DatabaseExtractor(Extractor):
    def __init__(self, db_path, query):
        self.db_path = db_path
        self.query = query
    
    def extract(self):
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query(self.query, conn)
        conn.close()
        return df

3. TRANSFORMERS (Transformation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class Transformer:
    def clean(self, df):
        # Suppression des doublons
        df = df.drop_duplicates()
        # Gestion des valeurs manquantes
        df = df.fillna(method='ffill')
        return df
    
    def enrich(self, df):
        # Ajout de colonnes calculées
        if 'prix' in df.columns and 'quantite' in df.columns:
            df['montant_total'] = df['prix'] * df['quantite']
        return df
    
    def validate(self, df):
        # Validation des types
        # Validation des contraintes métier
        return df
    
    def aggregate(self, df, group_by, agg_dict):
        return df.groupby(group_by).agg(agg_dict).reset_index()
    
    def transform(self, df):
        df = self.clean(df)
        df = self.enrich(df)
        df = self.validate(df)
        return df

4. LOADERS (Chargement)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from abc import ABC, abstractmethod

class Loader(ABC):
    @abstractmethod
    def load(self, data):
        pass

class CSVLoader(Loader):
    def __init__(self, output_path):
        self.output_path = output_path
    
    def load(self, data):
        data.to_csv(self.output_path, index=False)
        print(f"Données sauvegardées dans {self.output_path}")

class DatabaseLoader(Loader):
    def __init__(self, db_path, table_name):
        self.db_path = db_path
        self.table_name = table_name
    
    def load(self, data):
        conn = sqlite3.connect(self.db_path)
        data.to_sql(self.table_name, conn, if_exists='replace', index=False)
        conn.close()
        print(f"Données chargées dans {self.table_name}")

class JSONLoader(Loader):
    def __init__(self, output_path):
        self.output_path = output_path
    
    def load(self, data):
        data.to_json(self.output_path, orient='records', indent=2)
        print(f"Données sauvegardées dans {self.output_path}")

5. PIPELINE PRINCIPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import logging

class ETLPipeline:
    def __init__(self, extractor, transformer, loader):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader
        self.setup_logging()
    
    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def run(self):
        try:
            # Extract
            self.logger.info("Début de l'extraction...")
            data = self.extractor.extract()
            self.logger.info(f"Extraction terminée : {len(data)} lignes")
            
            # Transform
            self.logger.info("Début de la transformation...")
            data = self.transformer.transform(data)
            self.logger.info(f"Transformation terminée : {len(data)} lignes")
            
            # Load
            self.logger.info("Début du chargement...")
            self.loader.load(data)
            self.logger.info("Chargement terminé")
            
            return True
        except Exception as e:
            self.logger.error(f"Erreur dans le pipeline : {e}")
            return False

6. EXEMPLE D'UTILISATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Création des composants
extractor = CSVExtractor('donnees/ventes.csv')
transformer = Transformer()
loader = CSVLoader('output/ventes_clean.csv')

# Création et exécution du pipeline
pipeline = ETLPipeline(extractor, transformer, loader)
success = pipeline.run()

POINTS CLÉS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Utilisation de classes abstraites (ABC) pour les interfaces
✅ Pattern Strategy pour la flexibilité
✅ Séparation des responsabilités (Extract, Transform, Load)
✅ Gestion d'erreurs et logging
✅ Code modulaire et réutilisable
✅ Tests unitaires possibles sur chaque composant

BONNES PRATIQUES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Documenter chaque classe et méthode
- Utiliser des types hints pour la clarté
- Implémenter des tests pour chaque composant
- Gérer les erreurs de manière appropriée
- Utiliser le logging pour le suivi
- Penser à la performance (générateurs pour gros volumes)
""")

print("\n" + "="*60)
print("FIN DE LA CORRECTION")
print("="*60)
print("\nNote : Cette correction montre la structure et les concepts clés.")
print("Implémentez votre propre version en suivant ces principes.\n")

