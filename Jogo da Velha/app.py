from flask import Flask
from database import init_database
from controllers.login_controller import login_cadastro
from controllers.inicio_controller import inicio_controller
from controllers.velha_controller import velha_controller

app = Flask(__name__)
app.secret_key = 'chave'
init_database(app)
    
app.register_blueprint(login_cadastro)
app.register_blueprint(inicio_controller)
app.register_blueprint(velha_controller)

if __name__ == '__main__':
    app.run(debug=True)