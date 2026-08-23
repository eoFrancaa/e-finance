from datetime import date

from finance.conta import Conta
from finance.categoria import Categoria


class Lancamento:
    CREDITO = "CREDITO"
    DEBITO = "DEBITO"

    TIPOS_VALIDOS = {CREDITO, DEBITO}

    def __init__(self,descricao: str,valor: float, data: date,conta: Conta,categoria: Categoria,tipo: str):
        if not descricao:
            raise ValueError("A descrição do lançamento é obrigatória.")

        if valor <= 0:
            raise ValueError("O valor do lançamento deve ser maior que zero.")

        if tipo not in self.TIPOS_VALIDOS:
            raise ValueError("O tipo deve ser CREDITO ou DEBITO.")

        self.descricao = descricao
        self.valor = valor
        self.data = data
        self.conta = conta
        self.categoria = categoria
        self.tipo = tipo