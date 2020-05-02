"""
Exceto adição ou remoção todos os outros metodos vistos em listas.py estão disponiveis para tuplas
São imutaveis, cada alteração cria uma nova tupla, porem são definidas pelo ,
São represetadas por ()
"""
tupla = (1, 2, 4, 5, 6, 7, 8, 9)
print(type(tupla))

tupla2 = 5, 3, 2, 1
print(type(tupla2))

tupla3 = tuple(range(0, 10))
print(tupla3)
