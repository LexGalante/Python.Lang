"""
Iterable -> iteraveis
Iterator -> possibilidade de usar a funcao next(iterator)
"""
from iterador import foreach
from contador import Contador

texto = "Texto..."  # iterable
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(texto)
print(numeros)
iterador_texto = iter(texto)  # iterator
print(next(iterador_texto))
print(next(iterador_texto))
print(next(iterador_texto))
print(next(iterador_texto))
# ao usarmos um for, o python atribui a funcao iter() ao iterable e controla o next()
print(foreach([1, 2, 3, 4, 5, 6, 7, 8, 9]))
contador = Contador(1, 100)
print(type(contador))
print(type(iter(contador)))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
