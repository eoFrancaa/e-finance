from finance.fechamento import Fechamento


class Extrato:
    def __init__(self, fechamento: Fechamento):
        self.fechamento = fechamento

    def total_creditos(self) -> float:
        return self.fechamento.total_creditos()

    def total_debitos(self) -> float:
        return self.fechamento.total_debitos()

    def saldo(self) -> float:
        return self.fechamento.saldo()