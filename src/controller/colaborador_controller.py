from flask import Blueprint, request, jsonify
from src.model.colaborador_model import Colaborador
from src.model import database
from src.security.security import hash_senha, checar_senha
from flasgger import swag_from

bp_colaborador = Blueprint('colaborador', __name__, url_prefix='/colaborador')

@bp_colaborador.route('/pegar-dados', methods=['GET'])
@swag_from('../docs/colaborador/pegar_dados_colaborador.yml')
def pegar_dados(): 
    colaboradores = Colaborador.query.all()  

    dados_colaboradores = [{
        'id': colaborador.id,
        'nome': colaborador.nome,
        'cargo': colaborador.cargo,
        'senha': colaborador.senha,
        'email': colaborador.email
    } for colaborador in colaboradores]

    return jsonify(dados_colaboradores), 200

@bp_colaborador.route('/cadastrar', methods=['POST'])
@swag_from('../docs/colaborador/cadastrar_colaborador.yml')
def cadastrar_colaborador():
    dados_requisicao = request.get_json()
    
    if not dados_requisicao:
        return jsonify( {'Erro': 'Todos os campos devem ser preenchidos'}), 400
    
    novo_colaborador = Colaborador(
        nome=dados_requisicao['nome'],
        email=dados_requisicao['email'],
        senha=hash_senha(dados_requisicao['senha']),
        cargo=dados_requisicao['cargo'],
        salario=dados_requisicao['salario']
    )
    
    database.session.add(novo_colaborador) # INSERT INTO tb_colaborado(nome, email, senha, cargo, salario) VALUES('nome','email','senha','cargo','salario')
    database.session.commit() #click no raio do SQL
    
    return jsonify({'message': 'Colaborador cadastrado com sucesso'}), 201

@bp_colaborador.route('/atualizar/<int:id_colaborador>', methods=['PUT'])
@swag_from('../docs/colaborador/atualizar_colaborador.yml')
def atualizar_dados_colaborador(id_colaborador):
    dados_colaborador = request.get_json()

    colaborador = Colaborador.query.get(id_colaborador)
    if not colaborador:
        return jsonify({"erro": "Colaborador não encontrado"}), 404

    if 'nome' in dados_colaborador:
        colaborador.nome = dados_colaborador['nome']
    if 'email' in dados_colaborador:
        colaborador.email = dados_colaborador['email']
    if 'senha' in dados_colaborador:
        colaborador.senha = dados_colaborador['senha']
    if 'cargo' in dados_colaborador:
        colaborador.cargo = dados_colaborador['cargo']
    if 'salario' in dados_colaborador:
        colaborador.salario = dados_colaborador['salario']

    database.session.commit()

    return jsonify({"message": "Dados do colaborador atualizados com sucesso"}), 200


@bp_colaborador.route('/login', methods=['POST'])
@swag_from('../docs/colaborador/login_colaborador.yml')
def login():
    dados_requisicao = request.get_json()
    
    email = dados_requisicao.get('email')
    senha = dados_requisicao.get('senha')
    
    if not email or not senha:
        return jsonify({'messagem': 'Email e senha são obrigatórios'}), 400
    
    colaborador = database.session.execute(
        database.select(Colaborador).where(Colaborador.email == email)
    ).scalar()
    
    if not colaborador:
        return jsonify({'messagem': 'Email ou senha incorretos'}), 404
   
    colaborador = colaborador.to_dict()

    # Corrigindo a leitura da senha
    senha_hash = colaborador.get('senha')

    if isinstance(senha_hash, bytes):
        senha_hash = senha_hash.decode('utf-8')

    if email == colaborador.get('email') and checar_senha(senha, senha_hash):
        return jsonify({'messagem': 'Login realizado com sucesso'}), 200

    return jsonify({'messagem': 'Email ou senha incorretos'}), 401