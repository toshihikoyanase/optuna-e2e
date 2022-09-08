FROM python:3.9.10-buster

RUN pip install -U pip
RUN pip install git+https://github.com/c-bata/optuna.git@fix-issue-3966
RUN pip install PyMySQL psycopg2-binary cryptography alembic==1.5.1 sqlalchemy==1.3.0

WORKDIR /work
