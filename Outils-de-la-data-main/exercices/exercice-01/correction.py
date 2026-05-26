"""
CORRECTION DE L'EXERCICE 01 - APACHE SUPERSET
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
print("CORRECTION DE L'EXERCICE 01 - APACHE SUPERSET")
print("="*60 + "\n")

print("""
GUIDE COMPLET APACHE SUPERSET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. CONFIGURATION DE LA BASE DE DONNÉES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Dans Superset :
- Data > Databases > + Database
- Database Name : "Ventes E-commerce"
- SQLAlchemy URI : sqlite:///donnees/ventes.db
- Test Connection > Save

2. CRÉATION DU DATASET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Data > Datasets > + Dataset
- Sélectionner la base et la table "ventes"
- Nom : "Ventes"
- Explorer les colonnes

3. VISUALISATIONS À CRÉER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

VISUALISATION 1 : Bar Chart - CA par mois
────────────────────────────────────────────────────────────────────────────
- Type : Bar Chart
- Time Column : date (groupé par mois)
- Metric : SUM(montant_total)
- Titre : "Chiffre d'affaires par mois"

VISUALISATION 2 : Pie Chart - Répartition par catégorie
────────────────────────────────────────────────────────────────────────────
- Type : Pie Chart
- Dimension : categorie
- Metric : SUM(montant_total)
- Titre : "Répartition du CA par catégorie"

VISUALISATION 3 : Line Chart - Évolution temporelle
────────────────────────────────────────────────────────────────────────────
- Type : Line Chart
- Time Column : date
- Metric : SUM(montant_total)
- Titre : "Évolution des ventes"

VISUALISATION 4 : Table - Top 10 produits
────────────────────────────────────────────────────────────────────────────
- Type : Table View
- Columns : produit, SUM(quantite), SUM(montant_total)
- Order by : SUM(montant_total) DESC
- Row limit : 10

VISUALISATION 5 : Stacked Bar - Ventes par catégorie et mois
────────────────────────────────────────────────────────────────────────────
- Type : Stacked Bar Chart
- Time Column : date (par mois)
- Metric : SUM(montant_total)
- Stack : categorie

4. CRÉATION DU DASHBOARD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Dashboards > + Dashboard
- Nom : "Analyse des Ventes"
- Ajouter vos visualisations
- Organiser par lignes :
  * Ligne 1 : Vue d'ensemble (métriques clés)
  * Ligne 2 : Analyses temporelles
  * Ligne 3 : Analyses par catégorie
  * Ligne 4 : Détails produits

5. FILTRES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Ajouter un filtre par date
- Ajouter un filtre par catégorie
- Tester l'interactivité

6. SQL LAB (BONUS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Requêtes SQL utiles :

-- CA total par mois
SELECT 
  strftime('%Y-%m', date) as mois,
  SUM(montant_total) as ca_mois
FROM ventes
GROUP BY mois
ORDER BY mois;

-- Top produits
SELECT 
  produit,
  SUM(quantite) as quantite_totale,
  SUM(montant_total) as ca_total
FROM ventes
GROUP BY produit
ORDER BY ca_total DESC
LIMIT 10;

7. EXPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Dashboard > Settings > Export Dashboard
- Sauvegarder le JSON
- Prendre des captures d'écran

BONNES PRATIQUES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Utiliser des noms clairs pour les visualisations
✅ Organiser le dashboard de manière logique
✅ Utiliser des couleurs cohérentes
✅ Ajouter des descriptions
✅ Tester les filtres
✅ Documenter les métriques personnalisées
""")

print("\n" + "="*60)
print("FIN DE LA CORRECTION")
print("="*60)
print("\nNote : Adaptez ces instructions à votre configuration.\n")
