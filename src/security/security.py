from flask_bcrypt import bcrypt

def hash_senha(senha):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(senha.encode('utf-8'), salt) 
    return hashed.decode('utf-8')

def checar_senha(senha, senha_hash):
    return bcrypt.checkpw(senha.encode('utf-8'), senha_hash.encode('utf-8'))