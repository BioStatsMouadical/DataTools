"""
CORRECTION DE L'EXERCICE 01 - APACHE SUPERSET
Fichier chiffré - Nécessite le mot de passe pour déchiffrer
"""

import getpass
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

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

def dechiffrer_contenu():
    """Déchiffre le contenu de la correction"""
    # Le contenu chiffré est stocké ici (sera remplacé par le script de chiffrement)
    encrypted_content = b""  # Sera rempli par le script
    
    mot_de_passe = getpass.getpass("Entrez le mot de passe pour accéder à la correction : ")
    
    try:
        # Extraire le salt (16 premiers bytes)
        salt = encrypted_content[:16]
        encrypted_data = encrypted_content[16:]
        
        # Dériver la clé
        key = derive_key(mot_de_passe, salt)
        fernet = Fernet(key)
        
        # Déchiffrer
        decrypted_data = fernet.decrypt(encrypted_data)
        contenu = decrypted_data.decode('utf-8')
        
        print("\n" + "="*60)
        print("CORRECTION DE L'EXERCICE 01 - APACHE SUPERSET")
        print("="*60 + "\n")
        print(contenu)
        
    except Exception as e:
        print("Mot de passe incorrect. Accès refusé.")
        return False
    
    return True

if __name__ == "__main__":
    if not dechiffrer_contenu():
        exit(1)
