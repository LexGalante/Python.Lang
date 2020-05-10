"""
assertion -> keyword para checagem
"""


# com doctest precisamos escrever a expectativa do resultado no console
def divide(num1, num2):
    """divide dois numeros

    >>> divide(1, 2)
    0.5

    >>> divide(5,5)
    100
    """
    assert num1 > 0 and num2 > 0, 'Não pode haver zeros na divisão'
    return num1 / num2


print(divide(1, 2))
