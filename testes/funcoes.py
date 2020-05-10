from statistics import mean
from statistics import median


def soma(numeros):
    """Calcula a soma dos itens"""
    if type(numeros) is not list:
        raise TypeError("parametro NUMEROS deve ser lista")
    if len(numeros) is 0:
        raise ValueError("a lista de numeros não pode estar vazia")
    return sum(numeros)


def media(numeros):
    if type(numeros) is not list:
        raise TypeError("parametro NUMEROS deve ser lista")
    if len(numeros) is 0:
        raise ValueError("a lista de numeros não pode estar vazia")
    return mean(numeros)


def mediana(numeros):
    if type(numeros) is not list:
        raise TypeError("parametro NUMEROS deve ser lista")
    if len(numeros) is 0:
        raise ValueError("a lista de numeros não pode estar vazia")
    return median(numeros)
