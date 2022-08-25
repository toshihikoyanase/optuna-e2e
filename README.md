### Setup database

```sh
docker compose up --build
```

### Clean

```sh
docker compose down
```

### Migration

```sh
# Create study and run optimize()
docker compose run --rm optuna-210 python src/init.py

# Run migration on RDB
docker compose run --rm optuna-300 bash src/upgrade.sh

# Resume study
docker compose run --rm optuna-300 python src/load.py
```
