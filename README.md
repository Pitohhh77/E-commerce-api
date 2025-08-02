# 🛒 E-Commerce API

Este é um projeto de **API RESTful** para um sistema de **e-commerce** simples, construído com **Python**, **Flask**, **SQLAlchemy** e **SQLite**. Ele permite **registro e login de usuários**, **gerenciamento de produtos**, **carrinho de compras** e **checkout**.

---

## 🚀 Tecnologias utilizadas

- [Flask](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Flask-Login](https://flask-login.readthedocs.io/)
- [Flask-CORS](https://flask-cors.readthedocs.io/)
- SQLite (banco de dados embutido)

---

## 📂 Estrutura do projeto

```plaintext
.
├── app.py             # Código principal da API
├── requirements.txt   # Dependências do projeto
├── swagger.yaml       # Documentação da API
├── ecommerce.db       # Banco de dados SQLite
````

⚙️ Funcionalidades

✅ Registro de usuários

✅ Login e logout com sessão autenticada

✅ CRUD de produtos (criar, ler, atualizar, deletar)

✅ Carrinho de compras (adicionar/remover itens)

✅ Checkout (limpa o carrinho)

✅ Documentação via Swagger

🔐 Autenticação
O sistema usa Flask-Login para gerenciar sessões de usuário. Algumas rotas exigem autenticação.

📌 Rotas principais
POST /register → Cria novo usuário

POST /login → Login do usuário

POST /logout → Logout do usuário

POST /api/products/add → Adiciona produto (login obrigatório)

DELETE /api/products/delete/<product_id> → Deleta produto (login obrigatório)

PUT /api/products/update/<product_id> → Atualiza produto (login obrigatório)

GET /api/products → Lista todos os produtos

POST /api/cart/add/<product_id> → Adiciona item no carrinho (login obrigatório)

DELETE /api/cart/remove/<product_id> → Remove item do carrinho (login obrigatório)

GET /api/cart → Lista itens do carrinho (login obrigatório)

POST /api/cart/checkout → Finaliza compra (login obrigatório)

📃 Documentação
A documentação da API está disponível no arquivo swagger.yaml.
Você pode importar no Swagger Editor para testar as rotas.

▶️ Como executar
1️⃣ Clone este repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/seu-repositorio.git
2️⃣ Crie um ambiente virtual (opcional):

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
3️⃣ Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
4️⃣ Execute:

bash
Copiar
Editar
python app.py
O servidor rodará em: http://127.0.0.1:5000

🗃️ Banco de dados
Este projeto usa SQLite (ecommerce.db). Para resetar, basta deletar o arquivo .db e rodar novamente.

🙌 Contribuições
Contribuições são bem-vindas!
Abra uma issue ou Pull Request. 🚀

📜 Licença
Este projeto é de uso educacional. Modifique e use à vontade.

Desenvolvido por Pedro Henrique
