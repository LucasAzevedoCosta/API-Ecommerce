# API E-commerce

Este projeto consiste em uma API desenvolvida em Flask para gerenciamento de um sistema de e-commerce. Ele permite operações como cadastro de usuários, autenticação, adição de produtos, gerenciamento de carrinho de compras e muito mais.

![Projeto em Construção](https://img.shields.io/badge/Status-Em%20Construção-green)

Este repositório ainda está em fase de desenvolvimento. Novas funcionalidades estão sendo implementadas e melhorias serão feitas ao longo do tempo. Caso encontre algum problema ou tenha sugestões, fique à vontade para abrir uma issue ou contribuir!

---

## 🚀 Tecnologias Utilizadas

- 🐍 Python
- 🌐 Flask
- 🔄 Flask-CORS
- 🔑 Flask-Login (Autenticação)
- 🗄️ SQLAlchemy (ORM para banco de dados)
- 🐘 PostgreSQL (Banco de dados)
- 🐳 Docker & Docker Compose

## 📦 Configuração do Ambiente

### ✅ Pré-requisitos

Certifique-se de ter o **Python** e o **Docker** instalados na sua máquina.

### 📥 Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/API-Ecommerce.git
   cd API-Ecommerce
   ```
2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## ▶️ Como Executar

### 🔹 Opção 1: Executar diretamente com Python

```sh
python src/app.py
```

A API estará disponível em `http://127.0.0.1:5000/`.

### 🔹 Opção 2: Executar com Docker

```sh
docker-compose up --build
```

A API estará rodando dentro do container Docker.

## 🛠️ Estrutura do Projeto

| Pasta/Arquivo           | Descrição                                       |
| ----------------------- | ----------------------------------------------- |
| 📜 `.env`               | Configurações sensíveis do ambiente.            |
| 📜 `docker-compose.yml` | Configuração para execução com Docker.          |
| 📜 `requirements.txt`   | Lista de dependências do projeto.               |
| 📂 `src/`               | Código-fonte principal da API.                  |
| 📂 `src/Routes/`        | Definição das rotas e endpoints da API.         |
| 📂 `src/Models/`        | Modelos do banco de dados (ORM com SQLAlchemy). |
| 📂 `src/Database/`      | Configuração do banco de dados.                 |

## 🛠️ Funcionalidades Implementadas

- 🔐 **Autenticação de usuários**: Cadastro, login e logout de usuários com Flask-Login.
- 📦 **Gerenciamento de produtos**: Adicionar, listar, atualizar e remover produtos.
- 🛒 **Carrinho de compras**: Adicionar, remover e visualizar produtos no carrinho.
- 🔍 **Busca de produtos**: Permite pesquisar produtos por nome ou categoria.
- 📜 **Proteção de rotas**: Apenas usuários autenticados podem acessar certas funcionalidades.
- 🛠 **Persistência de dados**: Utilização de PostgreSQL para armazenamento seguro e eficiente.

---

🚀 **Fique ligado!** Novas funcionalidades estão chegando em breve, e este projeto continuará evoluindo! Caso queira contribuir, abra um Pull Request ou sugira melhorias. 🙌

