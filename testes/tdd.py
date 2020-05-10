"""
Escrevemos primeiro o teste e os cenários desejados
Teremos um estado RED, pois não há implementação para isso
Implementamos oque queremos
Executamos o teste novamente
O Teste deve passar

Para executar o teste, em um terminal executar o seguinte comando:
    -> python -m doctest -v testes/tdd.py

Não é a melhor forma de testar este codigo, pois precisamos escrever
o resultado esperado pelo console, qualquer coisa diferente gera erro
"""


def duplicar(lista):
    """ Duplica valores em uma lista

    >>> duplicar([1, 2, 3])
    [2, 4, 6]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']
    """
    return [2 * x for x in lista]
