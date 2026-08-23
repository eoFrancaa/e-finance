from datetime import date

from finance.conta import Conta
from finance.categoria import Categoria
from finance.lancamento import Lancamento
from finance.fechamento import Fechamento
from finance.conciliacao import Conciliacao


def test_deve_conciliar_quando_creditos_e_debitos_sao_iguais():
    conta = Conta("Conta Corrente", 0.0)

    credito = Lancamento(
        "Salário",
        5000.0,
        date(2026, 8, 22),
        conta,
        Categoria("Salário"),
        "CREDITO"
    )

    debito = Lancamento(
        "Despesas",
        5000.0,
        date(2026, 8, 22),
        conta,
        Categoria("Despesas"),
        "DEBITO"
    )

    fechamento = Fechamento([credito, debito])
    conciliacao = Conciliacao(fechamento)

    assert conciliacao.esta_conciliado() is True


def test_nao_deve_conciliar_quando_existe_divergencia():
    conta = Conta("Conta Corrente", 0.0)

    credito = Lancamento(
        "Salário",
        5000.0,
        date(2026, 8, 22),
        conta,
        Categoria("Salário"),
        "CREDITO"
    )

    debito = Lancamento(
        "Despesas",
        4500.0,
        date(2026, 8, 22),
        conta,
        Categoria("Despesas"),
        "DEBITO"
    )

    fechamento = Fechamento([credito, debito])
    conciliacao = Conciliacao(fechamento)

    assert conciliacao.esta_conciliado() is False