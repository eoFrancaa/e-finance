from datetime import date

class Fechamento:
    def __init__(self, data:date, saldo_inicial: float, saldo_final: float):
        self.data = data
        self.saldo_inicial = saldo_inicial
        self.saldo_final = saldo_final