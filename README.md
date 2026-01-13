# 🔧 SISPAR – Back-end (API)

API desenvolvida em **Python** com **Flask** para gerenciamento de usuários e controle de despesas.  
Responsável pela autenticação, cadastro de usuários e operações de despesas.

---

## ✨ Funcionalidades

- Cadastro de usuário  
- Login com autenticação  
- Cadastro de despesas  
- Busca de despesas por ID  
- Listagem de todas as despesas  
- Criptografia de senha  
- API REST  

---

## 🛠️ Tecnologias Utilizadas

- Python  
- Flask  
- Flask-SQLAlchemy  
- Flask-Bcrypt  
- Flask-CORS  
- MySQL / PostgreSQL  
- SQLAlchemy  
- Gunicorn  
- Dotenv  
- Flasgger (Swagger)  

---

## ⚙️ Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
DB_HOST=localhost
DB_USER=seu_usuario
DB_PASS=sua_senha
DB_NAME=sispar
SECRET_KEY=sua_chave_secreta
```

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instalar dependências
pip install -r requirements.txt

# Rodar o servidor
python app.py
