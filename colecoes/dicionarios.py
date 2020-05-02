"""
São coleções do tipo chave/valor
São representadas por {}
Tanto chavel quanto valor podem ser dinamicos
Nãos há chaves repetidas
"""

dicionario = {
    "item1": "teste",
    2: 2.99,
    False: True,
    (1, 2, 3): {
        1: 1,
        2: 2,
        3: 3
    }
}
print(dir(dicionario))
print(type(dicionario))
print(dicionario)

dicionario2 = dict(nome='Alex', sobrenome='Volnei Galante', idade=28)
print(dicionario2)

print("acessando elemento")
print(dicionario["item1"])
print(dicionario.get("item"))  # caso valor não exista retorna None
print(dicionario.get("item", "Chave não encontrada"))
for chave, valor in dicionario.items():
    print(f'{chave} - {valor}')

print("verificando se item existe na lista")
print("item2" in dicionario)  # busca pela chave
print("item" in dicionario)
print("teste" in dicionario)

print("acessando as chaves")
for key in dicionario.keys():
    print(key)

print("acessando as chaves")
for value in dicionario.values():
    print(value)

print("adicionando/alterando item ao dicionario")
dicionario["teste"] = "testando"
print(dicionario)

dicionario.update({"teste": "testamento"})
print(dicionario)

print("removendo item ao dicionario")
dicionario.pop("teste")
del dicionario[(1, 2, 3)]
print(dicionario)

print("limpando dicionario")
dicionario3 = {1: 2, 3: 4, 5: 6}
print(dicionario3)
dicionario3.clear()
print(dicionario3)

print("criando multiplas chaves")
dicionario4 = {}.fromkeys(["item1", "item2", "item3"], "teste")
print(dicionario4)

print("operações")
numeros = {'num1': 999.99, 'num2': 888.88, 'num3': 777.7}
print(sum(numeros.values()))
print(max(numeros.values()))
print(min(numeros.values()))
print(len(numeros))

# comprehensions
numeros = {'a': 1, 'b': 2, 'c': 4, 'd': 5}
quadrados = {chave: valor ** 2 for chave, valor in numeros.items()}
print(numeros)
print(quadrados)

chaves = 'abcd'
valores = [1, 2, 3, 4]

dicionario = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(dicionario)

print({numero: ('par' if numero % 2 == 0 else 'impar')
       for numero in range(1, 100)})
