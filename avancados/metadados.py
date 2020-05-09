from functools import wraps


def exibe_documentacao(funcao):
    @wraps(funcao)  # isto preserva os metadados da funcao
    def exibe(*args, **kwargs):
        print(f"Função: {funcao.__name__}")
        print(f"Documentação: {funcao.__doc__}")
        print("ARGS: ")
        print(args)
        print("KWARGS: ")
        print(kwargs)
        return funcao(*args, **kwargs)

    return exibe


@exibe_documentacao
def soma(numeros):
    """Passe um iteravel e receba a soma dos itens"""
    return sum(numeros)


print(soma((1, 2, 3, 4, 5, 6, 7, 8, 9)))
