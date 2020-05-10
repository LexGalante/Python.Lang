import json
from json import JSONEncoder


cliente = {
    'nome': 'Alex',
    'sobrenome': 'Galante',
    'idade': 29,
    'salario': 9899.99,
    'ativo': True
}
print(type(cliente))
cliente_serializado = json.dumps(cliente)
print(cliente_serializado)
print(json.dumps([1, 2, 3, 4, 5]))


class Usuario:
    def __init__(self, login, senha):
        self.login = login,
        self.senha = senha

    def to_json(self):
        return UsuarioSerialize().encode(self)


class UsuarioSerialize(JSONEncoder):
    def default(self, object):
        if isinstance(object, Usuario):
            return object.__dict__
        else:
            return json.JSONEncoder.default(self, object)


usuario = Usuario("alexg", "123456")
print(usuario.to_json())
json_recebido = json.loads('{"login":"amandag","senha":"1234"}')
print(json_recebido)
usuario2 = Usuario(**json_recebido)
print(usuario2.__dict__)
