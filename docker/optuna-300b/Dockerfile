FROM python:3.9.10-buster

RUN pip install -U pip
RUN pip install git+https://github.com/optuna/optuna.git@c23e17c
RUN pip install PyMySQL psycopg2-binary cryptography redis pymssql

WORKDIR /work
