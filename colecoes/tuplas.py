"""
Exceto adição ou remoção todos os outros metodos vistos em listas.py estão disponiveis para tuplas
São imutaveis, cada alteração cria uma nova tupla, porem são definidas pelo ,
São represetadas por ()
"""
from sys import getsizeof

tupla = (1, 2, 4, 5, 6, 7, 8, 9)
print(type(tupla))

tupla2 = 5, 3, 2, 1
print(type(tupla2))

tupla3 = tuple(range(0, 10))
print(tupla3)

print(tuple(reversed((9, 5, 4, 3, 2, 1, 8))))

# Generators
# similar aos comprehension, porém com menos memoria mais limitações
salarios = [5.575, 3.499, 1731.22, 677.00, 4.400, 2231.88,
            10031.88, 1031.72, 431.22, 18573.21, 65700.55]
generator = any(salario <= 1088 for salario in salarios)
comprehension = any([salario <= 1088 for salario in salarios])
print(generator)
print(comprehension)
# comparando a quantidade de bytes em memoria do elemento
print(getsizeof(generator))
print(getsizeof(comprehension))
