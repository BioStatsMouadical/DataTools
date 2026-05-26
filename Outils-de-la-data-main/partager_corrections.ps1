# Script PowerShell pour partager les corrections avec les étudiants
# Usage: .\partager_corrections.ps1

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Partage des corrections avec les étudiants" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Ce script va :" -ForegroundColor Yellow
Write-Host "1. Retirer les corrections du .gitignore"
Write-Host "2. Ajouter les corrections au dépôt"
Write-Host "3. Créer un commit"
Write-Host ""

$confirmation = Read-Host "Voulez-vous continuer ? (o/n)"

if ($confirmation -eq "o" -or $confirmation -eq "O") {
    # Retirer du .gitignore
    Write-Host "Retrait des corrections du .gitignore..." -ForegroundColor Green
    $content = Get-Content .gitignore
    $newContent = $content | Where-Object { 
        $_ -notmatch "exercices/\*/correction/" -and 
        $_ -notmatch "exercices/atelier-\*/correction/" 
    }
    $newContent | Set-Content .gitignore
    
    # Ajouter les corrections
    Write-Host "Ajout des corrections..." -ForegroundColor Green
    git add exercices/*/correction/ exercices/atelier-*/correction/
    
    # Commit
    Write-Host "Création du commit..." -ForegroundColor Green
    git commit -m "Rendre les corrections accessibles aux étudiants"
    
    Write-Host ""
    Write-Host "✅ Corrections ajoutées au dépôt" -ForegroundColor Green
    Write-Host "⚠️  N'oubliez pas de faire : git push origin main" -ForegroundColor Yellow
} else {
    Write-Host "Opération annulée" -ForegroundColor Red
}

