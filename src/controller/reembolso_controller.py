from datetime import datetime
from flask import Blueprint, request, jsonify
from src.model.reembolso_model import Reembolso
from src.model import database

bp_reembolso = Blueprint('reembolso', __name__, url_prefix='/reembolso')

@bp_reembolso.route('/cadastrar', methods=['POST'])
def cadastrar_reembolso():
    dados_request = request.get_json()
    
    if not dados_request:
        return jsonify( {'Erro': 'Todos os campos devem ser preenchidos'}), 400
    
   
    try:
        data_convertida = datetime.strptime(dados_request['data'], "%d/%m/%Y").date()
    except ValueError:
        return jsonify({'Erro': 'Formato de data inválido. Use o formato DD/MM/YYYY.'}), 400
   
    novo_reembolso = Reembolso(
        nome = dados_request['nome'],
        empresa = dados_request['empresa'],
        prestacao = dados_request['prestacao'],
        data = data_convertida,
        descricao = dados_request['descricao'],
        tipo_despesa = dados_request['tipo_despesa'],
        ctr_custo = dados_request['ctr_custo'],
        ordem = dados_request['ordem'],
        div = dados_request['div'],
        pep = dados_request['pep'],
        moeda = dados_request['moeda'],
        distancia = dados_request['distancia'],
        valor_km = dados_request['valor_km'],
        valor_faturado = dados_request['valor_faturado'],
        despesa = dados_request['despesa']
    )
    
    database.session.add(novo_reembolso) # INSERT INTO tb_colaborado(nome, email, senha, cargo, salario) VALUES('nome','email','senha','cargo','salario')
    database.session.commit() #click no raio do SQL
    
    return jsonify({'message': 'Colaborador cadastrado com sucesso'}), 201
    
    
@bp_reembolso.route('/pegar-reembolsos', methods=['GET'])
def pegar_reembolson():
    reembolsos = Reembolso.query.all()
    
    dados_reembolso = [{
        'nome': reembolso.nome,
        'empresa': reembolso.empresa,
        'prestacao': reembolso.prestacao,
        'data': reembolso.data,
        'descricao': reembolso.descricao,
        'tipo_despesa': reembolso.tipo_despesa,
        'ctr_custo': reembolso.ctr_custo,
        'ordem': reembolso.ordem,
        'div': reembolso.div,
        'pep': reembolso.pep,
        'moeda': reembolso.moeda,
        'distancia': reembolso.distancia,
        'valor_km': reembolso.valor_km,
        'valor_faturado': reembolso.valor_faturado,
        'despesa': reembolso.despesa
    } for reembolso in reembolsos]
    
    return jsonify(dados_reembolso), 200