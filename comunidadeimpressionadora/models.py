from comunidadeimpressionadora import database, login_manager
import datetime
from flask_login import UserMixin  #controla a conexão do login, quando a pessoa sai do site, etc


@login_manager.user_loader  # o decorater é pra dizer que a função é a logo abaixo
def load_usuario(id_usuario):  # o login_manager precisa de uma função que encontre o usuário pelo id
    return Usuario.query.get(int(id_usuario))


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False) # impede que o username seja vazio
    email = database.Column(database.String, nullable=False, unique=True) # o email precisa ser único
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post', backref='autor', lazy=True) #acessa quem criou o post (autor) / Lazy pega todas as informações do autor
    cursos = database.Column(database.String, nullable=False, default='Não informado') #apenas para exibir informação do curso

    def contar_posts(self):  # esse método foi criado dentro do models e não do routes, porque ele precisa funcionar para todos os usuários.
        return len(self.posts)


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False) #quando o texto é grande não é definido como string, mas como text
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False, ) #ForeignKey é a chave que liga o usuário ao post






