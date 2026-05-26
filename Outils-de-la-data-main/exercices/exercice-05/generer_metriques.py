"""
Script pour générer des métriques de monitoring pour l'exercice 05 (Grafana)
Simule des métriques système (CPU, mémoire, disque, réseau)
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Créer le dossier donnees s'il n'existe pas
os.makedirs('donnees', exist_ok=True)

# Paramètres
np.random.seed(42)
nb_serveurs = 10
nb_jours = 30
points_par_jour = 288  # Une mesure toutes les 5 minutes (24h * 60min / 5min)
nb_points = nb_serveurs * nb_jours * points_par_jour

date_debut = datetime.now() - timedelta(days=nb_jours)

print("Génération des métriques de monitoring...")
print(f"  - {nb_serveurs} serveurs")
print(f"  - {nb_jours} jours de données")
print(f"  - {points_par_jour} points par jour (toutes les 5 minutes)")

# Noms des serveurs
serveurs = [f'serveur-{i+1:02d}' for i in range(nb_serveurs)]

# Génération des données
metriques = []
intervalle = timedelta(minutes=5)

for i, serveur in enumerate(serveurs):
    print(f"  Génération pour {serveur}...")
    
    # Caractéristiques du serveur (pour variabilité)
    cpu_base = np.random.uniform(20, 40)
    mem_base = np.random.uniform(30, 50)
    disk_base = np.random.uniform(40, 60)
    
    timestamp = date_debut
    
    for jour in range(nb_jours):
        for point in range(points_par_jour):
            # CPU : variation avec pics aléatoires
            cpu = cpu_base + np.random.normal(0, 10)
            if np.random.random() < 0.05:  # 5% de chance de pic
                cpu += np.random.uniform(20, 40)
            cpu = max(0, min(100, cpu))
            
            # Mémoire : tendance avec variations
            mem = mem_base + np.random.normal(0, 8)
            mem = max(0, min(100, mem))
            
            # Disque : augmentation lente
            disk = disk_base + (jour * 0.5) + np.random.normal(0, 3)
            disk = max(0, min(100, disk))
            
            # Réseau : trafic variable
            network_in = np.random.exponential(100)  # MB/s
            network_out = np.random.exponential(50)
            
            # Requêtes par seconde
            rps = np.random.poisson(100)
            if np.random.random() < 0.1:  # Pic de trafic
                rps *= np.random.uniform(2, 5)
            
            # Latence (ms)
            latency = np.random.exponential(50)
            if rps > 200:  # Latence plus élevée sous charge
                latency *= 1.5
            
            metriques.append({
                'timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                'serveur': serveur,
                'cpu_percent': round(cpu, 2),
                'memory_percent': round(mem, 2),
                'disk_percent': round(disk, 2),
                'network_in_mbps': round(network_in, 2),
                'network_out_mbps': round(network_out, 2),
                'requests_per_second': int(rps),
                'latency_ms': round(latency, 2),
                'status': 'healthy' if cpu < 80 and mem < 85 else 'warning'
            })
            
            timestamp += intervalle

# Création du DataFrame
df = pd.DataFrame(metriques)

# Tri par timestamp et serveur
df = df.sort_values(['timestamp', 'serveur']).reset_index(drop=True)

# Sauvegarde
print("Sauvegarde du fichier...")
df.to_csv('donnees/metriques.csv', index=False, encoding='utf-8')

print(f"\n✅ Fichier metriques.csv créé avec succès !")
print(f"   - {len(df):,} points de données")
print(f"   - Période : {df['timestamp'].min()} à {df['timestamp'].max()}")
print(f"   - {df['serveur'].nunique()} serveurs")
print(f"   - Taille du fichier : {os.path.getsize('donnees/metriques.csv') / (1024*1024):.2f} MB")
print(f"\n📊 Statistiques :")
print(f"   - CPU moyen : {df['cpu_percent'].mean():.2f}%")
print(f"   - Mémoire moyenne : {df['memory_percent'].mean():.2f}%")
print(f"   - Disque moyen : {df['disk_percent'].mean():.2f}%")

