#!/bin/bash
# Script pour partager les corrections avec les étudiants
# Usage: ./partager_corrections.sh

echo "=========================================="
echo "Partage des corrections avec les étudiants"
echo "=========================================="
echo ""
echo "Ce script va :"
echo "1. Retirer les corrections du .gitignore"
echo "2. Ajouter les corrections au dépôt"
echo "3. Créer un commit"
echo ""
read -p "Voulez-vous continuer ? (o/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Oo]$ ]]
then
    # Retirer du .gitignore
    echo "Retrait des corrections du .gitignore..."
    sed -i.bak '/exercices\/\*\/correction\//d' .gitignore
    sed -i.bak '/exercices\/atelier-\*\/correction\//d' .gitignore
    
    # Ajouter les corrections
    echo "Ajout des corrections..."
    git add exercices/*/correction/ exercices/atelier-*/correction/
    
    # Commit
    echo "Création du commit..."
    git commit -m "Rendre les corrections accessibles aux étudiants"
    
    echo ""
    echo "✅ Corrections ajoutées au dépôt"
    echo "⚠️  N'oubliez pas de faire : git push origin main"
else
    echo "Opération annulée"
fi

