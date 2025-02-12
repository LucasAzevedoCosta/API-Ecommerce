from flask import Flask
from Database.database import SessionLocal
from Database.database import engine, Base
from Models import User, Product, CarItem
from Routes import products_bp, sign_up_bp, login_bp, logout_bp
from flask_login import LoginManager
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# Define a secret_key a partir da variável de ambiente
app.secret_key = os.getenv('SECRET_KEY')

# Inicializa o LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' 

# Função para carregar um usuário a partir do ID
@login_manager.user_loader
def load_user(user_id):
    db = SessionLocal()
    user = db.query(User).get(user_id)
    db.close()
    return user

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Registra os Blueprints
app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(sign_up_bp, url_prefix='/sign_up')
app.register_blueprint(login_bp, url_prefix='/login')
app.register_blueprint(logout_bp, url_prefix='/logout')


@app.route('/')
def hello_world():
    db = SessionLocal()
    db.close()
    return "hello world"

if __name__ == "__main__":
    app.run(debug=True)