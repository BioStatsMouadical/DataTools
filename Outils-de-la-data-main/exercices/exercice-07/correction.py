"""
CORRECTION DE L'EXERCICE 07 - DBT
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
print("CORRECTION DE L'EXERCICE 07 - DBT")
print("="*60 + "\n")

print("""
GUIDE COMPLET DBT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. STRUCTURE DES MODÈLES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

models/staging/stg_customers.sql
────────────────────────────────────────────────────────────────────────────
SELECT 
  client_id,
  UPPER(TRIM(nom)) as nom,
  INITCAP(TRIM(prenom)) as prenom,
  LOWER(TRIM(email)) as email,
  telephone,
  ville,
  date_inscription
FROM {{ source('raw', 'clients') }}

models/staging/stg_orders.sql
────────────────────────────────────────────────────────────────────────────
SELECT 
  commande_id,
  client_id,
  date_commande,
  montant_total,
  statut
FROM {{ source('raw', 'commandes') }}
WHERE date_commande >= '2024-01-01'

models/intermediate/int_order_items.sql
────────────────────────────────────────────────────────────────────────────
SELECT 
  co.commande_id,
  co.client_id,
  co.date_commande,
  dc.produit_id,
  p.nom as produit_nom,
  p.categorie,
  dc.quantite,
  dc.prix_unitaire,
  (dc.quantite * dc.prix_unitaire) as montant_ligne
FROM {{ ref('stg_orders') }} co
JOIN {{ source('raw', 'details_commandes') }} dc 
  ON co.commande_id = dc.commande_id
JOIN {{ ref('stg_products') }} p 
  ON dc.produit_id = p.produit_id

models/marts/dim_customers.sql
────────────────────────────────────────────────────────────────────────────
SELECT 
  c.client_id,
  c.nom,
  c.prenom,
  c.email,
  c.ville,
  COUNT(DISTINCT co.commande_id) as nb_commandes,
  SUM(co.montant_total) as ca_total,
  AVG(co.montant_total) as panier_moyen
FROM {{ ref('stg_customers') }} c
LEFT JOIN {{ ref('stg_orders') }} co 
  ON c.client_id = co.client_id
GROUP BY c.client_id, c.nom, c.prenom, c.email, c.ville

models/marts/fct_orders.sql
────────────────────────────────────────────────────────────────────────────
SELECT 
  oi.commande_id,
  oi.client_id,
  oi.date_commande,
  oi.produit_id,
  oi.categorie,
  oi.quantite,
  oi.prix_unitaire,
  oi.montant_ligne
FROM {{ ref('int_order_items') }} oi

2. MACROS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

macros/format_date.sql
────────────────────────────────────────────────────────────────────────────
{% macro format_date(date_column) %}
  DATE({{ date_column }})
{% endmacro %}

macros/calculate_growth.sql
────────────────────────────────────────────────────────────────────────────
{% macro calculate_growth(current, previous) %}
  CASE 
    WHEN {{ previous }} = 0 THEN NULL
    ELSE (({{ current }} - {{ previous }}) / {{ previous }}) * 100
  END
{% endmacro %}

3. TESTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

models/staging/schema.yml
────────────────────────────────────────────────────────────────────────────
version: 2

models:
  - name: stg_customers
    description: "Table staging des clients"
    columns:
      - name: client_id
        description: "Identifiant unique du client"
        tests:
          - unique
          - not_null
      - name: email
        tests:
          - unique
          - not_null

  - name: stg_orders
    description: "Table staging des commandes"
    columns:
      - name: commande_id
        tests:
          - unique
          - not_null
      - name: client_id
        tests:
          - relationships:
              to: ref('stg_customers')
              field: client_id

4. SOURCES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

models/sources.yml
────────────────────────────────────────────────────────────────────────────
version: 2

sources:
  - name: raw
    description: "Tables sources brutes"
    tables:
      - name: clients
      - name: produits
      - name: commandes
      - name: details_commandes

5. COMMANDES DBT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Compiler les modèles (vérifier la syntaxe)
dbt compile

# Exécuter les modèles
dbt run

# Exécuter les tests
dbt test

# Générer la documentation
dbt docs generate
dbt docs serve

# Exécuter un modèle spécifique
dbt run --select stg_customers

# Exécuter les modèles d'une couche
dbt run --select staging.*

BONNES PRATIQUES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Organiser en couches (staging, intermediate, marts)
✅ Utiliser ref() pour les dépendances
✅ Utiliser source() pour les tables sources
✅ Documenter chaque modèle
✅ Tester régulièrement
✅ Utiliser les macros pour la réutilisabilité
✅ Suivre les conventions de nommage
""")

print("\n" + "="*60)
print("FIN DE LA CORRECTION")
print("="*60)
print("\nNote : Adaptez ces exemples à votre structure de données.\n")

