from flask import request, jsonify, Blueprint
from Models import User
from Database.database import SessionLocal
from flask_login import login_required, logout_user

logout_bp = Blueprint('logout', __name__)


@logout_bp.route('', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso"}), 200