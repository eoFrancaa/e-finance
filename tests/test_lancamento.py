from datetime import date

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
        categoria
    )

    assert lancamento.descricao == "Almoço"
    assert lancamento.valor == 50.0
    assert lancamento.data == date(2026, 8, 22)
    assert lancamento.conta == conta
    assert lancamento.categoria == categoria