from flask import request, jsonify, Blueprint
from Models import User
from Database.database import SessionLocal

sign_up_bp = Blueprint('sign_up', __name__)

@sign_up_bp.route('', methods=['POST'])
def sign_up():
    data = request.json

    if "username" in data and "password" in data and "role" in data:
        db = SessionLocal()

        try:
            user = User (
                username=data['username'],
                password=data['password'],
                role=data['role']
            )

            db.add(user)
            db.commit()

            return jsonify({"message": "Cadastro realizado com sucesso"})
        
        except Exception as e:
            db.rollback()
            return jsonify({"error": str(e)}), 500

        finally:
            db.close()
    return jsonify({"error": "Dados inválidos"}), 400