from flask import Blueprint, render_template, flash, session
from models.usuario_model import Usuario

inicio_controller = Blueprint('inicio', __name__)

@inicio_controller.route('/')
def inicio():
    usuario1 = Usuario.query.filter_by(name=session.get('nome1')).first()
    if usuario1:
        flash(usuario1.vitorias)
    return render_template('inicio.html')