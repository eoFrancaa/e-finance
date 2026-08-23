from finance.fechamento import Fechamento


class Conciliacao:
    def __init__(self, fechamento: Fechamento):
        self.fechamento = fechamento

    def esta_conciliado(self) -> bool:
        return self.fechamento.saldo() == 0.0