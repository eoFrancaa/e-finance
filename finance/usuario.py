class Usuario:
    def __intit__(self, nome:str, email:str, senha:str):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)


    