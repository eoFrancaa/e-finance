# e-Finance

Sistema de controle financeiro desenvolvido para a disciplina de Programação Orientada a Objetos II.

O projeto tem como objetivo aplicar conceitos de orientação a objetos na construção de um domínio financeiro, utilizando classes, responsabilidades, relacionamentos entre objetos, regras de negócio e testes automatizados.

## Objetivo

O e-Finance representa um domínio financeiro capaz de:

- Representar contas financeiras;
- Organizar lançamentos por categorias;
- Registrar créditos e débitos;
- Realizar o fechamento de lançamentos;
- Calcular créditos, débitos e saldo;
- Realizar a conciliação financeira;
- Gerar informações de extrato;
- Validar regras de negócio;
- Testar os comportamentos do domínio.

---

## Domínio

O domínio principal do sistema é composto pelas seguintes classes:

- `Conta`
- `Categoria`
- `Lancamento`
- `Fechamento`
- `Conciliacao`
- `Extrato`

### Relacionamento entre os objetos

```text
Conta
  │
  └──── 1:N ────> Lancamento
                       │
                       └──── N:1 ────> Categoria

Lancamento
    │
    ▼
Fechamento
    │
    ├──────────> Conciliacao
    │
    └──────────> Extrato
```

---

# Classes do domínio

## Conta

Representa uma conta financeira.

### Atributos

- `nome`
- `saldo`

### Regras

- O nome da conta é obrigatório;
- O saldo não pode ser negativo.

### Exemplo

```python
conta = Conta("Conta Corrente", 1000.0)
```

---

## Categoria

Representa a categoria utilizada para classificar um lançamento financeiro.

### Exemplo

```python
categoria = Categoria("Alimentação")
```

### Regra

O nome da categoria é obrigatório.

---

## Lancamento

Representa uma movimentação financeira associada a uma conta e a uma categoria.

### Atributos

- `descricao`
- `valor`
- `data`
- `conta`
- `categoria`
- `tipo`

### Tipos

O domínio trabalha com dois tipos:

- `CREDITO`
- `DEBITO`

No código:

```python
Lancamento.CREDITO
Lancamento.DEBITO
```

### Regras

- A descrição é obrigatória;
- O valor deve ser maior que zero;
- O tipo deve ser `CREDITO` ou `DEBITO`;
- O lançamento pertence a uma conta;
- O lançamento pertence a uma categoria.

### Exemplo

```python
lancamento = Lancamento(
    "Salário",
    5000.0,
    data,
    conta,
    categoria,
    Lancamento.CREDITO
)
```

---

# Fechamento

A classe `Fechamento` é responsável por consolidar um conjunto de lançamentos.

Ela fornece os seguintes comportamentos:

```python
total_creditos()
total_debitos()
saldo()
```

O saldo é calculado através da regra:

```text
saldo = total de créditos - total de débitos
```

### Exemplo

```text
Créditos: R$ 5.000,00
Débitos:  R$ 2.000,00
Saldo:    R$ 3.000,00
```

### Fechamento sem lançamentos

Quando não existem lançamentos:

```text
Total de créditos = R$ 0,00
Total de débitos  = R$ 0,00
Saldo             = R$ 0,00
```

Essa situação possui teste automatizado.

---

# Conciliação

A classe `Conciliacao` é responsável por verificar se um fechamento está conciliado.

A regra utilizada é:

```text
saldo == 0
```

Quando os créditos e débitos são iguais:

```text
Créditos = Débitos
      ↓
Saldo = 0
      ↓
Conciliado
```

Quando existe divergência:

```text
Créditos != Débitos
      ↓
Saldo != 0
      ↓
Não conciliado
```

O método utilizado é:

```python
esta_conciliado()
```

### Decisão de projeto

A `Conciliacao` foi implementada como uma classe própria para separar a responsabilidade de verificar a consistência financeira da responsabilidade de consolidar os lançamentos realizada pelo `Fechamento`.

Dessa forma:

- `Fechamento` consolida os lançamentos;
- `Conciliacao` verifica a consistência;
- `Extrato` apresenta os resultados.

---

# Extrato

A classe `Extrato` utiliza um `Fechamento` para apresentar os resultados financeiros consolidados.

Ela disponibiliza:

```python
total_creditos()
total_debitos()
saldo()
```

O `Extrato` não realiza novamente os cálculos. Ele utiliza as informações fornecidas pelo `Fechamento`.

---

# Regras de negócio

## Conta

```text
- Nome obrigatório;
- Saldo não pode ser negativo.
```

## Categoria

```text
- Nome obrigatório.
```

## Lancamento

```text
- Descrição obrigatória;
- Valor maior que zero;
- Tipo deve ser CREDITO ou DEBITO.
```

## Fechamento

