from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class UserModel(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    idade = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(255), nullable=False, )
    telefone = db.Column(db.String(20), nullable=True)
    endereco = db.Column(db.Text, nullable=True)
    data_cadastro = db.Column(db.Date, nullable=True)
    ativo = db.Column(db.Boolean, default=True, nullable=False)
    salario = db.Column(db.Numeric(10, 2), default=0)
    email_verificado = db.Column(db.Boolean, default=False)
    

    def __init__(self, nome, idade, email, telefone, endereco, data_cadastro, ativo, salario):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.data_cadastro = data_cadastro
        self.ativo = ativo
        self.salario = salario

    def __repr__(self):
        return f"<Usuario {self.nome}>"
