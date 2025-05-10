from flask import Flask
from flask_cors import CORS
from src.controller.colaborador_controller import bp_colaborador
from src.controller.reembolso_controller import bp_reembolso
from src.model import database
from config import Config

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_colaborador)
    app.register_blueprint(bp_reembolso)
    
    CORS(app, origins = "*")
    
    app.config.from_object(Config) # trouxemos a configuraçao do ambiente de desenvolvimento
    database.init_app(app) # inicia a conexão com o banco de dados
    
    with app.app_context():
        database.create_all() #cria a tabela caso nao exista
    
    return app

