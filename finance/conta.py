from finance.usuario import Usuario

class Conta:
    def __init__(self, usuario: Usuario, saldo: float = 0.0):
        self.usuario = usuario
        self.saldo = saldo

        usuario.adicionar_conta(self)