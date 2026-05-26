"""
Script pour chiffrer toutes les corrections
Le contenu sera chiffré et intégré dans les fichiers solution.py
"""

import os
import base64
import re
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

PASSWORD = "Abidexercice123"

def derive_key(password: str, salt: bytes) -> bytes:
    """Dérive une clé à partir d'un mot de passe"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def chiffrer_contenu(contenu: str, password: str) -> bytes:
    """Chiffre un contenu avec un mot de passe"""
    salt = os.urandom(16)
    key = derive_key(password, salt)
    fernet = Fernet(key)
    encrypted = fernet.encrypt(contenu.encode('utf-8'))
    return salt + encrypted

def extraire_contenu_correction(fichier_original: str) -> str:
    """Extrait le contenu de la correction depuis le fichier original"""
    with open(fichier_original, 'r', encoding='utf-8') as f:
        contenu_complet = f.read()
    
    # Chercher le contenu entre print(""" et """)
    match = re.search(r'print\("""(.*?)"""\)', contenu_complet, re.DOTALL)
    if match:
        return match.group(1).strip()
    
    # Si pas trouvé, chercher avec print('''
    match = re.search(r"print\('''(.*?)'''\)", contenu_complet, re.DOTALL)
    if match:
        return match.group(1).strip()
    
    # Si toujours pas trouvé, retourner tout le fichier
    return contenu_complet

def creer_fichier_chiffre(contenu_texte: str, output_file: str, password: str, titre: str):
    """Crée un fichier Python avec le contenu chiffré intégré"""
    encrypted_bytes = chiffrer_contenu(contenu_texte, password)
    encrypted_b64 = base64.b64encode(encrypted_bytes).decode('utf-8')
    
    template = f'''"""
{titre}
Fichier chiffré - Le contenu est chiffré et nécessite le mot de passe pour être déchiffré.
"""

import getpass
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Contenu chiffré (base64) - Ne peut être déchiffré qu'avec le mot de passe
ENCRYPTED_CONTENT_B64 = """{encrypted_b64}"""

def derive_key(password: str, salt: bytes) -> bytes:
    """Dérive une clé à partir d'un mot de passe"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def dechiffrer_et_afficher():
    """Déchiffre et affiche le contenu de la correction"""
    mot_de_passe = getpass.getpass("Entrez le mot de passe pour accéder à la correction : ")
    
    try:
        # Décoder le contenu chiffré
        encrypted_bytes = base64.b64decode(ENCRYPTED_CONTENT_B64)
        
        # Extraire le salt (16 premiers bytes)
        salt = encrypted_bytes[:16]
        encrypted_data = encrypted_bytes[16:]
        
        # Dériver la clé
        key = derive_key(mot_de_passe, salt)
        fernet = Fernet(key)
        
        # Déchiffrer
        decrypted_data = fernet.decrypt(encrypted_data)
        contenu = decrypted_data.decode('utf-8')
        
        # Afficher le contenu
        print("\\n" + "="*60)
        print("{titre}")
        print("="*60 + "\\n")
        print(contenu)
        print("\\n" + "="*60)
        print("FIN DE LA CORRECTION")
        print("="*60)
        
    except Exception as e:
        print("❌ Mot de passe incorrect ou fichier corrompu. Accès refusé.")
        return False
    
    return True

if __name__ == "__main__":
    if not dechiffrer_et_afficher():
        exit(1)
'''
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"✅ {output_file} créé avec contenu chiffré")

if __name__ == "__main__":
    # Mapping des fichiers originaux vers les nouveaux
    fichiers_a_traiter = [
        ("exercices/exercice-01/correction.py", "exercices/exercice-01/correction/solution.py", "CORRECTION DE L'EXERCICE 01 - APACHE SUPERSET"),
        ("exercices/exercice-02/correction.py", "exercices/exercice-02/correction/solution.py", "CORRECTION DE L'EXERCICE 02 - METABASE"),
        ("exercices/exercice-03/correction.py", "exercices/exercice-03/correction/solution.py", "CORRECTION DE L'EXERCICE 03 - ELK STACK"),
        ("exercices/exercice-04/correction.py", "exercices/exercice-04/correction/solution.py", "CORRECTION DE L'EXERCICE 04 - APACHE SPARK"),
        ("exercices/exercice-05/correction.py", "exercices/exercice-05/correction/solution.py", "CORRECTION DE L'EXERCICE 05 - GRAFANA + PROMETHEUS"),
        ("exercices/exercice-06/correction.py", "exercices/exercice-06/correction/solution.py", "CORRECTION DE L'EXERCICE 06 - APACHE AIRFLOW"),
        ("exercices/exercice-07/correction.py", "exercices/exercice-07/correction/solution.py", "CORRECTION DE L'EXERCICE 07 - DBT"),
    ]
    
    for fichier_original, fichier_dest, titre in fichiers_a_traiter:
        if os.path.exists(fichier_original):
            contenu = extraire_contenu_correction(fichier_original)
            creer_fichier_chiffre(contenu, fichier_dest, PASSWORD, titre)
        else:
            print(f"⚠️  {fichier_original} non trouvé")
    
    print(f"\n✅ Tous les fichiers ont été chiffrés")
    print("⚠️  Les fichiers sont maintenant chiffrés et peuvent être poussés sur GitHub")
    print("⚠️  Seul le mot de passe permet de déchiffrer le contenu")
    print("\n📝 Les corrections sont maintenant visibles sur GitHub mais le contenu est chiffré")
