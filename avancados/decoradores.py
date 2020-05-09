def cumprimento(funcao):
    def saudacao():
        nome = funcao()
        print(f"Olá {nome}")
        print("Seja Bem-vindo")

    return saudacao()

# decorator
@cumprimento
def inicio_programa():
    return "Alex"


def caixa_alta_verifica_parametro(chave):
    def caixa(funcao):
        def aumentar(*args, **kwargs):
            if args and args[0] != chave:
                raise ValueError("Chave errada")
            return funcao(*args, **kwargs).upper()
        return aumentar
    return caixa


@caixa_alta_verifica_parametro('Alex')
def entrada(nome):
    return f'Olá {nome}'


@caixa_alta_verifica_parametro('Amanda')
def entrada_2(nome, sobrenome):
    return f'Olá 2 {nome} {sobrenome}'


print(entrada("Alex"))
print(entrada_2("Amanda", "Galante"))


def tipagem_forte(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novos_args = []
            for (valor, tipo) in zip(args, tipos):
                novos_args.append(tipo(valor))
            return funcao(*novos_args, **kwargs)
        return converte
    return decorador


@tipagem_forte(str, int)
def exibe_mensagem_repetida(mensagem, numero_vezes):
    for vez in range(numero_vezes):
        print(f"{vez} - {mensagem}")


print(exibe_mensagem_repetida("Teste...", '10'))
