"""
Tipos de armazenamento em memoria:
    STACK -> armazenam as referencias
    HEAP -> armazenam os valores
"""
import sys


# em python valores iguais tem a mesma referencia
x = 10
y = 10

if(id(x) == id(y)):
    print("x & y referenciam ao mesmo objeto")

print(id(x))
print(id(y))
print(sys.getrefcount(x))
print(sys.getrefcount(y))
x += 1
# agora as referencias são diferentes
print(id(x))
print(id(y))
print(sys.getrefcount(x))
print(sys.getrefcount(y))


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa("alex", "galante")
p2 = p1
print(f"p1: {id(p1)}")
print(f"p2: {id(p2)}")
print(sys.getrefcount(p1))
print(sys.getrefcount(p2))
