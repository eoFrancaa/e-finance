# 💰 e-Finance

Sistema de controle financeiro desenvolvido para a disciplina de **Programação Orientada a Objetos II (POO II)**.

O projeto tem como objetivo aplicar conceitos de **modelagem de domínio, orientação a objetos, relacionamentos entre entidades, regras de negócio, testes automatizados e decisões de projeto** na construção de um sistema financeiro.

---

## 📌 Sobre o projeto

O **e-Finance** é um sistema de controle financeiro que busca representar operações relacionadas ao gerenciamento de contas e lançamentos financeiros.

O desenvolvimento do projeto é realizado de forma incremental, partindo da **modelagem do domínio** para posteriormente implementar os comportamentos e regras de negócio.

O domínio inicial é composto pelas seguintes entidades:

- 💳 Conta
- 🏷️ Categoria
- 💰 Lançamento
- 📊 Fechamento
- 🔎 Conciliação
- 📄 Extrato

---

## 🎯 Objetivo

O objetivo do e-Finance é permitir a representação e o controle de informações financeiras, possibilitando o registro de lançamentos e a consolidação das informações de determinado período.

Além da construção do sistema, o projeto busca aplicar na prática os conceitos estudados na disciplina de **Programação Orientada a Objetos II**.

---

## 🧠 Modelagem do domínio

O desenvolvimento parte da análise do problema e da identificação dos conceitos relevantes do domínio.

O processo de desenvolvimento segue a seguinte sequência:

```text
Problema
   ↓
Análise do domínio
   ↓
Identificação dos conceitos
   ↓
Identificação das entidades
   ↓
Atributos e responsabilidades
   ↓
Relacionamentos
   ↓
Regras de negócio
   ↓
Implementação
   ↓
Testes
```

A modelagem busca evitar a criação de classes desnecessárias e atribuir a cada objeto uma responsabilidade coerente com o domínio.

---

## 🏗️ Entidades do domínio

### 💳 Conta

Representa uma conta financeira utilizada no sistema.

**Atributos iniciais:**

- `nome`
- `saldo`

**Responsabilidade:**

Representar a conta e manter as informações relacionadas ao seu saldo.

---

### 🏷️ Categoria

Representa a classificação de um lançamento financeiro.

**Atributos iniciais:**

- `nome`

**Exemplos:**

- Alimentação
- Transporte
- Moradia
- Lazer
- Educação
- Salário

Uma mesma categoria pode ser utilizada por vários lançamentos.

```text
Categoria 1 ───────── N Lançamento
```

---

### 💰 Lançamento

Representa um registro financeiro associado a uma conta.

**Atributos iniciais:**

- `descrição`
- `valor`
- `data`
- `categoria`

Um lançamento possui uma categoria e está relacionado à conta na qual a operação financeira ocorre.

```text
Conta 1 ───────── N Lançamento
```

---

### 📊 Fechamento

Representa a consolidação dos lançamentos de determinado período.

Sua responsabilidade é trabalhar com um conjunto de lançamentos e produzir informações consolidadas sobre o período.

O tratamento dos lançamentos utilizados pelo fechamento será definido durante a implementação e documentado como uma decisão de projeto.

---

### 🔎 Conciliação

Responsável por verificar a correspondência entre os valores financeiros considerados no processo de conciliação.

A conciliação deverá identificar situações em que os valores não estejam de acordo e apresentar uma falha de forma clara.

A classe `Conciliacao` será mantida como uma responsabilidade própria, separada de `Fechamento`.

---

### 📄 Extrato

Responsável por apresentar um resumo das informações financeiras de determinado período.

O extrato utiliza as informações consolidadas para representar o resultado financeiro do período.

---

## 🔗 Relacionamentos

O modelo inicial do domínio possui os seguintes relacionamentos:

```text
Conta 1 ───────── N Lançamento

Categoria 1 ───── N Lançamento
```

Representação simplificada:

```text
┌───────────────┐
│     Conta     │
└───────┬───────┘
        │
       1:N
        │
        ▼
┌───────────────┐
│  Lançamento   │
└───────┬───────┘
        │
       N:1
        │
        ▼
┌───────────────┐
│   Categoria   │
└───────────────┘
```

Fluxo de consolidação:

```text
Lançamentos
     │
     ▼
Fechamento
     │
     ▼
Conciliação
     │
     ▼
Extrato
```

---

## 📋 Regras de negócio

### RN01 — Conta possui saldo

Toda conta deve possuir um saldo que represente sua situação financeira.

### RN02 — Lançamento possui valor

Todo lançamento deve possuir um valor financeiro válido.

### RN03 — Lançamento possui categoria

Todo lançamento deve estar associado a uma categoria.

### RN04 — Categoria pode possuir vários lançamentos

Uma mesma categoria pode ser utilizada em diferentes lançamentos.

### RN05 — Conta pode possuir vários lançamentos

Uma conta pode possuir diversos lançamentos financeiros.

### RN06 — Fechamento consolida um período

O fechamento deve trabalhar com os lançamentos correspondentes ao período analisado.

