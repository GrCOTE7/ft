param(
    [string]$Mode = ""
)

$ErrorActionPreference = "Stop"
Set-Location -Path $PSScriptRoot

# Noms de projet Compose distincts pour isoler les deux stacks
$Project1 = "ft_main"
$Project2 = "ft_users"

function Start-Instance1 {
    Write-Host "▶ Instance 1 -> docker-compose.yml (projet: $Project1)" -ForegroundColor Cyan
    docker compose -p $Project1 -f docker-compose.yml up -d
}

function Start-Instance2 {
    Write-Host "▶ Instance 2 -> docker-compose_users.yml (projet: $Project2)" -ForegroundColor Cyan
    docker compose -p $Project2 -f docker-compose_users.yml up -d
}

function Stop-Instances {
    Write-Host "▶ Arrêt des instances (projets: $Project1 et $Project2)" -ForegroundColor Cyan
    docker compose -p $Project1 -f docker-compose.yml down
    docker compose -p $Project2 -f docker-compose_users.yml down
}

switch ($Mode.ToLower()) {
    ""  { Start-Instance1 }
    "u" { Start-Instance2 }
    "a" {
      Start-Instance1
      Start-Instance2
    }
    "0" { Stop-Instances }
    default {
        Write-Host "Usage: ./go [u|a|0]" -ForegroundColor Yellow
        Write-Host "  (aucun) : docker-compose.yml uniquement"
        Write-Host "  u       : docker-compose_users.yml uniquement"
        Write-Host "  a       : Tous fichiers en même temps"
        Write-Host "  0       : Arrêter toutes les instances"
        exit 1
    }
}
