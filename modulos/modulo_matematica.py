from statistics import mean
from statistics import median


def soma(numeros):
    """Calcula a soma dos itens"""
    if type(numeros) is not list:
        raise TypeError("parametro NUMEROS deve ser (list,tuple,set)")
    return sum(numeros)


def media(numeros):
    if type(numeros) is not list:
        raise TypeError("parametro NUMEROS deve ser (list,tuple,set)")
    return mean(numeros)


def mediana(numeros):
    if type(numeros) is not list:
        raise TypeError("parametro NUMEROS deve ser (list,tuple,set)")
    return median(numeros)
