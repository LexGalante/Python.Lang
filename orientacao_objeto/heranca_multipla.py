import random


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.__nome = nome,
        self.__sobrenome = sobrenome

    @property
    def nome(self):
        return self.__nome

    @property
    def sobrenome(self):
        return self.__nome

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

    # metodo builtin
    def __str__(self):
        return str({chave.split("__")[1]: valor for chave, valor in self.__dict__.items()})


class Usuario:
    def __init__(self, id, email):
        self.id = id
        self.email = email

    def gera_login(self):
        login = self.email.split("@")[0]
        numero = random.randint(1, 100)
        return f"{login}{numero}"


class Funcionario(Pessoa, Usuario):
    def __init__(self, nome, sobrenome, id, email, matricula):
        Pessoa.__init__(self, nome, sobrenome)
        Usuario.__init__(self, id, email)
        self.matricula = matricula


funcionario = Funcionario("alex", "galante", 1, "galante@teste.com", 9999)
print(type(funcionario))
print(dir(funcionario))
print(funcionario.nome_completo())
print(funcionario.gera_login())
print("Funcionário é instancia de:")
print(f"Pessoa: {isinstance(funcionario, Pessoa)}")
print(f"Usuario {isinstance(funcionario, Usuario)}")
print(f"Funcionario {isinstance(funcionario, Funcionario)}")
print("Ordem de execução de metodos: ")
print(Funcionario.__mro__)  # ordem de execução de metodos
teste = Pessoa("alex", "galante")
print(str(teste))  # invocando metodos builtins
