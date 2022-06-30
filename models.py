from msilib.schema import Class
from nork_town import db
class Carro():
    MODELOS = ['Hatch', 'Sedan', 'Conversível']
    COR = ['Amarelo', 'Azul', 'Cinza']

class Acesso(db.Model):
    __tablename__ = "acesso"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Login %r>' % self.login


class Clientes(db.Model):
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

class Carros(db.Model):
    __tablename__ = "carros"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_cliente = db.Column(db.Integer,db.ForeignKey("clientes.id"))
    cor = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Carro %r>' % self.modelo