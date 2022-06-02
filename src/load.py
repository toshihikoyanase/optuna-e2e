import optuna

from objective import objective


print("mysql")
study1 = optuna.load_study(study_name="test", storage="mysql+pymysql://root:root@mysql:3306/optuna")
try:
    study1.optimize(objective, n_trials=1)
except:
    pass
print("postgresql")
study2 = optuna.load_study(study_name="test", storage="postgresql+psycopg2://root:root@postgresql/optuna")
try:
    study2.optimize(objective, n_trials=1)
except:
    pass
print("sqlite")
study3 = optuna.load_study(study_name="test", storage="sqlite:///data/sample.db")
try:
    study3.optimize(objective, n_trials=1)
except:
    pass
print("mssql")
study4 = optuna.load_study(study_name="test", storage="mssql+pymssql://sa:optuna-test-5ZYB@mssql/optuna?charset=utf8")
try:
    study4.optimize(objective, n_trials=1)
except:
    pass
print("redis")
study5 = optuna.load_study(study_name="test", storage="redis://redis:6379")
try:
    study5.optimize(objective, n_trials=1)
except:
    pass

print(study1.trials[-1].value)
print(study2.trials[-1].value)
print(study3.trials[-1].value)
print(study4.trials[-1].value)
print(study5.trials[-1].value)

print("done")
