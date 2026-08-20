# trabalho_hackatton

# ♻️ Sistema de Reciclagem

Sistema desenvolvido em **Python** para gerenciamento de materiais recicláveis, pontos de coleta e registros de coleta.

O projeto foi desenvolvido como parte de um **Hackathon**, com o objetivo de criar uma solução simples para organizar informações relacionadas à reciclagem.

---

## 📋 Sobre o projeto

O **Sistema de Reciclagem** é uma aplicação executada pelo terminal que permite cadastrar materiais recicláveis, cadastrar pontos de coleta, registrar coletas realizadas e consultar informações por meio de relatórios.

A aplicação utiliza **Python** para a lógica do sistema e **MySQL** para armazenamento dos dados.

---

## ✨ Funcionalidades

O sistema possui as seguintes funcionalidades:

- ♻️ Cadastrar itens recicláveis
- 📋 Listar itens cadastrados
- 📍 Cadastrar pontos de coleta
- 📋 Listar pontos de coleta
- 🚛 Registrar coletas
- 📊 Listar coletas realizadas
- 📈 Gerar relatórios
- 🗑️ Remover itens cadastrados
- ✅ Validar informações inseridas pelo usuário

---

## 🛠️ Tecnologias utilizadas

- **Python 3**
- **MySQL**
- **MySQL Connector/Python**
- **SQL**

---

## 📁 Estrutura do projeto

    trabalho_hackatton/
    │
    ├── main.py
    ├── menu.py
    ├── funcoes.py
    ├── validacoes.py
    ├── database.sql
    ├── README.md
    └── LICENSE

### `main.py`

Responsável pela inicialização do sistema e pela conexão com o banco de dados MySQL.

### `menu.py`

Responsável pelo menu principal e pela navegação entre as funcionalidades do sistema.

### `funcoes.py`

Contém as principais funções do sistema, incluindo:

- cadastro de itens;
- listagem de itens;
- remoção de itens;
- cadastro de pontos de coleta;
- listagem de pontos de coleta;
- registro de coletas;
- listagem de coletas;
- geração de relatórios.

### `validacoes.py`

Responsável pelas validações dos dados fornecidos pelo usuário.

### `database.sql`

Contém a estrutura necessária para criação do banco de dados e suas tabelas.

---

## 🗄️ Banco de dados

O projeto utiliza o **MySQL**.

O banco de dados utilizado pela aplicação é:

    reciclagem

### Tabelas

O banco possui três tabelas principais:

### `itens`

Armazena os materiais recicláveis cadastrados.

Principais campos:

- `id`
- `nome`
- `categoria`

### `pontos_coleta`

Armazena os pontos de coleta cadastrados.

Principais campos:

- `id`
- `nome`
- `endereco`

### `coletas`

Armazena os registros das coletas realizadas.

Principais campos:

- `id`
- `item_id`
- `ponto_id`
- `quantidade`
- `data_coleta`

A tabela `coletas` relaciona os materiais recicláveis aos pontos de coleta, permitindo registrar a quantidade coletada e a data da coleta.

---

## ⚙️ Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- Python 3
- MySQL Server
- Pip

---

## 📦 Instalação

### 1. Clone o repositório

    git clone https://github.com/leonardocamilofrank-hue/trabalho_hackatton.git

### 2. Acesse a pasta do projeto

    cd trabalho_hackatton

### 3. Instale a dependência do MySQL

    pip install mysql-connector-python

### 4. Configure o banco de dados

Execute o arquivo `database.sql` utilizando o MySQL Workbench ou o terminal.

Exemplo:

    mysql -u root -p < database.sql

---

## 🔐 Configuração do banco

A aplicação precisa das informações de acesso ao MySQL para funcionar.

Caso seu ambiente utilize usuário, senha ou configurações diferentes, ajuste as informações de conexão no arquivo `main.py`.

> **Importante:** em ambientes reais, recomenda-se utilizar variáveis de ambiente para armazenar credenciais do banco de dados em vez de deixá-las diretamente no código.

---

## ▶️ Executando o projeto

Depois de configurar o banco de dados e instalar as dependências, execute:

    python main.py

O sistema será iniciado diretamente no terminal.

---

## 🖥️ Menu do sistema

O usuário pode navegar pelas opções disponíveis no menu, realizando operações como:

1. Cadastrar item
2. Listar itens
3. Cadastrar ponto de coleta
4. Listar pontos de coleta
5. Registrar coleta
6. Listar coletas
7. Gerar relatório
8. Remover item
9. Sair

---

## 📊 Relatórios

O sistema permite consultar informações relacionadas às coletas realizadas, como:

- quantidade total de material reciclado;
- quantidade de coletas realizadas;
- quantidade reciclada por item.

Essas informações são obtidas diretamente do banco de dados.

---

## 🔄 Fluxo de utilização

Um fluxo básico de utilização do sistema pode ser:

**Cadastrar item**  
↓  
**Cadastrar ponto de coleta**  
↓  
**Registrar coleta**  
↓  
**Listar coletas**  
↓  
**Gerar relatório**

---

## 🎯 Objetivo

O projeto tem como objetivo aplicar conceitos de desenvolvimento de software na criação de uma solução para gerenciamento de informações relacionadas à reciclagem.

Durante o desenvolvimento foram utilizados conceitos como:

- programação em Python;
- modularização;
- validação de dados;
- banco de dados relacional;
- SQL;
- operações CRUD;
- relacionamento entre tabelas;
- interação com o usuário pelo terminal.

---

## 👥 Equipe

Projeto desenvolvido para um **Hackathon** pelos seguintes integrantes:

- **Leonardo Camilo Frank**
- **Maria Fernanda Vargas de Souza**
- **Antônio Hoffmann**
- **Emanoel dos Santos Cardoso**

---

## 📌 Status

🚧 **Em desenvolvimento**

O sistema possui funcionalidades de cadastro, consulta, registro de coletas e geração de relatórios.

---

## 📄 Licença

Este projeto está disponível sob a licença definida no arquivo `LICENSE`.
