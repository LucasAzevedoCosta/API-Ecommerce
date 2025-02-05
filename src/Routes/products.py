from flask import request, jsonify, Blueprint
from Models import Product
from Database.database import SessionLocal

products_bp = Blueprint('products', __name__)

@products_bp.route('/add', methods=['POST'])
def add_products():
    data = request.json

    #validando o cadastro de produtos
    if "name" in data and "price" in data:
        # Cria uma nova sessão
        db = SessionLocal()

        try:
            # Cria o objeto Product
            product = Product(
                name=data["name"],
                price=data["price"],
                description=data.get("description", "")
            )

            # Adiciona e commita o produto
            db.add(product)
            db.commit()

            # Retorna uma mensagem de sucesso
            return jsonify({"message": "Produto adicionado com sucesso"})

        except Exception as e:
            # Em caso de erro, faz rollback e retorna uma mensagem de erro
            db.rollback()
            return jsonify({"error": str(e)}), 500

        finally:
            # Fecha a sessão
            db.close()
    return jsonify({"error": "Dados inválidos"}), 400



@products_bp.route('/delete/<int:product_id>', methods=['DELETE'])
def delete_products(product_id):
    # Cria uma nova sessão
    db = SessionLocal()

    try:
        # Busca o produto pelo ID
        product = db.query(Product).get(product_id)

        if product:
            # Deleta e commita o produto
            db.delete(product)
            db.commit()

            # Retorna uma mensagem de sucesso
            return jsonify({"message": "Produto removido com sucesso"}), 200
        else:
            # Retorna uma mensagem de erro se o produto não for encontrado
            return jsonify({"error": "Produto não encontrado"}), 404

    except Exception as e:
        # Em caso de erro, faz rollback e retorna uma mensagem de erro
        db.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        # Fecha a sessão
        db.close()