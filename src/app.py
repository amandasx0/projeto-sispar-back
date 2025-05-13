from flask import Flask # type: ignore
from flask_cors import CORS # type: ignore
from src.controller.colaborador_controller import bp_colaborador
from src.controller.reembolso_controller import bp_reembolso
from src.model import database
from config import Config
from flasgger import Swagger

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec", # <-- Da um nome de referencia para a documentacao
            "route": "/apispec.json/", # <- Rota do arquivo JSON para a construção da documentação
            "rule_filter": lambda rule: True, # <-- Todas as rotas/endpoints serão documentados
            "model_filter": lambda tag: True, # <-- Especificar quuais modelos da entidade serão documentados
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}   

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_colaborador)
    app.register_blueprint(bp_reembolso)
    
    CORS(app, origins = "*")
    
    app.config.from_object(Config) # trouxemos a configuraçao do ambiente de desenvolvimento
    database.init_app(app) # inicia a conexão com o banco de dados
    
    Swagger(app, config=swagger_config)
    
    with app.app_context():
        database.create_all() #cria a tabela caso nao exista
    
    return app

