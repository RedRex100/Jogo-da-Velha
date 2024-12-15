from flask import Blueprint, render_template
from database import database
from models.usuario import Usuario

usuario = Blueprint('usuario', __name__)

def oi():
    User = Usuario(name = 'Pretinhio', senha = '1234')
    database.session.add(User)
    database.session.commit()

    usuarios = Usuario.query.all()
    return usuarios

@usuario.route('/')
def inaa():
    usuarios = oi()
    return render_template('inicio.html', usuarios = usuarios)