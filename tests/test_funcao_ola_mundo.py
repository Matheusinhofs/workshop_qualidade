from app.func import funcao_ola_povo

def test_funcao_ola_povo_retorna_ola_povo():
    saida = funcao_ola_povo()
    gabarito = "Oi meu povo"
    assert saida == gabarito

