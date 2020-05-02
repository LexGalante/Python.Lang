"""
Teoria dos conjuntos
Não possuem valores duplicados
Não possuem valores ordenados
Não possui indice
Otimo para calculos
Muito performatico
"""

conjunto = {3, 6.66, 9.80}
# valores duplicados são ignorados
conjunto2 = set({1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7})
print(dir(conjunto))
print(conjunto)
print(conjunto2)

print("verificando se um elemento existe no conjunto")
if 6.66 in conjunto:
    print("6.66 existe no conjunto")

print("adicionando no conjunto")
conjunto.add(5.4444)
print(conjunto)

print("removendo no conjunto")
conjunto.remove(5.4444)
print(conjunto)

# comprehensions
conjunto = {numero for numero in range(1, 10)}
quadrado = {numero ** 2 for numero in conjunto}
dicionario = {numero: numero ** 2 for numero in conjunto}

print(conjunto)
print(quadrado)
print(dicionario)
