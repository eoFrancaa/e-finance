from datetime import date

from finance.conta import Conta
from finance.categoria import Categoria


class Lancamento:
    def __init__(self, descricao: str, valor: float, data: date, conta: Conta, categoria: Categoria):
        self.descricao = descricao
        self.valor = valor
        self.data = data
        self.conta = conta
        self.categoria = categoria  