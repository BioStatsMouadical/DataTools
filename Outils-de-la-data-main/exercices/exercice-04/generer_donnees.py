"""
Script pour générer un dataset volumineux pour l'exercice 04 (Apache Spark)
Exécutez ce script pour créer le fichier transactions_large.csv
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Créer le dossier donnees s'il n'existe pas
os.makedirs('donnees', exist_ok=True)

# Paramètres
np.random.seed(42)
nb_transactions = 100000  # 100k transactions pour tester Spark
date_debut = datetime(2023, 1, 1)

print("Génération des données...")

# Produits et catégories
produits_data = {
    'Electronique': ['Ordinateur', 'Tablette', 'Smartphone', 'Écran', 'Souris', 'Clavier', 'Casque', 'Webcam'],
    'Mobilier': ['Chaise', 'Bureau', 'Étagère', 'Fauteuil', 'Table', 'Lampe', 'Meuble'],
    'Education': ['Livre Python', 'Livre ML', 'Formation Data', 'Formation SQL', 'Cours Online'],
    'Vêtements': ['T-shirt', 'Pantalon', 'Veste', 'Chaussures', 'Accessoire'],
    'Alimentation': ['Produit Bio', 'Snack', 'Boisson', 'Repas']
}

# Génération des données
transactions = []

for i in range(nb_transactions):
    if (i + 1) % 10000 == 0:
        print(f"  Génération : {i + 1}/{nb_transactions}...")
    
    # Date
    jours_offset = np.random.randint(0, 730)  # 2 ans
    date = date_debut + timedelta(days=jours_offset)
    
    # Catégorie et produit
    categorie = np.random.choice(list(produits_data.keys()))
    produit = np.random.choice(produits_data[categorie])
    
    # Prix selon catégorie
    prix_ranges = {
        'Electronique': (50, 1000),
        'Mobilier': (40, 600),
        'Education': (20, 500),
        'Vêtements': (10, 200),
        'Alimentation': (5, 50)
    }
    prix_min, prix_max = prix_ranges[categorie]
    prix = round(np.random.uniform(prix_min, prix_max), 2)
    
    # Quantité
    quantite = np.random.randint(1, 10)
    
    # Client
    client_id = f'CL{str(np.random.randint(1, 5000)).zfill(4)}'
    
    # Transaction
    transaction_id = f'TXN{str(i + 1).zfill(8)}'
    
    transactions.append({
        'transaction_id': transaction_id,
        'date': date.strftime('%Y-%m-%d'),
        'client_id': client_id,
        'produit': produit,
        'categorie': categorie,
        'quantite': quantite,
        'prix_unitaire': prix,
        'montant_total': round(prix * quantite, 2),
        'region': np.random.choice(['Nord', 'Sud', 'Est', 'Ouest', 'Centre']),
        'canal': np.random.choice(['Online', 'Magasin', 'Mobile', 'Téléphone'])
    })

# Création du DataFrame
df = pd.DataFrame(transactions)

# Tri par date
df = df.sort_values('date').reset_index(drop=True)

# Sauvegarde
print("Sauvegarde du fichier...")
df.to_csv('donnees/transactions_large.csv', index=False, encoding='utf-8')

print(f"\n✅ Fichier transactions_large.csv créé avec succès !")
print(f"   - {len(df):,} transactions générées")
print(f"   - Période : {df['date'].min()} à {df['date'].max()}")
print(f"   - {df['produit'].nunique()} produits différents")
print(f"   - {df['client_id'].nunique()} clients différents")
print(f"   - Taille du fichier : {os.path.getsize('donnees/transactions_large.csv') / (1024*1024):.2f} MB")

