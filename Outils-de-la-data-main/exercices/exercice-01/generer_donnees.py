"""
Script pour générer les données de l'exercice 01
Exécutez ce script pour créer le fichier ventes.csv
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Créer le dossier donnees s'il n'existe pas
os.makedirs('donnees', exist_ok=True)

# Paramètres
np.random.seed(42)
nb_lignes = 200
date_debut = datetime(2024, 1, 1)

# Génération des données
produits = [
    'Ordinateur Portable', 'Souris Sans Fil', 'Clavier Mécanique', 'Tablette',
    'Chaise Bureau', 'Bureau Ergonomique', 'Écran 27 pouces', 'Livre Python',
    'Casque Audio', 'Webcam HD', 'Formation Data Science', 'Étagère',
    'SSD 1TB', 'Livre Machine Learning', 'Lampe Bureau', 'Smartphone',
    'Formation Python', 'Fauteuil Bureau', 'Disque Dur Externe', 'Livre Statistiques',
    'Moniteur 4K', 'Formation SQL', 'Table Basse', 'Clavier Rétroéclairé',
    'Livre Deep Learning', 'Chaise Gaming', 'Microphone USB', 'Formation Big Data',
    'Meuble TV', 'Tablette Graphique', 'Livre Data Visualization', 'Bureau Debout',
    'Enceinte Bluetooth', 'Formation Cloud Computing', 'Chaise Design'
]

categories = {
    'Ordinateur Portable': 'Electronique',
    'Souris Sans Fil': 'Electronique',
    'Clavier Mécanique': 'Electronique',
    'Tablette': 'Electronique',
    'Chaise Bureau': 'Mobilier',
    'Bureau Ergonomique': 'Mobilier',
    'Écran 27 pouces': 'Electronique',
    'Livre Python': 'Education',
    'Casque Audio': 'Electronique',
    'Webcam HD': 'Electronique',
    'Formation Data Science': 'Education',
    'Étagère': 'Mobilier',
    'SSD 1TB': 'Electronique',
    'Livre Machine Learning': 'Education',
    'Lampe Bureau': 'Mobilier',
    'Smartphone': 'Electronique',
    'Formation Python': 'Education',
    'Fauteuil Bureau': 'Mobilier',
    'Disque Dur Externe': 'Electronique',
    'Livre Statistiques': 'Education',
    'Moniteur 4K': 'Electronique',
    'Formation SQL': 'Education',
    'Table Basse': 'Mobilier',
    'Clavier Rétroéclairé': 'Electronique',
    'Livre Deep Learning': 'Education',
    'Chaise Gaming': 'Mobilier',
    'Microphone USB': 'Electronique',
    'Formation Big Data': 'Education',
    'Meuble TV': 'Mobilier',
    'Tablette Graphique': 'Electronique',
    'Livre Data Visualization': 'Education',
    'Bureau Debout': 'Mobilier',
    'Enceinte Bluetooth': 'Electronique',
    'Formation Cloud Computing': 'Education',
    'Chaise Design': 'Mobilier'
}

prix_base = {
    'Electronique': (30, 900),
    'Mobilier': (40, 500),
    'Education': (30, 600)
}

# Génération
dates = []
produits_list = []
categories_list = []
quantites = []
prix_unitaires = []
client_ids = []

for i in range(nb_lignes):
    # Date aléatoire sur l'année 2024
    jours_offset = np.random.randint(0, 365)
    date = date_debut + timedelta(days=jours_offset)
    dates.append(date.strftime('%Y-%m-%d'))
    
    # Produit aléatoire
    produit = np.random.choice(produits)
    produits_list.append(produit)
    categorie = categories[produit]
    categories_list.append(categorie)
    
    # Quantité
    quantites.append(np.random.randint(1, 15))
    
    # Prix selon catégorie
    prix_min, prix_max = prix_base[categorie]
    prix = round(np.random.uniform(prix_min, prix_max), 2)
    prix_unitaires.append(prix)
    
    # Client ID
    client_ids.append(f'CL{str(np.random.randint(1, 25)).zfill(3)}')

# Création du DataFrame
df = pd.DataFrame({
    'date': dates,
    'produit': produits_list,
    'categorie': categories_list,
    'quantite': quantites,
    'prix_unitaire': prix_unitaires,
    'client_id': client_ids
})

# Tri par date
df = df.sort_values('date').reset_index(drop=True)

# Sauvegarde
df.to_csv('donnees/ventes.csv', index=False, encoding='utf-8')

print(f"✅ Fichier ventes.csv créé avec succès !")
print(f"   - {len(df)} lignes générées")
print(f"   - Période : {df['date'].min()} à {df['date'].max()}")
print(f"   - {df['produit'].nunique()} produits différents")
print(f"   - {df['client_id'].nunique()} clients différents")

