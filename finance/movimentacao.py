from finance.conta import Conta
from finance.categoria import Categoria

class Movimentacao:
    def __init__(self, conta: Conta, tipo: str, valor: float, categoria: Categoria):
        self.conta = conta
        self.tipo = tipo
        self.valor = valor
        self.categoria = categoria

    

