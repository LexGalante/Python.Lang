import os
from csv import reader
from csv import DictReader
from csv import writer

with open("avancados/dados.csv") as arquivo:
    leitor = reader(arquivo)
    for linha in leitor:
        print(f"{linha[0]} {linha[1]} {linha[2]}")

with open("avancados/dados.csv") as arquivo:
    leitor = DictReader(arquivo, delimiter=",")  # OrderedDict
    for linha in leitor:
        print(
            f'Nome: {linha["nome"]}, Sobrenome: {linha["sobrenome"]}, Idade: {linha["idade"]}')


def get_clientes():
    return [
        ["alex", "galante", 29],
        ["amanda", "galante", 29],
        ["nino", "galante", 29]
    ]


with open("avancados/cliente.csv", "w") as arquivo:
    escritor = writer(arquivo)
    escritor.writerow(["nome", "sobrenome", "idade"])
    escritor.writerows(get_clientes())

os.unlink("avancados/cliente.csv")
