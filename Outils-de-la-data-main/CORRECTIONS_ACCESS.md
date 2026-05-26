# Accès aux Corrections

## Pour les formateurs

Les corrections sont disponibles dans les dossiers `correction/` de chaque exercice et atelier.

Pour partager les corrections avec les étudiants plus tard, plusieurs options :

### Option 1 : Branche Git séparée

```bash
# Créer une branche avec les corrections
git checkout -b corrections
git add exercices/*/correction/ exercices/atelier-*/correction/
git commit -m "Ajout des corrections"
git push origin corrections

# Plus tard, pour rendre accessible :
# - Merger la branche dans main
# - Ou donner accès à la branche corrections
```

### Option 2 : Retirer du .gitignore

Quand tu veux partager les corrections :

1. Retire les lignes du `.gitignore` :
   ```
   # exercices/*/correction/
   # exercices/atelier-*/correction/
   ```

2. Push les corrections :
   ```bash
   git add exercices/*/correction/ exercices/atelier-*/correction/
   git commit -m "Rendre les corrections accessibles"
   git push origin main
   ```

### Option 3 : Tag/Release GitHub

Créer un tag/release avec les corrections à un moment précis du cours.

### Option 4 : Dépôt privé séparé

Garder les corrections dans un dépôt privé et le rendre public quand nécessaire.

## Mot de passe

Le mot de passe pour accéder aux corrections est : `Abidexercice123`

**Note** : Ce mot de passe est réservé aux formateurs. Ne le partagez qu'au moment approprié du cours.

