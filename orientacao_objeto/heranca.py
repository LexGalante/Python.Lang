"""
Lembrar do principio de LISKOV -> (soLid)
"""
import random


# classe BASE
class Pessoa:
    def __init__(self, id, nome, sobrenome):
        self.__id = id
        self.nome = nome
        self.sobrenome = sobrenome

    # acesso a PROPERTY (GET)
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"


# classe FILHA
class Cliente(Pessoa):
    def __init__(self, id, nome, sobrenome, email):
        # metodo super() permite acessar classe pai
        super().__init__(id, nome, sobrenome)
        self.email = email

    def gera_login(self):
        login = self.email.split("@")[0]
        numero = random.randint(1, 100)
        return f"{login}{numero}"


class Funcionario(Pessoa):
    def __init__(self, id, nome, sobrenome, matricula, ativo):
        # metodo super() permite acessar classe pai
        super().__init__(id, nome, sobrenome)
        self.matricula = matricula
        self.ativo = ativo

    def nome_completo(self):
        return f"{self.matricula} - {super().nome_completo()}"


pessoa = Pessoa(id=1, nome="alex", sobrenome="galante")
print(type(pessoa))
print(dir(pessoa))
print(pessoa.nome_completo())
cliente = Cliente(id=2, nome="amanda", sobrenome="galante",
                  email="galante@x.com.br")
print(type(cliente))
print(dir(cliente))
print(cliente.nome_completo())
print(cliente.gera_login())
funcionario = Funcionario(
    id=3, nome="nino", sobrenome="ninox", matricula=9999, ativo=True)
print(type(funcionario))
print(dir(funcionario))
print(funcionario.nome_completo())
funcionario.id = 5  # utilizando o @id.setter
print(funcionario.id)  # utilizando @property
