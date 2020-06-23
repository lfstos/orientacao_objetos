from live61.abstracao_de_dado import Fila


def test_adiciona_um_usuario_na_fila_do_supermercado():
    supermercado = Fila()
    supermercado.entrar('Fernando')
    assert supermercado.fila == ['Fernando']


def test_adiciona_dois_usuarios_na_fila_do_banco():
    banco = Fila()
    banco.entrar('Manon')
    banco.entrar('Ana Beatriz')
    assert banco.fila == ['Manon', 'Ana Beatriz']


def test_remove_um_usuario_da_fila_do_supermercado():
    supermercado = Fila()
    supermercado.entrar('Manon')
    supermercado.sair()
    assert supermercado.fila == []


def test_remove_tres_usuarios_da_fila_da_loterica():
    loterica = Fila()
    loterica.entrar('Manon')
    loterica.entrar('Fernando')
    loterica.entrar('Júlia Caroline')
    loterica.sair()
    loterica.sair()
    loterica.sair()
    assert loterica.fila == []
