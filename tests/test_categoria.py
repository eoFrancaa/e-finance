import pytest

from finance.categoria import Categoria


def test_nao_deve_criar_categoria_sem_nome():
    with pytest.raises(ValueError):
        Categoria("")


def test_nao_deve_criar_categoria_sem_nome():
    with pytest.raises(ValueError):
        Categoria("")