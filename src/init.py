import os
import optuna
import pymssql

from objective import objective


def create_mssql_database() -> None:
    conn = pymssql.connect("mssql", "sa", "optuna-test-5ZYB")
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE optuna")


create_mssql_database()


print("mysql")
study1 = optuna.create_study(study_name="test", storage="mysql+pymysql://root:root@mysql:3306/optuna")
study1.optimize(objective, n_trials=10)
print("postgresql")
study2 = optuna.create_study(study_name="test", storage="postgresql+psycopg2://root:root@postgresql/optuna")
study2.optimize(objective, n_trials=10)
print("sqlite")
sqlite_path = os.path.join("data", "sample.db")
if os.path.exists(sqlite_path):
    os.remove(sqlite_path)
study3 = optuna.create_study(study_name="test", storage=f"sqlite:///{sqlite_path}")
study3.optimize(objective, n_trials=10)
print("mssql")
study4 = optuna.create_study(study_name="test", storage="mssql+pymssql://sa:optuna-test-5ZYB@mssql/optuna?charset=utf8")
study4.optimize(objective, n_trials=10)

print("done")
