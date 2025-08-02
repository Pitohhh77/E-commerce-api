# Importação
from flask import Flask, request, jsonify  # Usado nas requisições e retorno delas e para criar a API
from flask_sqlalchemy import SQLAlchemy  # Banco de dados
from flask_cors import CORS  # Usado para "transformar" o swagger em postman
from flask_login import UserMixin , login_user , LoginManager , login_required , logout_user , current_user # Usado para o login

# Criação da instancia
app = Flask(__name__)

# Chave Secreta para o login Manager
app.config["SECRET_KEY"] = "chave_123"

# Definir caminho para o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

# Configurar login Manager
login_manager = LoginManager() 
login_manager.init_app(app)    
login_manager.login_view = 'login'


# Iniciar conexão com banco de dados
db = SQLAlchemy(app)

# Ver no swagger
CORS(app)

# Modelagem
# User (id , username , password)
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    cart = db.relationship('CartItem', backref='user' , lazy=True) # Metódo para criar uma relação entre as classes lazy para performance

# Produto (id, name, price, description)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

# Item do carrinho de compras(id, user_id, product_id )
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id') , nullable = False) # Metódo que pega uma chave primaria de outro modelo
    product_id = db.Column(db.Integer, db.ForeignKey('product.id') , nullable = False)

# Autenticação
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Rota para registrar um novo usuário
@app.route('/register', methods=["POST"])
def register():
    data = request.json

    # Verifica se username e password foram enviados
    if not data.get("username") or not data.get("password"):
        return jsonify({"message": "Username and password are required"}), 400

    # Verifica se o usuário já existe
    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"message": "Username already exists"}), 400

    # Cria o novo usuário
    new_user = User(username=data["username"], password=data["password"])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"})

# Rota do login
@app.route('/login', methods=["POST"])
def login():
    data = request.json
    
    user = User.query.filter_by(username=data.get("username")).first()

    if user != None and data.get("password") == user.password:
       login_user(user)
       return jsonify({"message":"Logged successfully"})
    
    return jsonify({"message":"Unauthorized. Invalid credentials"}),401

# Rota do Logout
@app.route("/logout",methods =["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message":"Logout successfully"})

# Rota adicionar produtos
@app.route('/api/products/add', methods=["POST"])
@login_required
def add_product():
    data = request.json  # Vai receber os dados da requisição
    if "name" in data and "price" in data:
        product = Product(name=data["name"], price=data["price"], description=data.get("description", ""))
        # Mandar de fato o produto para o banco de dados
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product added successfully"})
    return jsonify({"message": "Invalid product data"}), 400

# Rota para deletar produtos
@login_required
@app.route("/api/products/delete/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product is not None:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully"})
    return jsonify({"message": "Product not found"}), 404

# Rota para pegar detalhes do produto
@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product_details(product_id):
    product = Product.query.get(product_id)
    if product is not None:
        return jsonify({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description
        })
    return jsonify({"message": "Product not found"}), 404

# Rota para atualizar o produto
@app.route("/api/products/update/<int:product_id>", methods=["PUT"])
@login_required
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404

    data = request.json
    if 'name' in data:
        product.name = data["name"]

    if 'price' in data:
        product.price = data["price"]

    if 'description' in data:
        product.description = data['description']

    db.session.commit()  # Sempre mandar commit para atualizar o banco de dados
    return jsonify({'message': "Product updated succesfully"})

# Rota para recuperar lista de produtos
@app.route("/api/products", methods=["GET"])
def get_products():
    products = Product.query.all()  # retornará todos os produtos em forma de lista
    product_list = []
    for product in products:
        product_data = {
            "id": product.id,
            "name": product.name,
            "price": product.price,
        }
        product_list.append(product_data)
    return jsonify(product_list)

# Checkout
# Rota para adicionar produtos no carrinho 
@app.route("/api/cart/add/<int:product_id>" , methods =["POST"])
@login_required
def add_to_cart(product_id):
    # Usuario
    user = User.query.get(int(current_user.id)) # Recuperar id do usuário para 
    # Produto
    product = Product.query.get(product_id)

    if user and product:
        cart_item = CartItem(user_id=user.id, product_id = product.id)
        db.session.add(cart_item)
        db.session.commit()
        return jsonify({'message': 'Item added to the cart successfully'})
    return jsonify({'message': 'Failed to add item to the cart'}) , 400

# Rota para remover item do carrinho
@app.route("/api/cart/remove/<int:product_id>", methods=["DELETE"])
@login_required
def remove_from_cart(product_id):
    cart_item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify({'message':'Item removed from the cart succesfully'})
    return  jsonify({'message':'Failed to remove item from the cart'}) , 400

# Rota para ver os itens do carrinho
@app.route("/api/cart",methods = ["GET"])
@login_required
def view_cart():
    # Recuperar o usuário
    user = User.query.get(int(current_user.id))
    cart_items = user.cart
    cart_content = []
    for cart_item in cart_items:
        product = Product.query.get(cart_item.product_id)
        cart_content.append({
                                "id": cart_item.id ,
                                "user_id":cart_item.user_id,
                                "product_id": cart_item.product_id,
                                "product_name": product.name,
                                "product_price":product.price
                            })
    return jsonify(cart_content)
        
# Rota de checkout
@app.route("/api/cart/checkout", methods = ["POST"])
@login_required
def checkout():
    user = User.query.get(int(current_user.id))
    cart_items = user.cart
    for cart_item in cart_items:
        db.session.delete(cart_item) # Deletar do carrinho e banco de dados
    db.session.commit()
    return jsonify({"message" : "Checkout successful. Cart has been cleared."})

# Shell context
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Product': Product, 'User': User, 'CartItem': CartItem}

if __name__ == '__main__':
    app.run(debug=True)  # Ativar modo depuração