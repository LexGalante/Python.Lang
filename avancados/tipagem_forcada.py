class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha


# typehiting serve apenas para desenvolvimento
# nao obriga ou força a tipagem
# utilizando : <tipagem> forçamos a entrada do valor no tipo que desejamos             retorno
def faz_um_monte_de_coisa(nome: str, ativo: bool, salario: float, usuario: Usuario) -> dict:
    return {
        'nome': nome,
        'ativo': ativo,
        'salario': salario,
        'usuario': usuario.__dict__
    }


usuario: Usuario = Usuario("alex", "123456")
teste = faz_um_monte_de_coisa(True, 10000, "alex", usuario)
print(teste)
print(faz_um_monte_de_coisa.__annotations__)