import os
import optuna

from objective import objective


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

print("done")
