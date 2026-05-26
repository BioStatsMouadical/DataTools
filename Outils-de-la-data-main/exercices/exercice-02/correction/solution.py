"""
CORRECTION DE L'EXERCICE 02 - METABASE
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
print("CORRECTION DE L'EXERCICE 02 - METABASE")
print("="*60 + "\n")

print("""
GUIDE COMPLET METABASE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. CONFIGURATION DE LA BASE DE DONNÉES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Settings > Admin > Databases
- Add database > SQLite
- Nom : "Boutique E-commerce"
- Fichier : Chemin vers donnees/boutique.db
- Save

2. QUESTIONS À CRÉER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

QUESTION 1 : Liste des clients
────────────────────────────────────────────────────────────────────────────
- Simple question > Table : clients
- Colonnes : nom, prenom, email, ville
- Visualisation : Table
- Sauvegarder comme "Liste des clients"

QUESTION 2 : Produits premium (> 100€)
────────────────────────────────────────────────────────────────────────────
- Simple question > Table : produits
- Filtre : prix > 100
- Trier : prix DESC
- Visualisation : Table
- Sauvegarder comme "Produits premium"

QUESTION 3 : CA total
────────────────────────────────────────────────────────────────────────────
- Simple question > Table : commandes
- Agrégation : SUM(montant_total)
- Visualisation : Number
- Sauvegarder comme "CA Total"

QUESTION 4 : Commandes avec noms clients
────────────────────────────────────────────────────────────────────────────
- Custom question > SQL Editor
Query :
  SELECT 
    co.commande_id,
    co.date_commande,
    co.montant_total,
    c.nom || ' ' || c.prenom as client_nom
  FROM commandes co
  JOIN clients c ON co.client_id = c.client_id
  ORDER BY co.date_commande DESC
- Visualisation : Table
- Sauvegarder comme "Commandes détaillées"

QUESTION 5 : Top 5 clients par CA
────────────────────────────────────────────────────────────────────────────
- Custom question > SQL Editor
Query :
  SELECT 
    c.nom,
    c.prenom,
    SUM(co.montant_total) as ca_total
  FROM clients c
  JOIN commandes co ON c.client_id = co.client_id
  GROUP BY c.client_id, c.nom, c.prenom
  ORDER BY ca_total DESC
  LIMIT 5
- Visualisation : Bar Chart
- Sauvegarder comme "Top 5 clients"

QUESTION 6 : Panier moyen par catégorie
────────────────────────────────────────────────────────────────────────────
- Custom question > SQL Editor
Query :
  SELECT 
    p.categorie,
    AVG(dc.quantite * dc.prix_unitaire) as panier_moyen
  FROM details_commandes dc
  JOIN produits p ON dc.produit_id = p.produit_id
  GROUP BY p.categorie
  ORDER BY panier_moyen DESC
- Visualisation : Bar Chart
- Sauvegarder comme "Panier moyen par catégorie"

3. CRÉATION DU DASHBOARD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Dashboards > New Dashboard
- Nom : "Analyse Boutique"
- Organiser par sections :
  * Section 1 : Vue d'ensemble (CA Total, métriques clés)
  * Section 2 : Analyse clients (Top 5, Liste clients)
  * Section 3 : Analyse produits (Produits premium, Panier moyen)
  * Section 4 : Analyse commandes (Commandes détaillées)

4. FILTRES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Ajouter filtre par date (sur les commandes)
- Ajouter filtre par catégorie (sur les produits)
- Ajouter filtre par client (optionnel)
- Tester l'interactivité en temps réel

5. MODÈLES DE DONNÉES (BONUS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Settings > Admin > Table Metadata
- Définir les relations :
  * clients.client_id -> commandes.client_id (Foreign Key)
  * produits.produit_id -> details_commandes.produit_id
  * commandes.commande_id -> details_commandes.commande_id
- Cela simplifie la création de questions avec jointures

6. ALERTES (BONUS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Créer une question pour le CA quotidien
- Ajouter une alerte si CA < seuil (ex: 1000€)
- Configurer les notifications (email, Slack)

BONNES PRATIQUES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Utiliser l'éditeur visuel (Simple question) pour commencer
- Passer à SQL Editor pour les requêtes complexes avec jointures
- Tester chaque question avant de l'ajouter au dashboard
- Organiser les dashboards par thème métier
- Utiliser les modèles de données pour simplifier les requêtes
- Documenter vos questions avec des descriptions claires
- Nommer clairement vos questions et dashboards
""")

print("\n" + "="*60)
print("FIN DE LA CORRECTION")
print("="*60)
print("\nNote : Adaptez ces instructions à votre configuration.\n")

