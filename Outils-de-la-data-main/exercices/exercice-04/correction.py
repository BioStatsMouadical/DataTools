"""
CORRECTION DE L'EXERCICE 04 - APACHE SPARK
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
print("CORRECTION DE L'EXERCICE 04 - APACHE SPARK")
print("="*60 + "\n")

print("""
EXEMPLE DE CODE SPARK COMPLET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

# 1. CONFIGURATION SPARK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

spark = SparkSession.builder \\
    .appName("AnalyseTransactions") \\
    .master("local[4]") \\
    .config("spark.sql.adaptive.enabled", "true") \\
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \\
    .getOrCreate()

# 2. CHARGEMENT DES DONNÉES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

df = spark.read.csv(
    "donnees/transactions_large.csv",
    header=True,
    inferSchema=True
)

# Exploration
df.printSchema()
df.show(5)
print(f"Nombre de lignes : {df.count()}")

# 3. TRANSFORMATIONS DE BASE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Filtrage
df_filtered = df.filter(col("montant_total") > 100)

# Sélection et projection
df_selected = df.select(
    "transaction_id",
    "date",
    "client_id",
    "produit",
    "categorie",
    "montant_total"
)

# Nouvelles colonnes calculées
df_with_calculated = df.withColumn(
    "annee_mois",
    date_format(col("date"), "yyyy-MM")
)

# 4. AGRÉGATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# CA total par client
ca_par_client = df.groupBy("client_id") \\
    .agg(sum("montant_total").alias("ca_total")) \\
    .orderBy(desc("ca_total"))

# Produits les plus vendus
produits_populaires = df.groupBy("produit") \\
    .agg(
        sum("quantite").alias("quantite_totale"),
        sum("montant_total").alias("ca_total")
    ) \\
    .orderBy(desc("quantite_totale"))

# Statistiques par catégorie
stats_categorie = df.groupBy("categorie") \\
    .agg(
        count("*").alias("nb_transactions"),
        sum("montant_total").alias("ca_total"),
        avg("montant_total").alias("panier_moyen"),
        max("montant_total").alias("transaction_max")
    )

# 5. FONCTIONS DE FENÊTRE (WINDOW FUNCTIONS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Définir la fenêtre
window_spec = Window.partitionBy("client_id").orderBy("date")

# Montant cumulé par client
df_with_cumsum = df.withColumn(
    "montant_cumule",
    sum("montant_total").over(window_spec)
)

# Top 3 produits par catégorie
window_rank = Window.partitionBy("categorie").orderBy(desc("montant_total"))
df_with_rank = df.withColumn("rank", rank().over(window_rank))
top3_par_categorie = df_with_rank.filter(col("rank") <= 3)

# 6. OPTIMISATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Repartitionnement
df_repartitioned = df.repartition(4, "categorie")

# Caching pour réutilisation
df.cache()
# ou
df.persist(StorageLevel.MEMORY_AND_DISK)

# Broadcast join pour petites tables
from pyspark.sql.functions import broadcast
small_df = spark.createDataFrame([...])
df_joined = df.join(broadcast(small_df), "key")

# 7. ANALYSES AVANCÉES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# CA par mois
ca_par_mois = df.groupBy(
    date_format(col("date"), "yyyy-MM").alias("mois")
).agg(
    sum("montant_total").alias("ca_mois")
).orderBy("mois")

# Détection d'anomalies (transactions > 3 écarts-types)
from pyspark.sql.functions import stddev, mean
stats = df.agg(
    mean("montant_total").alias("moyenne"),
    stddev("montant_total").alias("ecart_type")
).collect()[0]

seuil = stats.moyenne + 3 * stats.ecart_type
anomalies = df.filter(col("montant_total") > seuil)

# 8. EXPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Export CSV
ca_par_client.coalesce(1).write.csv(
    "output/ca_par_client",
    header=True,
    mode="overwrite"
)

# Export Parquet (recommandé)
produits_populaires.write.parquet(
    "output/produits_populaires",
    mode="overwrite"
)

# Export JSON
stats_categorie.coalesce(1).write.json(
    "output/stats_categorie",
    mode="overwrite"
)

# 9. REQUÊTES SQL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Créer une vue temporaire
df.createOrReplaceTempView("transactions")

# Requête SQL
result = spark.sql("""
    SELECT 
        categorie,
        COUNT(*) as nb_transactions,
        SUM(montant_total) as ca_total,
        AVG(montant_total) as panier_moyen
    FROM transactions
    GROUP BY categorie
    ORDER BY ca_total DESC
""")

# 10. NETTOYAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Libérer le cache
df.unpersist()

# Arrêter Spark
spark.stop()

POINTS CLÉS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Utiliser les DataFrames plutôt que les RDD
✅ Éviter les collect() sur gros datasets
✅ Utiliser le cache judicieusement
✅ Optimiser les partitions
✅ Utiliser les broadcast joins pour petites tables
✅ Préférer Parquet à CSV pour le stockage
✅ Utiliser spark.sql() pour requêtes complexes

BONNES PRATIQUES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Tester avec de petits datasets d'abord
- Monitorer l'UI Spark (http://localhost:4040)
- Utiliser explain() pour voir le plan d'exécution
- Éviter les opérations coûteuses (shuffles)
- Penser à la persistance (cache, checkpoint)
""")

print("\n" + "="*60)
print("FIN DE LA CORRECTION")
print("="*60)
print("\nNote : Adaptez ce code à votre dataset et vos besoins spécifiques.\n")