```text
- Créditos = soma dos lançamentos do tipo CREDITO;
- Débitos = soma dos lançamentos do tipo DEBITO;
- Saldo = créditos - débitos.
```

## Conciliação

```text
- Saldo igual a zero → conciliado;
- Saldo diferente de zero → não conciliado.
```

---

# Decisões de implementação

## Referência dos lançamentos

O `Fechamento` recebe os lançamentos e mantém uma referência à coleção fornecida.

Não são criadas cópias dos objetos `Lancamento`.

Essa decisão foi adotada porque o fechamento trabalha sobre os próprios objetos do domínio e não necessita criar versões independentes dos lançamentos.

## Responsabilidade das classes

As responsabilidades foram distribuídas entre os objetos do domínio.

```text
Conta
└── Representa a conta financeira

Categoria
└── Classifica lançamentos

Lancamento
└── Representa uma movimentação financeira

Fechamento
├── Calcula créditos
├── Calcula débitos
└── Calcula saldo

Conciliacao
└── Verifica se o fechamento está conciliado

Extrato
└── Apresenta os resultados do fechamento
```

A intenção é evitar concentrar todas as regras em uma única classe.

---

# Testes

O projeto utiliza `pytest` para os testes automatizados.

Os testes verificam tanto comportamentos válidos quanto situações inválidas.

## Testes de Conta

- Criação e validação de conta;
- Conta sem nome;
- Conta com saldo negativo.

## Testes de Categoria

- Criação e validação de categoria;
- Categoria sem nome.

## Testes de Lancamento

- Criação de lançamento;
- Lançamento com valor negativo;
- Lançamento com tipo inválido.

## Testes de Fechamento

- Cálculo de créditos;
- Cálculo de débitos;
- Cálculo do saldo;
- Fechamento sem lançamentos.

## Testes de Conciliação

- Fechamento conciliado;
- Fechamento com divergência.

## Testes de Extrato

- Geração das informações do extrato.

## Teste do fluxo completo

O projeto também possui um teste que percorre o fluxo principal do domínio:

```text
Conta
  ↓
Categoria
  ↓
Lancamento
  ↓
Fechamento
  ↓
Conciliacao
  ↓
Extrato
```

---

# Execução dos testes

Para executar os testes, utilize:

```bash
python3 -m pytest -v
```

Resultado atual:

```text
14 passed
```

Isso significa:

```text
14 testes executados
14 testes aprovados
0 testes falhos
```

---

# Estrutura do projeto

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
│   ├── test_categoria.py
│   ├── test_conciliacao.py
│   ├── test_conta.py
│   ├── test_fechamento.py
│   ├── test_fluxo_financeiro.py
│   └── test_lancamento.py
│
├── pyproject.toml
└── README.md
```

---

# Fluxo principal

O fluxo principal do domínio é:

```text
1. Criar uma Conta
       ↓
2. Criar Categorias
       ↓
3. Registrar Lançamentos
       ↓
4. Realizar o Fechamento
       ↓
5. Calcular créditos, débitos e saldo
       ↓
6. Realizar a Conciliação
       ↓
7. Gerar o Extrato
```

### Exemplo

```text
Conta Corrente
      │
      ├── Salário ........ R$ 5.000,00 → CREDITO
      │
      ├── Mercado ........ R$   500,00 → DEBITO
      │
      └── Aluguel ........ R$ 1.500,00 → DEBITO
                         │
                         ▼
                    Fechamento
                         │
                  Saldo = R$ 3.000
                         │
                         ▼
                       Extrato
```

---

# Status do projeto

## Domínio

- [x] Identificação das entidades
- [x] Definição dos relacionamentos
- [x] Definição das responsabilidades
- [x] Definição das regras de negócio
- [x] Definição das decisões de implementação

## Implementação

- [x] `Conta`
- [x] `Categoria`
- [x] `Lancamento`
- [x] `Fechamento`
- [x] `Conciliacao`
- [x] `Extrato`

## Testes

- [x] Testes unitários
- [x] Testes de regras de negócio
- [x] Testes de situações inválidas
- [x] Teste de fechamento sem lançamentos
- [x] Testes de conciliação
- [x] Teste do fluxo completo
- [x] 14 testes aprovados

---

# Tecnologias utilizadas

- Python
- pytest
- Git
- GitHub

---

# Contexto acadêmico

Projeto desenvolvido para aplicação prática dos conceitos de Programação Orientada a Objetos II, com foco em:

- Modelagem de domínio;
- Classes e objetos;
- Encapsulamento;
- Responsabilidade dos objetos;
- Colaboração entre objetos;
- Regras de negócio;
- Testes automatizados;
- Organização de código Python.

---

# Autor

**Rafael França**

Projeto acadêmico — e-Finance.
