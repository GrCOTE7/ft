# FT

## Commands

```pwsh
./go      # démarre gc000 (projet ft_main)
./go u    # démarre ftd000 + ftd001 (projet ft_all)
./go a    # démarre les trois
./go 0    # arrête tous les containers en route
```

Utils

```pwsh
# Voir les conteneurs par projet
docker compose -p ft_main ps
docker compose -p ft_all  ps

# Logs en direct
docker compose -p ft_main -f docker-compose.yml logs -f
docker compose -p ft_all  -f docker-compose_all_u.yml logs -f

# Arrêter une instance
docker compose -p ft_main -f docker-compose.yml down
docker compose -p ft_all  -f docker-compose_all_u.yml down
```

## BackTesting

Conseillé :

- 10 ans de période (Différents cycles de marchés)

  → 2018 à 2022 pour mise au point

- Nombre de trades : 200
  - Intraday (5m)
  - Swing (1d)

- En final, 5000+ trades pour bons calcul des Moyennes longues.

---

- [ ] Essayer config schema dev
