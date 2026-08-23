from finance.lancamento import Lancamento


class Fechamento:
    def __init__(self, lancamentos: list[Lancamento]):
        self.lancamentos = lancamentos

    def total_creditos(self) -> float:
        return sum(
            lancamento.valor
            for lancamento in self.lancamentos
            if lancamento.tipo == "CREDITO"
        )

    def total_debitos(self) -> float:
        return sum(
            lancamento.valor
            for lancamento in self.lancamentos
            if lancamento.tipo == "DEBITO"
        )

    def saldo(self) -> float:
        return self.total_creditos() - self.total_debitos()