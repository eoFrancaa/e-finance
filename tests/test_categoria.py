from finance.categoria import Categoria

def test_criar_categoria():
    c = Categoria("Categoria Teste")
    assert c.nome == "Categoria Teste"