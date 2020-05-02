"""
Listas
Vetores e matrizes em python
São dinâmicas
QUALQUER tipo de dado pode ser inserido
não possuem tamanho fixo
"""
print('metodos da lista')
lista = ['a', 'b', 'c', 'd']
print(dir(lista))
print(lista)

print('adicionando item')
lista[2] = 'z'
lista.append('e')
lista.insert(3, 'x')
print(lista)

print('removendo item')
lista.remove('a')
del lista[2]
lista.pop()
print(lista)

print('clonando lista')
lista2 = lista.copy()
print(lista2)

print('contando items')
print(len(lista))

print('adicionando lista a lista original')
lista.extend(['g', 'h', 'i', 'a', 'a', 'a', 'a', 'a', 1, 2, 3, False, 5.5])
print(lista.count('a'))

print('indice especifico')
print(lista.index('d'))

print('juntando duas lista')
lista3 = list(range(11))
lista += lista3
print(lista)

print('calculos com lista')
lista4 = list((3, 4, 5, 6))
lista4 = lista4 * 4
print(lista4)

print('acessando item da lista')
print(lista[0])
print(lista[-1])
print(lista.index(1))
print(lista[4:6])
print(lista[:7])
print(lista[7:])

print('ordenando lista')
lista6 = [45.8, 33.8, 77.6, 10989.99, 1.99999999999999]
lista6.sort()
print(lista6)

print('iterando sobre lista')
for item in lista:
    print(item)
lista.reverse()
iterador = 0
while iterador != len(lista):
    print(lista[iterador])
    iterador += 1
# indexação      0      1      2     3
lista_index = [False, 1.29, "Teste", 6]

print('tipos de acesso a items -> lista[inicio:fim:passo]')
lista7 = list((range(100)))
print(lista7[1:10:2])
print(lista7[10::])  # da posicao 10 ate o final de 1 em 1
print(lista7[:10:])  # da posicao 0 ate 10 de 1 em 1
print(lista7[::10])  # da posicao 0 ate 100 de 10 em 10

lista = list((range(1000)))
print('metodo sum')
print(sum(lista))

print('metodo max')
print(max(lista))

print('metodo min')
print(min(lista))

print('desatribuição de lista')
lista = [1, 2, False]
num1, num2, bool3 = lista  # precisa ser exatamente igual
print(num1)
print(num2)
print(bool3)

# comprehension
numeros = range(0, 11)
multiplicacao = [numero * 10 for numero in numeros]
divisao = [numero / 1 for numero in numeros]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
processamento = [numero * 2 if numero %
                 2 == 0 else numero * 2 for numero in numeros]

print(numeros)
print(multiplicacao)
print(divisao)
print(pares)
print(impares)
print(processamento)
print([palavra.upper() for palavra in 'alex volnei galante'.split(' ')])

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[0])
print(matriz[2][1])
print([[print(valor) for valor in lista] for lista in matriz])
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)
