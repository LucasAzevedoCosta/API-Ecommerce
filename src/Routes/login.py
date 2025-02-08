from flask import request, jsonify, Blueprint
from Models import User
from Database.database import SessionLocal
from flask_login import login_user

login_bp = Blueprint('login', __name__)


@login_bp.route('', methods=['POST'])
def login():
    data = request.json

    db = SessionLocal()
    
    user = db.query(User).filter_by(username=data['username']).first()

    if user and user.password == data.get("password"):
            login_user(user)
            return jsonify({"message": "Login realizado com sucesso"})

    db.close()
    return jsonify({"message": "Usuário ou senha inválidos"}), 401