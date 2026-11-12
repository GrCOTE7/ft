# FT

## Cds

```pwsh
./go      # démarre gc000 (projet ft_main)
./go u    # démarre ftd000 + ftd001 (projet ft_all)
./go a    # démarre les trois
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
