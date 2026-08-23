import pytest

from finance.conta import Conta


def test_nao_deve_criar_conta_sem_nome():
    with pytest.raises(ValueError):
        Conta("")


def test_nao_deve_criar_conta_com_saldo_negativo():
    with pytest.raises(ValueError):
        Conta("Conta Corrente", -100.0)