"""
Por conveção se utiliza o camel case
"""
import random
from passlib.hash import pbkdf2_sha256 as crypto  # pacote para encriptar strings


class Usuario:  # definição da classe
    mensagem = "seja bem vindo"

    def __init__(self, email, senha, ativo):
        self.email = email  # publico
        self.__senha = crypto.encrypt(
            senha, rounds=20000, salt_size=16)  # publico
        self.__ativo = ativo  # privado
        # a partir do construtor acessando o attr de classe
        Usuario.mensagem += "!!!"

    @property
    def esta_ativo(self):
        """ propiedade para acessar um atributo privado"""
        return self.__ativo

    # metodo de instancia
    def gera_login(self):
        login = self.email.split("@")[0]
        numero = random.randint(1, 100)
        return f"{login}{numero}"

    # metodo de instancia
    def valida_senha(self, senha):
        if crypto.verify(senha, self.__senha):
            return True
        else:
            return False

    # metodo de classes
    @classmethod
    def saudacao(cls):
        print(cls)
        return cls.mensagem.title()

    # metodo estatico
    @staticmethod
    def gerar_usuario():
        return Usuario("teste@teste", "123456", False)


print(type(Usuario))
print(dir(Usuario))
usuario = Usuario(input("Informe o email: "), input("Informe a senha: "), True)
print(usuario.__dict__)
print(usuario)
print(usuario.email)
try:
    print(usuario.__ativo)  # não vai funcionar pois o atributo e privado
except AttributeError:
    print("não é possivel acessar atributos privados")
print(usuario.esta_ativo)
print(usuario.mensagem)
print(usuario.saudacao())
# adcionando atributos dinamicos ao objeto
usuario.exibe_mensagem = lambda usuario: print(
    f"{usuario.mensagem} {usuario.email}")
usuario.exibe_mensagem(usuario)
# removendo atributos dinamicos
del usuario.exibe_mensagem
try:
    usuario.exibe_mensagem(usuario)
except AttributeError:
    print("impossivel acessar atributo dinamico após remove-lo")
# invocando um metodo
print(usuario.gera_login())
print(usuario.valida_senha(input("Informe a senha para validamos: ")))
usuario2 = Usuario.gerar_usuario()
print(usuario2)
print(usuario2.__dict__)
