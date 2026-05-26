"""
CORRECTION DE L'EXERCICE 03 - ELK STACK (Elasticsearch, Logstash, Kibana)
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
print("CORRECTION DE L'EXERCICE 03 - ELK STACK")
print("="*60 + "\n")

print("""
GUIDE COMPLET ELK STACK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. CONFIGURATION DOCKER COMPOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Créez docker-compose.yml :

version: '3.8'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.11.0
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ports:
      - "9200:9200"
    volumes:
      - es_data:/usr/share/elasticsearch/data

  logstash:
    image: docker.elastic.co/logstash/logstash:8.11.0
    volumes:
      - ./logstash/config:/usr/share/logstash/config
      - ./logstash/pipeline:/usr/share/logstash/pipeline
      - ./logs:/usr/share/logstash/logs
    depends_on:
      - elasticsearch

  kibana:
    image: docker.elastic.co/kibana/kibana:8.11.0
    ports:
      - "5601:5601"
    environment:
      - ELASTICSEARCH_HOSTS=http://elasticsearch:9200
    depends_on:
      - elasticsearch

volumes:
  es_data:

2. CONFIGURATION LOGSTASH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

logstash/pipeline/logstash.conf :

input {
  file {
    path => "/usr/share/logstash/logs/app.log"
    start_position => "beginning"
    codec => json
    sincedb_path => "/dev/null"
  }
}

filter {
  date {
    match => [ "timestamp", "ISO8601" ]
  }
  
  if [level] == "ERROR" {
    mutate {
      add_tag => [ "error" ]
    }
  }
  
  mutate {
    convert => {
      "response_time" => "integer"
      "status_code" => "integer"
    }
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "app-logs-%{+YYYY.MM.dd}"
  }
  stdout { codec => rubydebug }
}

3. GÉNÉRATION DE LOGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Utilisez le script generer_logs.py fourni pour générer des logs réalistes.

4. CONFIGURATION KIBANA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

a) Créer un index pattern :
- Management > Stack Management > Index Patterns
- Pattern : app-logs-*
- Time field : @timestamp

b) Visualisations à créer :

VISUALISATION 1 : Timeline des logs
- Type : Line Chart
- X-axis : @timestamp (par heure)
- Y-axis : Count
- Titre : "Volume de logs par heure"

VISUALISATION 2 : Répartition par niveau
- Type : Pie Chart
- Slice by : level
- Titre : "Répartition des logs par niveau"

VISUALISATION 3 : Top endpoints
- Type : Data Table
- Group by : message.keyword (avec regex pour extraire l'endpoint)
- Titre : "Top 10 endpoints"

VISUALISATION 4 : Erreurs par heure
- Type : Bar Chart
- X-axis : @timestamp (par heure)
- Y-axis : Count
- Filter : level:ERROR
- Titre : "Erreurs par heure"

VISUALISATION 5 : Temps de réponse moyen
- Type : Line Chart
- X-axis : @timestamp
- Y-axis : Average of response_time
- Titre : "Temps de réponse moyen"

VISUALISATION 6 : Codes de statut HTTP
- Type : Bar Chart
- X-axis : status_code
- Y-axis : Count
- Titre : "Répartition des codes HTTP"

5. DASHBOARD KIBANA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Créer un dashboard "Monitoring Application"
- Organiser les visualisations :
  * Ligne 1 : Vue d'ensemble (timeline, répartition niveau)
  * Ligne 2 : Analyses de performance (temps de réponse, top endpoints)
  * Ligne 3 : Analyses d'erreurs (erreurs par heure, codes HTTP)
- Ajouter des filtres temporels
- Configurer l'auto-refresh

6. REQUÊTES KQL UTILES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Logs d'erreur des dernières 24h
level:ERROR and @timestamp >= now()-24h

# Endpoints avec temps de réponse > 500ms
response_time > 500

# Codes HTTP 5xx
status_code >= 500

# Combinaison
level:ERROR and status_code >= 500 and response_time > 1000

7. ALERTES (BONUS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Stack Management > Watcher
- Créer une alerte si :
  * Nombre d'erreurs > seuil sur 5 minutes
  * Temps de réponse moyen > seuil
  * Code 500 détecté

BONNES PRATIQUES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Utiliser des index patterns avec dates pour la rotation
- Configurer la rétention des données (ILM - Index Lifecycle Management)
- Créer des visualisations réutilisables
- Documenter vos dashboards
- Tester les filtres et requêtes KQL
- Monitorer l'espace disque d'Elasticsearch
""")

print("\n" + "="*60)
print("FIN DE LA CORRECTION")
print("="*60)
print("\nNote : Adaptez ces instructions à votre configuration.\n")

