# 🚗 Sistema de Gestão de Locadora Veicular

> Projeto acadêmico em Python para simular o controle de uma locadora de veículos, aplicando conceitos de algoritmos, estruturas de dados e programação estruturada.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![License](https://img.shields.io/github/license/ViniciusFVianna/locadora_veicular?style=flat-square)

---

## 📌 Sobre o Projeto

Este projeto foi desenvolvido como parte das atividades da disciplina de Algoritmos de Programação do curso de graduação em Engenharia de Software. A proposta é criar um sistema simples, porém funcional, para gerenciar informações relacionadas a clientes, veículos e locações em uma locadora.

O objetivo principal é aplicar conceitos fundamentais da programação, como variáveis, estruturas condicionais, laços de repetição, funções, listas, dicionários e modularização, em um contexto realista e prático.

## ✨ Funcionalidades

- [x] Cadastro de clientes.
- [x] Cadastro de veículos.
- [x] Registro de locações.
- [x] Controle de disponibilidade dos veículos.
- [x] Listagem de carros, clientes e locações.
- [x] Persistência em arquivos JSON.
- [ ] Geração de relatórios avançados.
- [ ] Integração com banco de dados.

## 🛠️ Tecnologias e Ferramentas

As principais tecnologias e ferramentas utilizadas no projeto são:

- **Linguagem:** Python
- **Ambiente de desenvolvimento:** Visual Studio Code
- **Versionamento:** Git e GitHub
- **Persistência:** Arquivos locais em JSON
- **Paradigma:** Programação estruturada e modular

## 🏗️ Estrutura do Projeto

Uma visão geral da organização do repositório:

```text
locadora_veicular/
├── .venv/                  # Ambiente virtual do projeto
├── src/                    # Código-fonte principal
│   ├── database/
│   │   └── database.py     # Manipulação de dados em banco simples
│   ├── feature/
│   │   ├── datasource/
│   │   │   ├── json_datasource.py
│   │   │   └── json_datasource_impl.py
│   │   ├── domain/
│   │   │   ├── model/
│   │   │   │   ├── car.py
│   │   │   │   ├── client.py
│   │   │   │   └── rent.py
│   │   │   └── models/
│   │   │       ├── car_model.py
│   │   │       ├── cliente_model.py
│   │   │       └── rent_model.py
│   │   ├── repository/
│   │   │   ├── car/
│   │   │   ├── client/
│   │   │   └── rent/
│   │   └── usecase/
│   │       ├── car/
│   │       ├── client/
│   │       └── rent/
│   ├── main.py             # Menu principal do sistema
│   └── __init__.py
├── tests/                  # Testes e validações do projeto
├── .gitignore
├── requirements.txt
├── README.md
├── LICENSE
└── .git
```

## 📦 O que contém no projeto

O sistema foi organizado para separar responsabilidades em camadas, seguindo uma abordagem simples de arquitetura em módulos:

- **Models:** representam as entidades principais do sistema, como carro, cliente e locação.
- **DataSource:** responsável pela leitura e escrita de dados em arquivos JSON.
- **Repositories:** encapsulam o acesso e manipulação dos dados por entidade.
- **Use Cases:** centralizam a lógica da aplicação, como cadastro, listagem e regras de disponibilidade.
- **Main:** contém o menu interativo do programa para o usuário executar as operações.
- **Database:** armazena os arquivos de persistência, como carros, clientes e locações.

Essas estruturas permitem que o sistema gerencie:

- cadastro de veículos;
- cadastro de clientes;
- registro de locações;
- atualização da disponibilidade do carro;
- listagem dos itens cadastrados;
- persistência local em arquivos JSON.

## 🎯 Objetivos Acadêmicos

- Compreender e aplicar conceitos básicos de algoritmos.
- Praticar a organização do código em funções e módulos.
- Desenvolver uma solução simples para um problema real de gestão.
- Aprimorar habilidades de documentação e versionamento em projetos de software.

## ▶️ Como Executar

Para iniciar o sistema, rode o arquivo principal em Python a partir da pasta do projeto:

```bash
cd locadora_veicular
.venv/bin/python src/main.py
```

Ou, se preferir usar o interpretador global:

```bash
python src/main.py
```

Este comando abrirá o menu principal da locadora e permitirá cadastrar clientes, veículos e realizar locações.