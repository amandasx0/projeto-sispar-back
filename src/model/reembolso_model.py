from src.model import database
from sqlalchemy.schema import Column
from sqlalchemy.types import String, DECIMAL, Integer, INT, Date

class Reembolso(database.Model):
    __tablename__ = 'tb_reembolso'
    
    id = Column(Integer, primary_key=True, autoincrement=True) #id INT AUTO_INCREMENT PRIMARY_KEY
    nome = Column(String(255))
    empresa = Column(String(150))
    prestacao = Column(INT)
    data = Column(Date)
    descricao = Column(String(250))
    tipo_despesa = Column(String(250))
    ctr_custo = Column(String(250))
    ordem = Column(INT)
    div = Column(INT)
    pep = Column(INT)
    moeda = Column(String(10))
    distancia = Column(DECIMAL(10, 2))
    valor_km = Column(DECIMAL(10, 2))
    valor_faturado = Column(DECIMAL(10, 2))
    despesa = Column(DECIMAL(10, 2))
    status = Column(String(100))
    
    def __init__(self, nome, empresa, prestacao, data, descricao, tipo_despesa, ctr_custo, ordem, div, pep, moeda, distancia, valor_km, valor_faturado, despesa, status):
        self.nome = nome
        self.empresa = empresa
        self.prestacao = prestacao
        self.data = data
        self.descricao = descricao
        self.tipo_despesa = tipo_despesa
        self.ctr_custo = ctr_custo
        self.ordem = ordem
        self.div = div
        self.pep = pep
        self.moeda = moeda
        self.distancia = distancia
        self.valor_km = valor_km
        self.valor_faturado = valor_faturado
        self.despesa = despesa
        self.status = status

        
        