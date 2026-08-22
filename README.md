# 💰 e-Finance

Sistema de **controle financeiro pessoal** desenvolvido para a disciplina de **Programação Orientada a Objetos II (POO II)**.

O projeto tem como objetivo aplicar conceitos de **modelagem de domínio, Programação Orientada a Objetos, regras de negócio, testes e boas práticas de desenvolvimento** na construção de uma aplicação financeira.

---

## 📌 Sobre o projeto

O **e-Finance** permite que um usuário organize sua vida financeira por meio do cadastro de contas e do registro de movimentações financeiras.

O sistema foi desenvolvido inicialmente a partir da **modelagem do domínio**, identificando os principais conceitos do problema antes da implementação das classes.

O domínio inicial contempla:

* 👤 Usuários
* 💳 Contas
* 💰 Movimentações
* 🏷️ Categorias

---

## 🎯 Objetivo

O principal objetivo do projeto é desenvolver um sistema capaz de representar e controlar operações financeiras pessoais, permitindo:

* Cadastrar usuários;
* Associar contas aos usuários;
* Registrar receitas e despesas;
* Categorizar movimentações;
* Controlar o saldo das contas;
* Aplicar regras de negócio relacionadas às movimentações financeiras.

Além do desenvolvimento do sistema, o projeto busca aplicar na prática os conceitos estudados em **Programação Orientada a Objetos**.

---

## 🧠 Modelagem do domínio

Antes da implementação, foi realizada uma análise do domínio do problema.

O processo utilizado foi:

```text
Problema
   ↓
Narrativa do domínio
   ↓
Identificação dos conceitos
   ↓
Identificação das entidades
   ↓
Definição dos atributos
   ↓
Definição dos relacionamentos
   ↓
Definição das regras de negócio
   ↓
Implementação
```

O domínio foi construído buscando representar os conceitos essenciais do controle financeiro sem transformar automaticamente todos os conceitos encontrados em classes.

---

## 🏗️ Entidades

### 👤 Usuário

Representa a pessoa que utiliza o sistema.

Principais atributos:

```text
nome
email
senha
contas
```

Um usuário pode possuir várias contas.

```text
Usuário 1 ───────── N Conta
```

---

### 💳 Conta

Representa uma conta financeira pertencente a um usuário.

Principais atributos:

```text
usuário
saldo
```

Exemplos de contas que podem existir no domínio:

* Conta corrente
* Poupança
* Carteira

---

### 💰 Movimentação

Representa uma alteração financeira realizada em uma conta.

Principais atributos:

```text
conta
tipo
valor
categoria
```

Uma movimentação pode representar:

* **RECEITA**
* **DESPESA**

---

### 🏷️ Categoria

Representa a classificação de uma movimentação financeira.

Exemplos:

* Alimentação
* Transporte
* Moradia
* Lazer
* Educação
* Salário

Uma categoria pode estar associada a várias movimentações.

```text
Categoria 1 ───────── N Movimentação
```

---

## 🔗 Relacionamentos

O modelo atual do domínio possui os seguintes relacionamentos:

```text
Usuário 1 ───────── N Conta

Conta 1 ───────── N Movimentação

Categoria 1 ────── N Movimentação
```

Representação simplificada:

```text
                  ┌───────────────┐
                  │    Usuário    │
                  └───────┬───────┘
                          │
                         1:N
                          │
                          ▼
                  ┌───────────────┐
                  │     Conta     │
                  └───────┬───────┘
                          │
                         1:N
                          │
                          ▼
                  ┌───────────────┐
                  │ Movimentação  │
                  └───────┬───────┘
                          │
                         N:1
                          │
                          ▼
                  ┌───────────────┐
                  │   Categoria   │
                  └───────────────┘
```

---

## 📋 Regras de negócio

As principais regras definidas para o domínio são:

### RN01 — Usuário possui contas

Um usuário pode possuir uma ou mais contas financeiras.

