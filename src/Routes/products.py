from flask import request, jsonify, Blueprint
from Models import Product
from Database.database import SessionLocal
from flask_login import login_required

products_bp = Blueprint('products', __name__)

@products_bp.route('/add', methods=['POST'])
@login_required
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
@login_required
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
            return jsonify({"message": "Produto removido com sucesso"})
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



@products_bp.route('/<int:product_id>', methods=['GET'])
def get_products_details(product_id):
    # Cria uma nova sessão
    db = SessionLocal()

    try:
        # Busca o produto pelo ID
        product = db.query(Product).get(product_id)

        if product:
            return jsonify({
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "description": product.description
            })
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



@products_bp.route('/update/<int:product_id>', methods=['PUT'])
@login_required
def update_products(product_id):

    # Cria uma nova sessão
    db = SessionLocal()

    # Busca o produto pelo ID
    product = db.query(Product).get(product_id)
    if not product:
        return jsonify({"error": "Produto nao encontrado"}), 404

    data = request.json

    # Atualiza os dados do produto
    product.name = data.get("name", product.name)
    product.price = data.get("price", product.price)
    product.description = data.get("description", product.description)

    db.commit()
    db.close()

    return jsonify({"message": "Produto atualizado com sucesso"})


@products_bp.route('', methods=['GET'])
def get_products():

    # Cria uma nova sessão
    db = SessionLocal()
    
    products = db.query(Product).all()
    product_list = []

    for product in products:
        products_data = {
        "id": product.id,
        "name": product.name,
        "price": product.price
        }
        product_list.append(products_data)

    db.close()
    return jsonify(product_list)