class Categoria:
    def __init__(self, nome: str):
        if not nome:
            raise ValueError("O nome da categoria é obrigatório.")

        self.nome = nome