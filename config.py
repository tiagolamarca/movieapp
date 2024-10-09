from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configurações do banco de dados MySQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tiago:Jimi@2022@localhost/movie'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app

