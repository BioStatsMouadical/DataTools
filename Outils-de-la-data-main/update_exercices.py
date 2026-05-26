"""
Script pour mettre à jour tous les README des exercices
- Enlève les durées estimées
- Ajoute les instructions de push
"""

import os
import re

def update_readme(file_path, exercice_num):
    """Met à jour un README d'exercice"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Enlever les durées estimées (lignes comme "**Durée estimée : X heures**")
    content = re.sub(r'\*\*Durée estimée.*?\*\*', '', content)
    content = re.sub(r'Durée estimée.*?\n', '', content)
    
    # Enlever les durées dans les tableaux
    content = re.sub(r'\|\s*\d+[h-]\d+h\s*\|', '|', content)
    
    # Remplacer la section Soumission
    old_soumission = r'## 📤 Soumission.*?Suivez les instructions.*?'
    new_soumission = f"""## 📤 Comment soumettre votre solution

### Étapes pour pousser votre exercice sur GitHub

1. **Préparez votre environnement** :
   ```bash
   cd exercice-{exercice_num:02d}
   ```
   
   {"2. **Générez les données nécessaires** (si applicable) :" if exercice_num in [1, 4, 5] else "2. **Créez la base de données** (si applicable) :" if exercice_num == 2 else "2. **Installez les dépendances** :"}
   ```bash
   {"python generer_donnees.py" if exercice_num in [1, 4] else "python generer_metriques.py" if exercice_num == 5 else "python creer_base_donnees.py" if exercice_num == 2 else "# Installez les outils requis selon les instructions du README"}
   ```

2. **Créez votre dossier de solution** :
   ```bash
   mkdir -p solutions/votre-nom
   cd solutions/votre-nom
   ```

3. **Placez tous vos fichiers** dans ce dossier :
   - Votre code source
   - Votre fichier `resultats.md`
   - Tous les fichiers générés (graphiques, exports, etc.)

4. **Ajoutez et commitez vos fichiers** :
   ```bash
   git add solutions/votre-nom/
   git commit -m "Solution exercice {exercice_num:02d} - Votre Nom"
   ```

5. **Poussez vers GitHub** :
   ```bash
   git push origin main
   ```
   
   Si vous avez forké le dépôt :
   ```bash
   git push origin votre-branche
   ```

6. **Créez une Pull Request** (si vous avez forké) ou vos fichiers seront directement visibles dans le dépôt principal.

### Structure de votre soumission

Votre dossier `solutions/votre-nom/` doit contenir :
- ✅ Tous vos fichiers de code source
- ✅ `resultats.md` : Votre analyse et résultats
- ✅ Tous les fichiers générés (graphiques, exports, etc.)
- ✅ Un fichier `README.md` (optionnel) expliquant votre approche

### Vérification

Avant de pousser, vérifiez que :
- [ ] Votre code fonctionne sans erreur
- [ ] Tous les fichiers sont présents
- [ ] La documentation est complète
- [ ] Les critères d'évaluation sont remplis

**Important** : N'oubliez pas de remplacer "votre-nom" par votre vrai nom dans le chemin du dossier !"""
    
    # Remplacer la section soumission
    content = re.sub(old_soumission, new_soumission, content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Mis a jour : {file_path}")

# Mettre à jour tous les exercices
for i in range(1, 8):
    readme_path = f"exercices/exercice-{i:02d}/README.md"
    if os.path.exists(readme_path):
        update_readme(readme_path, i)

# Mettre à jour les ateliers
ateliers = [1, 2, 3]
for i in ateliers:
    readme_path = f"exercices/atelier-{i:02d}/README.md"
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Enlever les durées
        content = re.sub(r'\*\*Durée estimée.*?\*\*', '', content)
        content = re.sub(r'Durée estimée totale.*?\n', '', content)
        
        # Ajouter instructions de push
        old_soumission = r'## 📤 Soumission.*?Suivez les instructions.*?'
        new_soumission = f"""## 📤 Comment soumettre votre solution

### Étapes pour pousser votre atelier sur GitHub

1. **Créez votre dossier de solution** :
   ```bash
   cd atelier-{i:02d}
   mkdir -p solutions/votre-nom
   cd solutions/votre-nom
   ```

2. **Placez tous vos fichiers** dans ce dossier :
   - Tous vos fichiers de code
   - Votre documentation
   - Tous les fichiers générés

3. **Ajoutez et commitez** :
   ```bash
   git add solutions/votre-nom/
   git commit -m "Atelier {i:02d} - Votre Nom"
   git push origin main
   ```

4. **Créez une Pull Request** si vous avez forké le dépôt.

**Important** : N'oubliez pas de remplacer "votre-nom" par votre vrai nom !"""
        
        content = re.sub(old_soumission, new_soumission, content, flags=re.DOTALL)
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Mis a jour : {readme_path}")

print("\nTous les README ont ete mis a jour !")

