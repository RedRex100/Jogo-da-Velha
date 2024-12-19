from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from database import database
from models.usuario_model import Usuario

login_cadastro = Blueprint('login', __name__)

def criar(name, senha):
    # Verifica se o usuário já existe antes de criar
    usuario_existente = Usuario.query.filter_by(name=name).first()
    if usuario_existente:
        return None  # O usuário já existe, então retornamos None
    
    # Se o usuário não existir, cria um novo
    usuario = Usuario(name=name, senha=senha, vitorias = 0, derrotas = 0, empates = 0)
    database.session.add(usuario)
    database.session.commit()
    return usuario

def logar1(name, senha):
    # Verifica se o usuário existe e se a senha está correta
    usuario = Usuario.query.filter_by(name=name).first()
    if usuario and usuario.senha == senha:
        session['nome1'] = name
        return True
    return False

def logar2(name, senha):
    # Verifica se o usuário existe e se a senha está correta
    usuario = Usuario.query.filter_by(name=name).first()
    if usuario and usuario.senha == senha and session.get('nome1') != name:
        session['nome2'] = name
        return True
    return False


@login_cadastro.route('/login1', methods=['GET', 'POST'])
def login1():
    numero = 1
    if session.get('nome1') is None and session.get('nome2') is None:  # Usuário não está logado
        if request.method == 'POST':
            nome = request.form['nome']
            senha = request.form['senha']
            if logar1(nome, senha):  # Se o login for bem-sucedido
                return redirect(url_for('login.login2'))
            else:
                # Tenta criar o usuário caso o login falhe
                if (criar(nome, senha)):
                    if logar1(nome, senha):
                        return redirect(url_for('login.login2'))  # Redireciona após o registro bem-sucedido
                else:
                    # Se o usuário já existir, mostra uma mensagem de erro
                    flash('Jogador 1 já existente com senha incorreta')
                    return render_template('login.html', numero = numero)
        return render_template('login.html', numero = numero)
    else:
        return redirect(url_for('inicio.inicio'))

@login_cadastro.route('/login2', methods=['GET', 'POST'])
def login2():
    numero = 2
    if session.get('nome2') is None and session.get('nome1') is not None:  # Usuário não está logado
        if request.method == 'POST':
            nome = request.form['nome']
            senha = request.form['senha']
            if logar2(nome, senha):  # Se o login for bem-sucedido
                return redirect(url_for('velha.tabuleiro'))
            else:
                # Tenta criar o usuário caso o login falhe
                if (criar(nome, senha)):
                    if logar2(nome, senha):
                        return redirect(url_for('velha.tabuleiro'))  # Redireciona após o registro bem-sucedido
                else:
                    flash('Jogador 1 não pode ser igual ao Jogador 2, e suas senhas e nomes devem ser compatíveis')
                    return render_template('login.html', numero = numero)
        return render_template('login.html', numero = numero)
    else:
        return redirect(url_for('velha.tabuleiro')) 

    
@login_cadastro.route('/novodesafiante1', methods=['GET', 'POST'])
def novodesafiante1():
    session.pop('nome1', None)
    numero = 1
    if session.get('nome1') is None and session.get('nome2') is None:  # Usuário não está logado
        if request.method == 'POST':
            nome = request.form['nome']
            senha = request.form['senha']
            if logar1(nome, senha):  # Se o login for bem-sucedido
                return redirect(url_for('login.login2'))
            else:
                # Tenta criar o usuário caso o login falhe
                if (criar(nome, senha)):
                    if logar1(nome, senha):
                        return redirect(url_for('login.login2'))  # Redireciona após o registro bem-sucedido
                else:
                    # Se o usuário já existir, mostra uma mensagem de erro
                    flash('Jogador 1 já existente com senha incorreta')
                    return render_template('login.html', numero = numero)
        return render_template('login.html', numero = numero)
    else:
        return redirect(url_for('inicio.inicio'))
    
@login_cadastro.route('/novodesafiante2', methods=['GET', 'POST'])
def novodesafiante2():
    session.pop('nome2', None)
    numero = 2
    if session.get('nome2') is None and session.get('nome1') is not None:  # Usuário não está logado
        if request.method == 'POST':
            nome = request.form['nome']
            senha = request.form['senha']
            if logar2(nome, senha):  # Se o login for bem-sucedido
                return redirect(url_for('inicio.inicio'))
            else:
                # Tenta criar o usuário caso o login falhe
                if (criar(nome, senha)):
                    if logar2(nome, senha):
                        return redirect(url_for('inicio.inicio'))  # Redireciona após o registro bem-sucedido
                else:
                    flash('Jogador 1 não pode ser igual ao Jogador 2, e suas senhas e nomes devem ser compatíveis')
                    return render_template('login.html', numero = numero)
        return render_template('login.html', numero = numero)
    else:
        return redirect(url_for('velha.tabuleiro')) 
    
@login_cadastro.route('/logout')
def logout():
    session.pop('nome1', None)
    session.pop('nome2', None)
    return redirect(url_for('inicio.inicio'))