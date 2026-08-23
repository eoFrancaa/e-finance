class Conta:
    def __init__(self, nome: str, saldo: float = 0.0):
        if not nome:
            raise ValueError("O nome da conta é obrigatório.")

        if saldo < 0:
            raise ValueError("O saldo não pode ser negativo.")

        self.nome = nome
        self.saldo = saldo