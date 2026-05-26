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
        print("❌ Mot de passe incorrect. Accès refusé.")
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
- Table : clients
- Colonnes : nom, prenom, email, ville
- Visualisation : Table

QUESTION 2 : Produits > 100€
────────────────────────────────────────────────────────────────────────────
- Table : produits
- Filtre : prix > 100
- Trier : prix DESC
- Visualisation : Table

QUESTION 3 : CA total
────────────────────────────────────────────────────────────────────────────
- Table : commandes
- Agrégation : SUM(montant_total)
- Visualisation : Number

QUESTION 4 : Commandes avec noms clients
────────────────────────────────────────────────────────────────────────────
- Tables : commandes + clients
- Jointure : commandes.client_id = clients.client_id
- Colonnes : commande_id, date_commande, montant_total, nom, prenom
- Visualisation : Table

QUESTION 5 : Top 5 clients par CA (SQL)
────────────────────────────────────────────────────────────────────────────
Mode : SQL
Query :
  SELECT 
    c.nom, 
    c.prenom, 
    SUM(co.montant_total) as ca_total
  FROM clients c
  JOIN commandes co ON c.client_id = co.client_id
  GROUP BY c.client_id
  ORDER BY ca_total DESC
  LIMIT 5
Visualisation : Bar Chart

QUESTION 6 : Panier moyen par catégorie
────────────────────────────────────────────────────────────────────────────
- Tables : produits + details_commandes + commandes
- Jointures multiples
- Agrégation : AVG(quantite * prix_unitaire)
- Grouper par : categorie
- Visualisation : Bar Chart

3. CRÉATION DU DASHBOARD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Dashboards > New Dashboard
- Nom : "Analyse Boutique"
- Organiser par sections :
  * Section 1 : Vue d'ensemble (métriques)
  * Section 2 : Analyse clients
  * Section 3 : Analyse produits
  * Section 4 : Analyse commandes

4. FILTRES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Ajouter filtre par date
- Ajouter filtre par catégorie
- Ajouter filtre par client
- Tester l'interactivité

5. MODÈLES DE DONNÉES (BONUS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Settings > Admin > Table Metadata
- Définir les relations :
  * clients.client_id -> commandes.client_id
  * produits.produit_id -> details_commandes.produit_id
  * commandes.commande_id -> details_commandes.commande_id

6. ALERTES (BONUS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Créer une question pour le CA
- Ajouter une alerte si CA < seuil
- Configurer les notifications

BONNES PRATIQUES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Utiliser l'éditeur visuel pour commencer
✅ Passer à SQL pour les requêtes complexes
✅ Tester chaque question avant d'ajouter au dashboard
✅ Organiser les dashboards par thème
✅ Utiliser les modèles de données
✅ Documenter vos questions
""")

print("\n" + "="*60)
print("FIN DE LA CORRECTION")
print("="*60)
print("\nNote : Adaptez ces instructions à votre configuration.\n")
