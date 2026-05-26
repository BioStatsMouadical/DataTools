"""
Script pour créer la base de données SQLite pour l'exercice 02
Exécutez ce script avant de commencer l'exercice
"""

import sqlite3
import os

# Créer le dossier donnees s'il n'existe pas
os.makedirs('donnees', exist_ok=True)

# Connexion à la base de données
conn = sqlite3.connect('donnees/boutique.db')
cursor = conn.cursor()

# Supprimer les tables si elles existent
cursor.execute("DROP TABLE IF EXISTS details_commandes")
cursor.execute("DROP TABLE IF EXISTS commandes")
cursor.execute("DROP TABLE IF EXISTS produits")
cursor.execute("DROP TABLE IF EXISTS clients")

# Créer la table clients
cursor.execute("""
CREATE TABLE clients (
    client_id TEXT PRIMARY KEY,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    telephone TEXT,
    ville TEXT,
    date_inscription DATE
)
""")

# Créer la table produits
cursor.execute("""
CREATE TABLE produits (
    produit_id TEXT PRIMARY KEY,
    nom TEXT NOT NULL,
    categorie TEXT NOT NULL,
    prix REAL NOT NULL,
    stock INTEGER DEFAULT 0,
    description TEXT
)
""")

# Créer la table commandes
cursor.execute("""
CREATE TABLE commandes (
    commande_id TEXT PRIMARY KEY,
    client_id TEXT NOT NULL,
    date_commande DATE NOT NULL,
    montant_total REAL NOT NULL,
    statut TEXT DEFAULT 'en_attente',
    FOREIGN KEY (client_id) REFERENCES clients(client_id)
)
""")

# Créer la table details_commandes
cursor.execute("""
CREATE TABLE details_commandes (
    detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
    commande_id TEXT NOT NULL,
    produit_id TEXT NOT NULL,
    quantite INTEGER NOT NULL,
    prix_unitaire REAL NOT NULL,
    FOREIGN KEY (commande_id) REFERENCES commandes(commande_id),
    FOREIGN KEY (produit_id) REFERENCES produits(produit_id)
)
""")

# Insérer des clients
clients = [
    ('CL001', 'Dupont', 'Jean', 'jean.dupont@email.com', '0612345678', 'Paris', '2023-01-15'),
    ('CL002', 'Martin', 'Marie', 'marie.martin@email.com', '0623456789', 'Lyon', '2023-02-20'),
    ('CL003', 'Bernard', 'Pierre', 'pierre.bernard@email.com', '0634567890', 'Marseille', '2023-03-10'),
    ('CL004', 'Dubois', 'Sophie', 'sophie.dubois@email.com', '0645678901', 'Toulouse', '2023-04-05'),
    ('CL005', 'Leroy', 'Thomas', 'thomas.leroy@email.com', '0656789012', 'Nice', '2023-05-12'),
    ('CL006', 'Moreau', 'Julie', 'julie.moreau@email.com', '0667890123', 'Nantes', '2023-06-18'),
    ('CL007', 'Petit', 'Lucas', 'lucas.petit@email.com', '0678901234', 'Strasbourg', '2023-07-22'),
    ('CL008', 'Robert', 'Emma', 'emma.robert@email.com', '0689012345', 'Bordeaux', '2023-08-30'),
    ('CL009', 'Richard', 'Hugo', 'hugo.richard@email.com', '0690123456', 'Lille', '2023-09-14'),
    ('CL010', 'Durand', 'Léa', 'lea.durand@email.com', '0601234567', 'Rennes', '2023-10-25'),
]