### RN02 — Conta pertence a um usuário

Toda conta deve estar associada a um usuário.

### RN03 — Conta possui saldo

Toda conta possui um saldo que representa seu valor financeiro atual.

### RN04 — Movimentação pertence a uma conta

Toda movimentação deve estar associada a uma conta.

### RN05 — Valor válido

O valor de uma movimentação deve ser maior que zero.

```text
valor > 0
```

### RN06 — Tipo da movimentação

Toda movimentação deve possuir um tipo:

```text
RECEITA
DESPESA
```

### RN07 — Receita

Uma receita aumenta o saldo da conta:

```text
saldo = saldo + valor
```

### RN08 — Despesa

Uma despesa reduz o saldo da conta:

```text
saldo = saldo - valor
```

### RN09 — Categoria

Toda movimentação deve possuir uma categoria.

---

## 🧩 Decisões de modelagem

Durante a construção do domínio, alguns conceitos foram analisados para evitar a criação desnecessária de entidades.

### Receita e Despesa

Receita e despesa não são entidades independentes.

Ambas representam uma **Movimentação**, diferenciadas pelo atributo `tipo`.

```text
TipoMovimentacao

RECEITA
DESPESA
```

### Categorias

Categorias como `Alimentação`, `Transporte` e `Lazer` não são classes diferentes.

Elas são instâncias da entidade:

```text
Categoria
```

Essa abordagem mantém o domínio mais simples e evita classes desnecessárias.

---

## 📁 Estrutura atual

A estrutura inicial do projeto está organizada da seguinte maneira:

```text
e-finance/
│
├── finance/
│   ├── __init__.py
│   ├── usuario.py
│   ├── conta.py
│   ├── movimentacao.py
│   └── categoria.py
│
├── tests/
│
├── README.md
└── ...
```

---

## 🐍 Implementação atual

As entidades principais estão sendo implementadas em Python utilizando classes e composição entre os objetos do domínio.

Exemplo simplificado:

```python
class Usuario:
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.contas = []
```

Um usuário pode então manter várias contas:

```text
Usuario
 ├── Conta Corrente
 ├── Poupança
 └── Carteira
```

---

## 🧪 Testes

Os testes serão utilizados para validar o comportamento das entidades e principalmente as regras de negócio.

Entre os comportamentos que deverão ser testados estão:

* Criação de usuário;
* Associação de contas ao usuário;
* Criação de movimentações;
* Associação de categorias;
* Validação do valor da movimentação;
* Adição de receitas ao saldo;
* Subtração de despesas do saldo.

A ferramenta utilizada para os testes será o **pytest**.

---

## 🛠️ Tecnologias

* **Python**
* **Programação Orientada a Objetos**
* **pytest**
* **Git**
* **GitHub**

---

## 🚧 Status do projeto

**Em desenvolvimento.**

### Implementado

* [x] Definição inicial do domínio
* [x] Identificação das entidades
* [x] Definição dos relacionamentos
* [x] Definição inicial das regras de negócio
* [x] Criação das classes principais

### Em desenvolvimento

* [ ] Implementação completa das regras de negócio
* [ ] Testes automatizados
* [ ] Validações
* [ ] Evolução do modelo de domínio
* [ ] Documentação técnica
* [ ] Novas funcionalidades

---

## 📚 Documentação

A documentação completa do domínio contém o processo de modelagem, narrativa, identificação dos conceitos, entidades, relacionamentos, regras de negócio e decisões de modelagem.

A documentação será mantida separadamente do README para que o repositório tenha uma visão geral objetiva, enquanto o documento de domínio apresenta o processo de modelagem com maior profundidade.

---

## 👨‍💻 Autor

**Rafael França**

Projeto desenvolvido como parte das atividades da disciplina de **Programação Orientada a Objetos II**.

---

> 🚧 **e-Finance** — Projeto acadêmico em desenvolvimento.
