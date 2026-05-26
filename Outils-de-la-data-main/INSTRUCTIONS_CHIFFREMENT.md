# Instructions pour chiffrer les corrections

## Objectif

Les fichiers de correction seront visibles sur GitHub, mais leur contenu sera chiffré. Les étudiants pourront voir les fichiers mais ne pourront pas lire le contenu sans le mot de passe.

## Étapes

### 1. Installer la bibliothèque de chiffrement

```bash
pip install cryptography
```

### 2. Chiffrer toutes les corrections

```bash
python chiffrer_toutes_corrections.py
```

Ce script va :
- Lire tous les fichiers `correction.py` originaux
- Extraire le contenu de chaque correction
- Chiffrer le contenu avec le mot de passe
- Créer des fichiers `solution.py` avec le contenu chiffré intégré

### 3. Retirer les corrections du .gitignore

Les corrections sont maintenant chiffrées, elles peuvent être poussées sur GitHub. Le `.gitignore` a déjà été mis à jour.

### 4. Pousser sur GitHub

```bash
git add exercices/*/correction/ exercices/atelier-*/correction/
git add .gitignore
git commit -m "Ajout des corrections chiffrées"
git push origin main
```

## Utilisation par les étudiants

Quand un étudiant veut voir une correction :

```bash
cd exercice-01/correction
python solution.py
# Entrer le mot de passe quand demandé
```

**Le mot de passe est : `Abidexercice123`**

Tu peux le donner aux étudiants quand tu veux leur donner accès aux corrections.

## Avantages

- ✅ Les fichiers sont visibles sur GitHub (pas cachés)
- ✅ Le contenu est chiffré (illisible sans mot de passe)
- ✅ Les étudiants peuvent exécuter les scripts mais ne voient rien sans le mot de passe
- ✅ Tu contrôles quand donner le mot de passe

