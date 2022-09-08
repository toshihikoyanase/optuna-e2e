#!env bash

echo "mysql"
optuna storage upgrade --storage mysql+pymysql://root:root@mysql:3306/optuna

echo "postgresql"
optuna storage upgrade --storage postgresql+psycopg2://root:root@postgresql/optuna

echo "sqlite"
optuna storage upgrade --storage sqlite:///data/sample.db
