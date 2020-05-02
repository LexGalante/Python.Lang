"""
Lista de alta performance
Coloca os valores como chave e o os valores são o numero de vezes que o mesmo aparece
"""
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import namedtuple

print("counter")
lista = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 6, 7, 8, 9]
counter = Counter(lista)
print(dir(lista))
print(lista)

print(dir(counter))
print(counter)

counter = Counter("Alex Volnei Galante")
print(dir(counter))
print(counter)
print(counter.most_common(3))

print("defaultdict")
dicionario = defaultdict(lambda: "testando")
print(type(dicionario))
print(dir(dicionario))
dicionario["teste"] = "testando"
print(dicionario["nao_existess"])

print("ordereddict")
dicionario = {'a': 1, 'b': 2, 'd': 3, 'z': 4, 'c': 5}
for chave, valor in dicionario.items():
    print(f"{chave} {valor}")

dicionario = OrderedDict({'a': 1, 'b': 2, 'd': 3, 'z': 4, 'c': 5})
for chave, valor in dicionario.items():
    print(f"{chave} {valor}")

print("namedtuple")
tupla_nomeada = namedtuple('teste', 'item1 item2 item3')
tupla_nomeada = namedtuple('teste', 'item1, item2, item3')
tupla_nomeada = namedtuple('teste', ['item1', 'item2', 'item3'])

primeiro = tupla_nomeada(item1="teste", item2="teste", item3="teste")

print(primeiro)
