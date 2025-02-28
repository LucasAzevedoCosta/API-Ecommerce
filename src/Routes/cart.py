from flask import request, jsonify, Blueprint
from Models import CarItem, User, Product
from Database.database import SessionLocal
from flask_login import login_required, current_user

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/add/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):

    db = SessionLocal()
    try:
        # Obtém o usuário atual
        user = db.query(User).get(int(current_user.id))
        # Obtém o produto pelo ID
        product = db.query(Product).get(product_id)

        if user and product:
            # Define a quantidade desejada (pode ser obtida do request)
            quantity = request.json.get('quantity',1) # Ou use request.json.get('quantity', 1) para obter do corpo da requisição

            # Verifica se o produto já existe no carrinho
            existing_item = db.query(CarItem).filter_by(user_id=user.id, product_id=product.id).first()

            if existing_item:# Atualiza a quantidade e o total
                existing_item.quantity += quantity
                existing_item.total_price = existing_item.quantity * product.price
                db.commit()
                return jsonify({"message": "Quantidade do produto atualizada no carrinho"}), 200
            else:
                # Cria um novo item no carrinho
                car_item = CarItem(
                    user_id=user.id,
                    product_id=product.id,
                    quantity=quantity,
                    price=product.price,
                    total_price=product.price * quantity
                )
                db.add(car_item)
                db.commit()
                return jsonify({"message": "Produto adicionado ao carrinho"})
        else:
            return jsonify({"message": "Usuário ou produto não encontrado"}), 404
        
    except Exception as e:

        db.rollback()

        return jsonify({"message": f"Erro ao adicionar ao carrinho: {str(e)}"}), 400
    
    finally:
        db.close()


@cart_bp.route('/remove/<int:product_id>', methods=['DELETE'])
@login_required
def remove_to_cart(product_id):

    db = SessionLocal()
    try:
        car_item = db.query(CarItem).filter_by(user_id=current_user.id, product_id=product_id).first()
    
        if car_item:
            # Obtém a quantidade a ser removida
            quantity_to_remove = request.json.get('quantity', 1)  # Default é 1 se não informado

            if quantity_to_remove <= 0:
                return jsonify({"message": "A quantidade a ser removida deve ser maior que 0"}), 400
            
            if quantity_to_remove > car_item.quantity:
                return jsonify({"message": f"Quantidade a ser removida excede a quantidade disponível ({car_item.quantity})"}), 400

            # Reduz a quantidade ou deleta o item caso a quantidade seja 0
            car_item.quantity -= quantity_to_remove
            car_item.total_price = car_item.quantity * car_item.price

            if car_item.quantity <= 0:
                # Se a quantidade chegar a 0, deleta o item do carrinho
                db.delete(car_item)
                db.commit()
                return jsonify({"message": "Item removido do carrinho"})
            else:
                # Caso contrário, apenas atualiza a quantidade e o preço
                db.commit()
                return jsonify({"message": f"{quantity_to_remove} unidade(s) removida(s) do carrinho"})
        else:
            return jsonify({"message": "Item não encontrado no carrinho"}), 404


    except Exception as e:
        db.rollback()
        return jsonify({"message": f"Erro ao remover item do carrinho: {str(e)}", "error": "INTERNAL_SERVER_ERROR"}), 400
    
    finally:
        db.close()



@cart_bp.route('', methods=['GET'])
@login_required
def view_cart():
    db = SessionLocal()

    try:
        # Obtém o usuário atual
        user = db.query(User).get(int(current_user.id))
        cart_itens = db.query(CarItem).filter_by(user_id=user.id).all()
        cart_content = []

        for car_item in cart_itens:
            product = db.query(Product).get(car_item.product_id)
            cart_content.append({
                "id": car_item.id,
                "user_id": car_item.user_id,
                "product_id": car_item.product_id,
                "name": product.name,
                "quantity": car_item.quantity,
                "price": car_item.price,
                "total_price": car_item.total_price
            })
        return jsonify(cart_content)
    
    except Exception as e:
        db.rollback()
        return jsonify({"message": f"Erro ao visualizar carrinho: {str(e)}", "error": "INTERNAL_SERVER_ERROR"}), 400
    finally:
        db.close()
    


@cart_bp.route('/checkout', methods=['POST'])
@login_required
def checkout_cart():
    db = SessionLocal()

#por enquanto está só limpando o carrinho depois será adicionada mais funcionalizades
    try:
        # Obtém o usuário atual
        user = db.query(User).get(int(current_user.id))
        cart_itens = db.query(CarItem).filter_by(user_id=user.id).all()
        for car_item in cart_itens:
            db.delete(car_item)
        db.commit()

        return jsonify({"message": "Carrinho limpo"})    
    except Exception as e:
        db.rollback()
        return jsonify({"message": f""}), 400
    finally:
        db.close()
    