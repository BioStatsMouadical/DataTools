"""
Script pour chiffrer le contenu des corrections
Les fichiers seront visibles sur GitHub mais le contenu sera chiffré
"""

import os
import base64
import glob
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

PASSWORD = "Abidexercice123"  # Mot de passe pour chiffrer/déchiffrer

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

def creer_fichier_chiffre(contenu_original: str, output_file: str, password: str):
    """Crée un fichier Python avec le contenu chiffré intégré"""
    # Chiffrer le contenu
    encrypted_bytes = chiffrer_contenu(contenu_original, password)
    encrypted_b64 = base64.b64encode(encrypted_bytes).decode('utf-8')
    
    # Template du fichier avec contenu chiffré
    template = f'''"""
CORRECTION - Fichier chiffré
Le contenu est chiffré et nécessite le mot de passe pour être déchiffré.
"""

import getpass
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Contenu chiffré (base64)
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
        print("CORRECTION")
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
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"✅ {output_file} créé avec contenu chiffré")

if __name__ == "__main__":
    # Lire tous les fichiers solution.py originaux et les chiffrer
    fichiers_originaux = []
    fichiers_originaux.extend(glob.glob("exercices/exercice-*/correction/solution.py"))
    fichiers_originaux.extend(glob.glob("exercices/atelier-*/correction/solution.py"))
    
    # Lire le contenu original de chaque fichier
    for fichier_original in fichiers_originaux:
        # Lire le contenu original (sans la partie chiffrement)
        with open(fichier_original, 'r', encoding='utf-8') as f:
            contenu = f.read()
        
        # Extraire seulement la partie contenu (après les prints)
        # On va garder tout le contenu original
        creer_fichier_chiffre(contenu, fichier_original, PASSWORD)
    
    print(f"\n✅ {len(fichiers_originaux)} fichiers chiffrés avec succès")
    print("⚠️  Les fichiers sont maintenant chiffrés et peuvent être poussés sur GitHub")
    print("⚠️  Seul le mot de passe permet de déchiffrer le contenu")
