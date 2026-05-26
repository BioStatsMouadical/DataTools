"""
Script pour générer des logs simulés pour l'exercice 03 (ELK Stack)
"""

import json
import random
from datetime import datetime, timedelta
import os

# Créer le dossier donnees/logs
os.makedirs('donnees/logs', exist_ok=True)

# Paramètres
nb_logs = 10000
date_debut = datetime.now() - timedelta(days=7)

# Endpoints simulés
endpoints = [
    '/api/users', '/api/products', '/api/orders', '/api/login',
    '/api/logout', '/api/cart', '/api/checkout', '/api/search',
    '/api/reviews', '/api/categories', '/api/payment', '/api/shipping'
]

# Status codes
status_codes = [200, 200, 200, 200, 200, 201, 301, 400, 401, 403, 404, 500, 503]
weights = [40, 40, 40, 40, 40, 10, 5, 3, 2, 2, 3, 1, 1]

# Méthodes HTTP
methods = ['GET', 'GET', 'GET', 'POST', 'POST', 'PUT', 'DELETE']

print("Génération des logs...")

logs = []
for i in range(nb_logs):
    # Date aléatoire sur la dernière semaine
    jours_offset = random.uniform(0, 7)
    heures_offset = random.uniform(0, 24)
    timestamp = date_debut + timedelta(days=jours_offset, hours=heures_offset)
    
    # Données du log
    endpoint = random.choice(endpoints)
    method = random.choice(methods)
    status_code = random.choices(status_codes, weights=weights)[0]
    response_time = random.uniform(0.1, 2.0) if status_code < 400 else random.uniform(2.0, 5.0)
    
    # IP simulée
    ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
    
    # User agent simulé
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
        'Mozilla/5.0 (X11; Linux x86_64)',
    ]
    user_agent = random.choice(user_agents)
    
    log_entry = {
        "timestamp": timestamp.isoformat(),
        "level": "INFO" if status_code < 400 else "ERROR",
        "method": method,
        "endpoint": endpoint,
        "status_code": status_code,
        "response_time": round(response_time, 3),
        "ip": ip,
        "user_agent": user_agent,
        "bytes_sent": random.randint(100, 10000)
    }
    
    logs.append(log_entry)
    
    if (i + 1) % 1000 == 0:
        print(f"  Généré {i + 1}/{nb_logs} logs...")

# Écrire dans des fichiers (par jour pour simuler des logs réels)
logs_par_jour = {}
for log in logs:
    date = datetime.fromisoformat(log['timestamp']).date()
    if date not in logs_par_jour:
        logs_par_jour[date] = []
    logs_par_jour[date].append(log)

# Sauvegarder
for date, day_logs in logs_par_jour.items():
    filename = f"donnees/logs/app-{date.strftime('%Y-%m-%d')}.log"
    with open(filename, 'w') as f:
        for log in day_logs:
            f.write(json.dumps(log) + '\n')

print(f"\n✅ {nb_logs} logs générés dans donnees/logs/")
print(f"   - {len(logs_par_jour)} fichiers créés (un par jour)")
print(f"   - Période : {min(logs_par_jour.keys())} à {max(logs_par_jour.keys())}")

