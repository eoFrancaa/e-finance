from datetime import date

from finance.conta import Conta
from finance.categoria import Categoria
from finance.lancamento import Lancamento
from finance.fechamento import Fechamento
from finance.conciliacao import Conciliacao
from finance.extrato import Extrato


def test_fluxo_completo_financeiro():
    # 1. Criação da conta
    conta = Conta("Conta Corrente", 1000.0)

    # 2. Criação das categorias
    categoria_salario = Categoria("Salário")
    categoria_alimentacao = Categoria("Alimentação")
    categoria_moradia = Categoria("Moradia")

    # 3. Registro dos lançamentos
    salario = Lancamento(
        "Salário",
        5000.0,
        date(2026, 8, 22),
        conta,
        categoria_salario,
        Lancamento.CREDITO
    )

    alimentacao = Lancamento(
        "Mercado",
        500.0,
        date(2026, 8, 22),
        conta,
        categoria_alimentacao,
        Lancamento.DEBITO
    )

    aluguel = Lancamento(
        "Aluguel",
        1500.0,
        date(2026, 8, 22),
        conta,
        categoria_moradia,
        Lancamento.DEBITO
    )

    # 4. Fechamento dos lançamentos
    fechamento = Fechamento([
        salario,
        alimentacao,
        aluguel
    ])

    # 5. Verificação dos valores do fechamento
    assert fechamento.total_creditos() == 5000.0
    assert fechamento.total_debitos() == 2000.0
    assert fechamento.saldo() == 3000.0

    # 6. Conciliação
    conciliacao = Conciliacao(fechamento)

    # Como os créditos e débitos não são iguais,
    # o fechamento não está conciliado.
    assert conciliacao.esta_conciliado() is False

    # 7. Geração do extrato
    extrato = Extrato(fechamento)

    assert extrato.total_creditos() == 5000.0
    assert extrato.total_debitos() == 2000.0
    assert extrato.saldo() == 3000.0



def test_fluxo_completo_com_conciliacao():
    conta = Conta("Conta Corrente", 1000.0)

    salario = Lancamento(
        "Salário",
        5000.0,
        date(2026, 8, 22),
        conta,
        Categoria("Salário"),
        Lancamento.CREDITO
    )

    despesas = Lancamento(
        "Despesas",
        5000.0,
        date(2026, 8, 22),
        conta,
        Categoria("Despesas"),
        Lancamento.DEBITO
    )

    fechamento = Fechamento([
        salario,
        despesas
    ])

    conciliacao = Conciliacao(fechamento)

    assert fechamento.total_creditos() == 5000.0
    assert fechamento.total_debitos() == 5000.0
    assert fechamento.saldo() == 0.0
    assert conciliacao.esta_conciliado() is True