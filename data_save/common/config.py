import os

class Config:
    # URL de conexão com o banco de dados PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:password@db:5432/mydatabase')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
