from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '955e2630c4ce08e0b7855eec624f38bc'   '''o código foi gerado no terminal do python. No terminal digitei python.
Depois import secrets  e depois: secrets.token_hex(16)'''

if os.getenv("DATABASE_URL"):  # inclusão no banco de dados postgres no servidor railway
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'  # configurando o banco de dados

database = SQLAlchemy(app)  #cria o banco de dados
bcrypt = Bcrypt(app)  #cria a criptografia
login_manager = LoginManager(app)  # gerencia o login
login_manager.login_view = 'login'  # a pagina que vai direcionar quando usuario fizer login na pagina bloqueada
login_manager.login_message_category = 'alert-info'  # mensage que exibe para fazer login

from comunidadeimpressionadora import models
engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
inspector = sqlalchemy.inspect(engine)
if not inspector.has_table("usuario"):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print("Base de dados criado")
else:
    print("Base de dados já existente")

from comunidadeimpressionadora import routes #Está executando os routes. Ele está no fim, porque 1º precisa executar o app




