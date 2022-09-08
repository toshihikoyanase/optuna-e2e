FROM python:3.9.10-buster

RUN pip install -U pip
RUN pip install git+https://github.com/nzw0301/optuna.git@reduce-warning-in-rdb-tests
RUN pip install PyMySQL psycopg2-binary cryptography

WORKDIR /work
