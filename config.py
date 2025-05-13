from os import environ # Traz para o arquivo o acesso as variaveis de ambiente
from dotenv import load_dotenv # Traz a função para carregar as variaveis de ambiente nesse arquivo

load_dotenv() # Carrega as variaveis de ambiente para esse arquivo

class Config():
    SQLALCHEMY_DATABASE_URI = environ.get("URL_DATABASE_PROD")
    SQLALCHEMY_TRACK_MODIFICATIONS = False