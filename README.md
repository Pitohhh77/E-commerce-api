E-commerce API 🛍️
Uma API RESTful completa para um sistema de e-commerce, construída com Flask e SQLAlchemy.

🚀 Visão Geral do Projeto
Este projeto é uma API de e-commerce robusta, projetada para gerenciar todos os aspectos de uma loja online. A aplicação é construída com Flask, um microframework web leve e poderoso, e utiliza SQLAlchemy para uma gestão de banco de dados eficiente e segura. A autenticação de usuário é tratada de forma simples e eficaz com o Flask-Login.

O objetivo principal é fornecer uma base sólida para qualquer plataforma de e-commerce, com endpoints bem definidos para operações essenciais como gerenciamento de produtos, carrinhos de compras e autenticação de usuários.

✨ Funcionalidades Principais
Autenticação de Usuários: Login e logout seguros com sessões de usuário.

Gerenciamento de Produtos: CRUD (Create, Read, Update, Delete) de produtos.

Carrinho de Compras: Adicionar, remover e visualizar itens no carrinho do usuário.

Checkout: Finalizar a compra, limpando o carrinho para novas transações.

🛠️ Tecnologias e Ferramentas
O projeto utiliza um conjunto de bibliotecas Python para oferecer uma solução completa e moderna:

Flask: O coração da API, fornecendo as rotas e o servidor web.

Flask-SQLAlchemy: Uma poderosa ORM (Object-Relational Mapper) para interagir com o banco de dados.

Flask-Login: Para gerenciar de forma segura as sessões de login dos usuários.

Flask-CORS: Habilita o Cross-Origin Resource Sharing, permitindo a integração com aplicações front-end em domínios diferentes.

Para mais detalhes, confira a lista completa de dependências no arquivo requirements.txt.

⚙️ Como Começar
Siga os passos abaixo para configurar e executar a API em sua máquina local.

Pré-requisitos
Python 3.x

pip (gerenciador de pacotes do Python)

Instalação
Clone este repositório:

Bash

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Crie e ative um ambiente virtual (recomendado):

Bash

python -m venv venv
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate
Instale as dependências do projeto:

Bash

pip install -r requirements.txt
Executando a Aplicação
A API utiliza o SQLite como banco de dados, e o arquivo ecommerce.db já está configurado. Basta executar o arquivo principal:

Bash

python app.py
A API estará disponível em http://127.0.0.1:5000.

🗺️ Documentação da API
A documentação da API é detalhada no arquivo swagger.yaml. Você pode usar esta especificação para testar os endpoints com ferramentas como Swagger UI ou Postman.

Aqui estão os principais endpoints para referência:

Método	Endpoint	Descrição
POST	/login	Autentica um usuário.
POST	/logout	Encerra a sessão do usuário.
GET	/api/products	Lista todos os produtos disponíveis.
GET	/api/products/{product_id}	Obtém detalhes de um produto específico.
POST	/api/cart/add/{product_id}	Adiciona um produto ao carrinho.
GET	/api/cart	Visualiza o conteúdo do carrinho.
POST	/api/cart/checkout	Finaliza a compra e limpa o carrinho.

Exportar para as Planilhas
🤝 Contribuição
Sua colaboração é muito bem-vinda! Se você tem ideias para melhorias, encontrou um bug ou quer adicionar novas funcionalidades, sinta-se à vontade para:

Abrir uma Issue descrevendo a sua sugestão.

Criar um Pull Request com suas alterações.
