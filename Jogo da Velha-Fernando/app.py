from flask import Flask
from database import init_database
from controllers.usuarios_controller import usuario

app = Flask(__name__)

init_database(app)
    
app.register_blueprint(usuario)

if __name__ == '__main__':
    app.run(debug=True)