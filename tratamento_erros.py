"""
Erros mais comuns

SyntaxError -> erro de sintaxe no script
NameError -> algo não foi definido
TypeError -> erros com conversoes etc...
IndexError -> tentiva de acessar indice invalido
KeyError -> acessando um colecionavel com uma chave inexistente 
AttributeError -> acessando um atributo inexistente em objeto
IdentationError -> o script não identado corretamente
"""
if True == False:
    # lançando nosso proprio erro mesmo que THROWN em outras linguagens
    raise OSError("Alguma coisa nao ta certa com seu computador")


def calcule(numeros):
    if type(numeros) is not list:
        raise TypeError("o parametro números deve ser uma lista")
    if len(numeros) == 0:
        raise ValueError("a lista de numeros não pode estar vazia")
    return sum(numeros)


# tratando erro generico
try:
    calcule("vai da erro")
except:
    print("Ocorreu um erro inesperado")

# tratando erro especifico
try:
    calcule({1, 2, 3})
except TypeError as err:
    print(err)

try:
    calcule([])
except ValueError as err:
    print(err)

# bloco ELSE
# executado somente se não houver erro
try:
    calcule([1, 2, 3])
except:
    print("Ocorreu um erro inesperado")
else:
    print("deu tudo certo")

# bloco FINALLY
# executado sempre, com erro ou sem erro
try:
    calcule([1, 2, 3])
except:
    print("Ocorreu um erro inesperado")
else:
    print("deu tudo certo")
finally:
    print("finalizado...")
