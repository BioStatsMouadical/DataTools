"""
CORRECTION DE L'EXERCICE 06 - APACHE AIRFLOW
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
print("CORRECTION DE L'EXERCICE 06 - APACHE AIRFLOW")
print("="*60 + "\n")

print("""
EXEMPLES DE DAGs AIRFLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. DAG SIMPLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd

default_args = {
    'owner': 'data_team',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def generate_data():
    import random
    data = {
        'id': range(100),
        'value': [random.randint(1, 100) for _ in range(100)]
    }
    df = pd.DataFrame(data)
    df.to_csv('/tmp/data.csv', index=False)
    print("Données générées")

def calculate_stats():
    df = pd.read_csv('/tmp/data.csv')
    stats = {
        'mean': df['value'].mean(),
        'max': df['value'].max(),
        'min': df['value'].min()
    }
    import json
    with open('/tmp/stats.json', 'w') as f:
        json.dump(stats, f)
    print(f"Statistiques : {stats}")

def send_email():
    print("Email envoyé avec les résultats")

with DAG(
    'simple_etl_dag',
    default_args=default_args,
    description='DAG simple ETL',
    schedule_interval=timedelta(days=1),
    catchup=False,
) as dag:
    
    task1 = PythonOperator(
        task_id='generate_data',
        python_callable=generate_data,
    )
    
    task2 = PythonOperator(
        task_id='calculate_stats',
        python_callable=calculate_stats,
    )
    
    task3 = PythonOperator(
        task_id='send_email',
        python_callable=send_email,
    )
    
    task1 >> task2 >> task3

2. DAG COMPLEXE AVEC DÉPENDANCES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

def extract_api():
    import requests
    response = requests.get('https://api.example.com/data')
    data = response.json()
    import json
    with open('/tmp/api_data.json', 'w') as f:
        json.dump(data, f)
    return 'API data extracted'

def extract_csv():
    # Simuler extraction CSV
    print("CSV extracted")
    return 'CSV extracted'

def extract_db():
    import sqlite3
    conn = sqlite3.connect('database.db')
    # Extraction...
    return 'DB extracted'

def clean_api_data(**context):
    # Récupérer le résultat de la tâche précédente
    api_result = context['ti'].xcom_pull(task_ids='extract_api')
    print(f"Cleaning {api_result}")
    # Nettoyage...

def clean_csv_data(**context):
    csv_result = context['ti'].xcom_pull(task_ids='extract_csv')
    print(f"Cleaning {csv_result}")

def clean_db_data(**context):
    db_result = context['ti'].xcom_pull(task_ids='extract_db')
    print(f"Cleaning {db_result}")

def merge_data(**context):
    # Récupérer tous les résultats
    api_clean = context['ti'].xcom_pull(task_ids='clean_api')
    csv_clean = context['ti'].xcom_pull(task_ids='clean_csv')
    db_clean = context['ti'].xcom_pull(task_ids='clean_db')
    print("Merging all data...")

def load_data(**context):
    merge_result = context['ti'].xcom_pull(task_ids='merge_data')
    print("Loading to warehouse...")

with DAG(
    'complex_etl_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:
    
    # Extraction (en parallèle)
    extract_api_task = PythonOperator(
        task_id='extract_api',
        python_callable=extract_api,
    )
    
    extract_csv_task = PythonOperator(
        task_id='extract_csv',
        python_callable=extract_csv,
    )
    
    extract_db_task = PythonOperator(
        task_id='extract_db',
        python_callable=extract_db,
    )
    
    # Transformation (en parallèle après extraction)
    clean_api_task = PythonOperator(
        task_id='clean_api',
        python_callable=clean_api_data,
    )
    
    clean_csv_task = PythonOperator(
        task_id='clean_csv',
        python_callable=clean_csv_data,
    )
    
    clean_db_task = PythonOperator(
        task_id='clean_db',
        python_callable=clean_db_data,
    )
    
    # Agrégation
    merge_task = PythonOperator(
        task_id='merge_data',
        python_callable=merge_data,
    )
    
    # Chargement
    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load_data,
    )
    
    # Définir les dépendances
    [extract_api_task, extract_csv_task, extract_db_task] >> \\
    [clean_api_task, clean_csv_task, clean_db_task] >> \\
    merge_task >> load_task

3. GESTION D'ERREURS ET RETRIES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup

def task_with_retry():
    import random
    if random.random() < 0.3:  # 30% de chance d'échec
        raise Exception("Erreur simulée")
    return "Succès"

def on_failure_callback(context):
    print(f"Tâche {context['task_instance'].task_id} a échoué")
    # Envoyer une alerte

task = PythonOperator(
    task_id='task_with_retry',
    python_callable=task_with_retry,
    retries=3,
    retry_delay=timedelta(minutes=2),
    on_failure_callback=on_failure_callback,
)

4. VARIABLES ET CONNEXIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from airflow.models import Variable
from airflow.hooks.base import BaseHook

# Utiliser une variable
api_key = Variable.get("api_key")
db_connection = BaseHook.get_connection("my_database")

def use_variables():
    print(f"API Key: {api_key}")
    print(f"DB Host: {db_connection.host}")

5. SCHEDULING AVEC CRON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Tous les jours à minuit
schedule_interval='0 0 * * *'

# Toutes les heures
schedule_interval='0 * * * *'

# Tous les lundis à 9h
schedule_interval='0 9 * * 1'

# Tous les 1er du mois
schedule_interval='0 0 1 * *'

BONNES PRATIQUES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Utiliser des IDs de tâches descriptifs
✅ Documenter les DAGs avec doc_md
✅ Utiliser des TaskGroups pour organiser
✅ Éviter les dépendances circulaires
✅ Tester les DAGs en mode debug
✅ Utiliser XComs pour passer des données
✅ Configurer les retries appropriés
✅ Utiliser les callbacks pour le monitoring
""")

print("\n" + "="*60)
print("FIN DE LA CORRECTION")
print("="*60)
print("\nNote : Adaptez ces exemples à vos besoins spécifiques.\n")

