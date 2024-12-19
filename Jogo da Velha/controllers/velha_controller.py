from flask import Blueprint, render_template, redirect, request, session, url_for
from models.usuario_model import Usuario
from database import database

velha_controller = Blueprint('velha', __name__)

def updateVitorias(nome, vitorias):
    try:
        usuario = Usuario.query.filter_by(name=nome).first()
        if usuario:
            usuario.vitorias = vitorias
            database.session.commit()
            return True
        return False
    except Exception as e:
        database.session.rollback()
        print(f"Erro ao atualizar vitórias do usuário: {e}")
        return False
    
def updateDerrotas(nome, derrotas):
    try:
        usuario = Usuario.query.filter_by(name=nome).first()
        if usuario:
            usuario.derrotas = derrotas
            database.session.commit()
            return True
        return False
    except Exception as e:
        database.session.rollback()
        print(f"Erro ao atualizar vitórias do usuário: {e}")
        return False

@velha_controller.route('/jogo', methods=['GET', 'POST'])
def tabuleiro():
    if session.get('nome1') and session.get('nome2'):
        if request.method == "POST":
            data = request.get_json()  # Corrigido para obter o JSON corretamente
            if data is None:
                return {"error": "Dados não fornecidos"}, 400  # Retorna erro se não houver dados

            valor = data.get('valor')
            if valor == 'Vitória do jogador 1!':
                usuario1 = Usuario.query.filter_by(name=session.get('nome1')).first()
                usuario2 = Usuario.query.filter_by(name=session.get('nome2')).first()
                if usuario1 and usuario2:
                    if updateVitorias(session.get('nome1'), usuario1.vitorias + 1):
                        updateDerrotas(session.get('nome2'), usuario2.derrotas + 1)
                        return {"message": "Vitória do jogador 1 atualizada com sucesso!"}, 200
                    else:
                        return {"error": "Erro ao atualizar vitórias."}, 500
                else:
                    return {"error": "Usuário não encontrado."}, 404
            elif valor == 'Vitória do jogador 2!':
                usuario1 = Usuario.query.filter_by(name=session.get('nome1')).first()
                usuario2 = Usuario.query.filter_by(name=session.get('nome2')).first()
                if usuario1 and usuario2:
                    if updateVitorias(session.get('nome2'), usuario2.vitorias + 1):
                        updateDerrotas(session.get('nome1'), usuario1.derrotas + 1)
                        return {"message": "Vitória do jogador 2 atualizada com sucesso!"}, 200
                    else:
                        return {"error": "Erro ao atualizar vitórias."}, 500
                else:
                    return {"error": "Usuário não encontrado."}, 404
            # Adicione outras condições para outros resultados do jogo, se necessário
        return render_template('jogodavelha.html')
    else:
        return redirect(url_for('login.login1'))