def minha_funcao_sem_parametro():
    """Documentação Docsstring, utilize print(help(minha_funcao_sem_parametro))"""
    return "Teste testando testamento...."


def minha_funcao_com_parametro(texto):
    return texto.upper()


def soma(numeros):
    if type(numeros) is not list:
        return 0
    return sum(numeros)


def quadrado(numero):
    if type(numero) is not int:
        return 0
    return numero * numero


def exponencial(numero, potencia=2):
    return numero ** potencia


def funcao_com_parametro_callback(text, func=lambda text: text.title()):
    text += " testando..."
    return func(text)


def usuario(login, password, active):
    """
    Cria um usuário
    :login do usuário
    :password do usuário
    :active usuário está ativo
    """
    return {
        "login": login,
        "password": password,
        "active": active
    }


def nome_programa(nome="Python.Lang"):
    return nome


teste = 42


def funcao_usando_parametro_global():
    global teste
    return teste


def funcoes_aninhadas():
    numero = 42

    def funcao_interna():
        nonlocal numero
        return numero

    return funcao_interna()

# utilizar *args como o ultimo parametro antes dos opicionais
# transforma o *args em uma tupla


def funcao_com_varios_parametros(*args):
    return print(sum(args))

# utilizar o **kwargs como ultimo parametro de uma funcao
# tranforma o **kwargs em uma tupla


def funcao_com_varios_parametros_2(**kwargs):
    if 'nome' in kwargs:
        print(f'achei o nome: {kwargs["nome"]}')
    print(kwargs)


print(help(print))
print(help(minha_funcao_sem_parametro()))
print(minha_funcao_sem_parametro())
print(minha_funcao_com_parametro(minha_funcao_sem_parametro()))
print(soma([5, 5, 5, 6]))
print(quadrado(5))
print("parametros nomeados")
print(usuario(active=False, password="teste", login="teste"))
print("parametros com valores default")
print(nome_programa())
print(exponencial(5))
print(funcao_com_parametro_callback("Teste"))
print(funcao_usando_parametro_global())
print(funcoes_aninhadas())
funcao_com_varios_parametros(1)
funcao_com_varios_parametros(1, 2)
funcao_com_varios_parametros(1, 2, 3)
funcao_com_varios_parametros(1, 2, 3, 4)
funcao_com_varios_parametros(1, 2, 3, 4, 5)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# usando o * pedimos ao python que realize o desempactamento da variavel antes de usar
funcao_com_varios_parametros(*numeros)
funcao_com_varios_parametros_2(nome='Alex', sobrenome='Galante', idade=18)
