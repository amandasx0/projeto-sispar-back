from src.model import database # traz a instancia do SQLAlchemy para esse arquivo
from sqlalchemy.schema import Column # traz o recurso que transforma atributos em coluna
from sqlalchemy.types import String, DECIMAL, Integer # traz o recurso que identifica os tipos de dado para as colunas

class Colaborador(database.Model): #mapear e criar a tabela
    __tablename__ = 'tb_colaboradores'
    #atributos
    id = Column(Integer, primary_key=True, autoincrement=True) #id INT AUTO_INCREMENT PRIMARY_KEY
    nome = Column(String(255))
    email = Column(String(150))
    senha = Column(String(255))
    cargo = Column(String(100))
    salario = Column(DECIMAL(10,2)) #2 quantidade de casa depois da virgula
    
    def __init__(self, nome, email, senha, cargo, salario):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo
        self.salario = salario
        
    def to_dict(self) -> dict:
         return {
            'email': self.email,
            'senha': self.senha
        }