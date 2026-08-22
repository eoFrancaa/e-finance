from finance import conta

def test_criar_conta():
    c = conta.Conta("Conta Teste", 100.0)
    assert c.nome == "Conta Teste"
    assert c.saldo == 100.0 