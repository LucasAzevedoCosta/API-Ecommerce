from flask import Flask
from Database.database import SessionLocal
from Database.database import engine, Base
from Models import User, Product
from Routes.products import products_bp
from Routes.sign_up import sign_up_bp
from Routes.login import login_bp
from flask_login import LoginManager


app = Flask(__name__)

login_manager = LoginManager()
Base.metadata.create_all(bind=engine)
login_manager.init_app(app)
login_manager.login_view = 'login'

app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(sign_up_bp, url_prefix='/sign_up')
app.register_blueprint(login_bp, url_prefix='/login')


@app.route('/')
def hello_world():
    db = SessionLocal()
    db.close()
    return "hello world"

if __name__ == "__main__":
    app.run(debug=True)