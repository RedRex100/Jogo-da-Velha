from database import database

class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String(100), nullable = False)
    senha = database.Column(database.String(100), nullable = False)
