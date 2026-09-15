# 🚗 Locadora Veicular

Sistema de gestão de locadora veicular desenvolvido em Python com organização em camadas, usando SQLite como persistência local.

---

## 📌 Visão geral

Este projeto foi reorganizado para seguir uma arquitetura mais clara e sustentável, separando responsabilidades em:

- camada de infraestrutura
- entidades do domínio
- repositórios
- serviços de negócio
- interface de linha de comando

A aplicação permite cadastrar clientes e veículos, listar registros e realizar a locação de veículos com regras simples de negócio.

---

## ✨ Funcionalidades

- Cadastro de clientes
- Listagem de clientes
- Cadastro de veículos
- Listagem de veículos
- Aluguel de veículos
- Validação de cliente e disponibilidade do veículo
- Persistência em SQLite
- Menu interativo em terminal
- Estrutura de pacote Python organizada

---

## 🏗️ Estrutura do projeto

```text
locadora_veicular/
├── .venv/                     # ambiente virtual
├── database/                 # diretório para armazenamento do SQLite
├── locadora_veicular/        # pacote principal da aplicação
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── database.py       # conexão e inicialização do SQLite
│   ├── models/
│   │   ├── __init__.py
│   │   ├── cliente.py
│   │   └── veiculo.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── cliente_repository.py
│   │   └── veiculo_repository.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── locacao_service.py
│   └── __init__.py
├── main.py                   # menu principal da aplicação
├── pyproject.toml            # configuração do pacote
├── requirements.txt          # dependências do projeto
├── README.md
├── LICENSE
└── tests/                    # testes de smoke/import
```

---

## 🧩 Camadas da aplicação

### Core
Responsável pela configuração e conexão com o SQLite.

- [locadora_veicular/core/database.py](locadora_veicular/core/database.py)

### Models
Representam as entidades do domínio da aplicação.

- Cliente
- Veículo

### Repositories
Encapsulam a persistência e consulta no banco de dados.

- ClienteRepository
- VeiculoRepository

### Services
Centralizam a regra de negócio da locação.

- LocacaoService

### Main
Contém o menu interativo para o usuário usar o sistema.

- [main.py](main.py)

---

## ▶️ Como executar

### 1. Criar e ativar o ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalar o projeto em modo editável

```bash
pip install -e .
```

### 3. Rodar a aplicação

```bash
python main.py
```

ou, se preferir usar o interpretador do ambiente virtual:

```bash
.venv/bin/python main.py
```

---

## 🧪 Validação

O projeto foi validado em importação e execução básica do menu. O fluxo principal do sistema já foi testado com sucesso para:

- cadastro de cliente
- listagem de clientes
- saída do sistema

---

## 📝 Observações

- O projeto foi reorganizado para evitar dependência de pastas antigas e manter a estrutura como um pacote Python legítimo.
- O banco de dados é gerado e persistido localmente na pasta [database](database).
- O arquivo [requirements.txt](requirements.txt) está alinhado ao projeto atual e não exige bibliotecas externas além da biblioteca padrão do Python.

---

## 🎯 Objetivo acadêmico

O projeto foi pensado para praticar conceitos de:

- arquitetura em camadas
- modularização
- persistência com banco de dados
- encapsulamento de regras de negócio
- desenvolvimento de um sistema simples de gestão em Python