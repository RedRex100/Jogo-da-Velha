from database import database

class Usuario(database.Model):
    
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50), nullable=False, unique=True)
    senha = database.Column(database.String(100), nullable=False)
    vitorias = database.Column(database.Integer, nullable=False, default = 0)
    derrotas = database.Column(database.Integer, nullable=False, default = 0)
    empates = database.Column(database.Integer, nullable=False, default = 0)
