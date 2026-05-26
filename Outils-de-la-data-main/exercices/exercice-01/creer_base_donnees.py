"""
Script pour créer une base de données SQLite à partir du CSV
Pour utiliser avec Apache Superset
"""

import pandas as pd
import sqlite3
import os

# Créer le dossier donnees s'il n'existe pas
os.makedirs('donnees', exist_ok=True)

# Lire le CSV
print("Lecture du fichier CSV...")
df = pd.read_csv('donnees/ventes.csv')

# Calculer le montant total
df['montant_total'] = df['quantite'] * df['prix_unitaire']

# Convertir la date
df['date'] = pd.to_datetime(df['date'])

# Créer la base de données SQLite
print("Création de la base de données...")
conn = sqlite3.connect('donnees/ventes.db')

# Sauvegarder dans SQLite
df.to_sql('ventes', conn, if_exists='replace', index=False)

# Créer un index pour améliorer les performances
conn.execute('CREATE INDEX idx_date ON ventes(date)')
conn.execute('CREATE INDEX idx_categorie ON ventes(categorie)')
conn.execute('CREATE INDEX idx_produit ON ventes(produit)')

conn.commit()
conn.close()

print(f"✅ Base de données créée : donnees/ventes.db")
print(f"   - {len(df)} lignes")
print(f"   - Table 'ventes' créée avec succès")
print(f"   - Index créés pour optimiser les requêtes")