### RN07 — Conciliação verifica os valores

A conciliação deve comparar os valores envolvidos e identificar divergências.

### RN08 — Extrato representa um período

O extrato deve apresentar um resumo coerente das informações financeiras do período.

---

## 🧩 Decisões de modelagem

### Lançamento em vez de Movimentação

Durante a evolução do projeto, o conceito inicialmente chamado de `Movimentacao` foi ajustado para `Lancamento`.

A alteração acompanha a nomenclatura utilizada no domínio trabalhado na disciplina e na proposta da primeira entrega.

```text
Movimentacao
      ↓
Lancamento
```

---

### Categoria como entidade

Categorias como `Alimentação`, `Transporte` ou `Moradia` não são classes independentes.

Elas são instâncias da entidade `Categoria`.

```python
Categoria("Alimentação")
Categoria("Transporte")
Categoria("Moradia")
```

Essa abordagem evita a criação de classes desnecessárias.

---

### Conciliação como classe própria

`Conciliacao` será representada como uma classe independente de `Fechamento`.

As responsabilidades são diferentes:

```text
Fechamento
→ consolida informações de um período

Conciliacao
→ verifica a correspondência dos valores
```

Manter as responsabilidades separadas torna o modelo mais organizado e facilita a implementação e os testes.

---

### Fechamento e os lançamentos

O tratamento dos lançamentos utilizados pelo `Fechamento` será definido durante a implementação.

A decisão adotada deverá ser documentada no projeto, considerando se os objetos serão **referenciados ou copiados** e qual o impacto dessa escolha no domínio.

---

## 🧪 Testes

O projeto utilizará **pytest** para realizar os testes automatizados.

Os testes deverão verificar tanto situações esperadas quanto situações de erro.

Entre os comportamentos que deverão ser testados:

- [ ] Criação de uma conta
- [ ] Criação de uma categoria
- [ ] Criação de um lançamento
- [ ] Associação entre lançamento e categoria
- [ ] Associação entre lançamento e conta
- [ ] Validação dos valores
- [ ] Funcionamento do fechamento
- [ ] Conciliação válida
- [ ] Conciliação com divergência
- [ ] Geração do extrato
- [ ] Situações sem lançamentos

---

## 📁 Estrutura do projeto

```text
e-finance/
│
├── finance/
│   ├── __init__.py
│   ├── conta.py
│   ├── categoria.py
│   ├── lancamento.py
│   ├── fechamento.py
│   ├── conciliacao.py
│   └── extrato.py
│
├── tests/
│   ├── __init__.py
│   ├── test_conta.py
│   ├── test_categoria.py
│   ├── test_lancamento.py
│   ├── test_fechamento.py
│   ├── test_conciliacao.py
│   └── test_extrato.py
│
├── README.md
└── pyproject.toml
```

---

## 📚 Evolução do projeto

O desenvolvimento do e-Finance ocorre de forma incremental.

### Módulo 1 — Domínio e primeiras entidades

Nesta etapa são trabalhados:

- Identificação do problema;
- Análise do domínio;
- Identificação das entidades;
- Definição dos atributos;
- Relacionamentos;
- Responsabilidades;
- Implementação inicial;
- Testes das entidades.

Entidades principais:

```text
Conta
Categoria
Lancamento
```

---

### Módulo 2 — Evolução do domínio

Com a evolução do sistema, novas responsabilidades são incorporadas:

```text
Conta
Categoria
Lancamento
      ↓
Fechamento
      ↓
Conciliacao
      ↓
Extrato
```

Essa evolução permite aplicar conceitos de colaboração entre objetos, responsabilidades e decisões de projeto.

---

## 🛠️ Tecnologias

- **Python**
- **Programação Orientada a Objetos**
- **pytest**
- **Git**
- **GitHub**

---
## 🚧 Status do projeto

**Primeira versão do domínio implementada.**

### Domínio

- [x] Identificação do problema
- [x] Identificação dos conceitos
- [x] Definição das entidades
- [x] Definição dos relacionamentos
- [x] Definição das responsabilidades
- [x] Definição das regras de negócio

### Implementação

- [x] `Conta`
- [x] `Categoria`
- [x] `Lancamento`
- [x] `Fechamento`
- [x] `Conciliacao`
- [x] `Extrato`

### Testes

- [x] Testes de `Conta`
- [x] Testes de `Categoria`
- [x] Testes de `Lancamento`
- [x] Testes de `Fechamento`
- [x] Testes de `Conciliacao`
- [x] Testes de `Extrato`
- [x] Testes de regras de negócio
- [x] Testes de situações inválidas

---

## 📖 Documentação

A documentação do domínio apresenta o processo de análise e modelagem utilizado para construir o e-Finance.

O projeto será atualizado conforme novas etapas da disciplina forem implementadas.

---

## 👨‍💻 Autor

**Rafael França**

Projeto desenvolvido para a disciplina de **Programação Orientada a Objetos II**.

---

> 🚧 **e-Finance — Projeto acadêmico em desenvolvimento.**
