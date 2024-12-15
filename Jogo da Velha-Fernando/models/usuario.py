from database import database

class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String(100), nullable = False)
    senha = database.Column(database.String(100), nullable = False)

def oi():
    User = Usuario(name = 'Pretinhio', senha = '1234')
    database.session.add(User)
    database.session.commit()

    usuarios = Usuario.query.all()
    return usuarios