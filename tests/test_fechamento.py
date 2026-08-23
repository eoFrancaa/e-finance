from datetime import date

from finance.conta import Conta
from finance.categoria import Categoria
from finance.lancamento import Lancamento
from finance.fechamento import Fechamento


def test_deve_calcular_total_de_creditos():
    conta = Conta("Conta Corrente", 0.0)
    categoria = Categoria("Salário")

    salario = Lancamento(
        "Salário",
        5000.0,
        date(2026, 8, 22),
        conta,
        categoria,
        "CREDITO"
    )

    fechamento = Fechamento([salario])

    assert fechamento.total_creditos() == 5000.0


def test_deve_calcular_total_debitos():
    conta = Conta("Conta Corrente", 0.0)
    categoria = Categoria("Alimentação")

    almoco = Lancamento(
        "Almoço",
        50.0,
        date(2026, 8, 22),
        conta,
        categoria,
        "DEBITO"
    )

    fechamento = Fechamento([almoco])

    assert fechamento.total_debitos() == 50.0


def test_deve_calcular_saldo():
    conta = Conta("Conta Corrente", 0.0)

    salario = Lancamento(
        "Salário",
        5000.0,
        date(2026, 8, 22),
        conta,
        Categoria("Salário"),
        "CREDITO"
    )

    aluguel = Lancamento(
        "Aluguel",
        1200.0,
        date(2026, 8, 22),
        conta,
        Categoria("Moradia"),
        "DEBITO"
    )

    fechamento = Fechamento([salario, aluguel])

    assert fechamento.total_creditos() == 5000.0
    assert fechamento.total_debitos() == 1200.0
    assert fechamento.saldo() == 3800.0


def test_fechamento_sem_lancamentos():
    fechamento = Fechamento([])

    assert fechamento.total_creditos() == 0.0
    assert fechamento.total_debitos() == 0.0
    assert fechamento.saldo() == 0.0