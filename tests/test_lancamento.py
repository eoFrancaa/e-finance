from datetime import date

import pytest

from finance.conta import Conta
from finance.categoria import Categoria
from finance.lancamento import Lancamento


def test_deve_criar_lancamento():
    conta = Conta("Conta Corrente", 1000.0)
    categoria = Categoria("Alimentação")

    lancamento = Lancamento(
        "Almoço",
        50.0,
        date(2026, 8, 22),
        conta,
        categoria,
        "DEBITO"
    )

    assert lancamento.descricao == "Almoço"
    assert lancamento.valor == 50.0
    assert lancamento.data == date(2026, 8, 22)
    assert lancamento.conta == conta
    assert lancamento.categoria == categoria
    assert lancamento.tipo == "DEBITO"


def test_nao_deve_criar_lancamento_com_valor_negativo():
    conta = Conta("Conta Corrente", 1000.0)
    categoria = Categoria("Alimentação")

    with pytest.raises(ValueError):
        Lancamento(
            "Almoço",
            -50.0,
            date(2026, 8, 22),
            conta,
            categoria,
            "DEBITO"
        )


def test_nao_deve_criar_lancamento_com_tipo_invalido():
    conta = Conta("Conta Corrente", 1000.0)
    categoria = Categoria("Alimentação")

    with pytest.raises(ValueError):
        Lancamento(
            "Almoço",
            50.0,
            date(2026, 8, 22),
            conta,
            categoria,
            "INVALIDO"
        )