cursor.executemany("""
INSERT INTO clients (client_id, nom, prenom, email, telephone, ville, date_inscription)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", clients)

# Insérer des produits
produits = [
    ('PR001', 'Ordinateur Portable', 'Electronique', 899.99, 15, 'Laptop haute performance'),
    ('PR002', 'Souris Sans Fil', 'Electronique', 29.99, 50, 'Souris ergonomique'),
    ('PR003', 'Clavier Mécanique', 'Electronique', 79.99, 30, 'Clavier gaming'),
    ('PR004', 'Tablette', 'Electronique', 499.99, 20, 'Tablette 10 pouces'),
    ('PR005', 'Chaise Bureau', 'Mobilier', 199.99, 25, 'Chaise ergonomique'),
    ('PR006', 'Bureau Ergonomique', 'Mobilier', 349.99, 10, 'Bureau réglable en hauteur'),
    ('PR007', 'Écran 27 pouces', 'Electronique', 299.99, 18, 'Écran 4K'),
    ('PR008', 'Livre Python', 'Education', 39.99, 100, 'Apprendre Python'),
    ('PR009', 'Casque Audio', 'Electronique', 149.99, 40, 'Casque sans fil'),
    ('PR010', 'Webcam HD', 'Electronique', 89.99, 35, 'Webcam 1080p'),
    ('PR011', 'Formation Data Science', 'Education', 499.99, 0, 'Formation en ligne'),
    ('PR012', 'Étagère', 'Mobilier', 79.99, 45, 'Étagère 5 niveaux'),
    ('PR013', 'SSD 1TB', 'Electronique', 129.99, 60, 'SSD NVMe'),
    ('PR014', 'Livre Machine Learning', 'Education', 49.99, 80, 'Introduction au ML'),
    ('PR015', 'Lampe Bureau', 'Mobilier', 39.99, 70, 'Lampe LED'),
]

cursor.executemany("""
INSERT INTO produits (produit_id, nom, categorie, prix, stock, description)
VALUES (?, ?, ?, ?, ?, ?)
""", produits)

# Insérer des commandes
commandes = [
    ('CMD001', 'CL001', '2024-01-15', 1799.98, 'livree'),
    ('CMD002', 'CL002', '2024-01-20', 149.95, 'livree'),
    ('CMD003', 'CL003', '2024-01-22', 239.97, 'livree'),
    ('CMD004', 'CL001', '2024-02-10', 499.99, 'livree'),
    ('CMD005', 'CL004', '2024-02-15', 399.98, 'livree'),
    ('CMD006', 'CL005', '2024-02-20', 349.99, 'livree'),
    ('CMD007', 'CL002', '2024-03-05', 899.97, 'livree'),
    ('CMD008', 'CL006', '2024-03-12', 399.90, 'livree'),
    ('CMD009', 'CL003', '2024-03-18', 599.96, 'livree'),
    ('CMD010', 'CL007', '2024-04-02', 539.94, 'livree'),
    ('CMD011', 'CL001', '2024-04-10', 999.98, 'livree'),
    ('CMD012', 'CL008', '2024-04-15', 399.95, 'livree'),
    ('CMD013', 'CL002', '2024-05-08', 1039.92, 'livree'),
    ('CMD014', 'CL009', '2024-05-12', 349.93, 'livree'),
    ('CMD015', 'CL010', '2024-05-20', 479.88, 'livree'),
    ('CMD016', 'CL001', '2024-06-05', 699.99, 'en_attente'),
    ('CMD017', 'CL011', '2024-06-15', 899.97, 'livree'),
    ('CMD018', 'CL005', '2024-06-22', 899.98, 'livree'),
]

cursor.executemany("""
INSERT INTO commandes (commande_id, client_id, date_commande, montant_total, statut)
VALUES (?, ?, ?, ?, ?)
""", commandes)

# Insérer des détails de commandes
details = [
    ('CMD001', 'PR001', 2, 899.99),
    ('CMD002', 'PR002', 5, 29.99),
    ('CMD003', 'PR003', 3, 79.99),
    ('CMD004', 'PR004', 1, 499.99),
    ('CMD005', 'PR005', 2, 199.99),
    ('CMD006', 'PR006', 1, 349.99),
    ('CMD007', 'PR007', 3, 299.99),
    ('CMD008', 'PR008', 10, 39.99),
    ('CMD009', 'PR009', 4, 149.99),
    ('CMD010', 'PR010', 6, 89.99),
    ('CMD011', 'PR011', 2, 499.99),
    ('CMD012', 'PR012', 5, 79.99),
    ('CMD013', 'PR013', 8, 129.99),
    ('CMD014', 'PR014', 7, 49.99),
    ('CMD015', 'PR015', 12, 39.99),
    ('CMD016', 'PR001', 1, 699.99),
    ('CMD017', 'PR008', 3, 39.99),
    ('CMD017', 'PR014', 2, 49.99),
    ('CMD017', 'PR011', 1, 499.99),
    ('CMD018', 'PR005', 2, 199.99),
    ('CMD018', 'PR006', 1, 349.99),
]

cursor.executemany("""
INSERT INTO details_commandes (commande_id, produit_id, quantite, prix_unitaire)
VALUES (?, ?, ?, ?)
""", details)

# Valider les changements
conn.commit()

# Afficher un résumé
print("Base de données créée avec succès!")
print(f"- {len(clients)} clients")
print(f"- {len(produits)} produits")
print(f"- {len(commandes)} commandes")
print(f"- {len(details)} détails de commandes")

# Fermer la connexion
conn.close()

