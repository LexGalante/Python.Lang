"""
Operações em arquivos
"""

arquivo = open(file="arquivos/poema.txt", mode="r", encoding="utf8")
print(type(arquivo))
# efetuando leitura do arquivo todo
conteudo = arquivo.read()
print(conteudo)
# o ponteiro para manipulação se chama CURSOR
# retornando o CURSOR para inicio do arquivo
arquivo.seek(0)
# lendo linha a linha
print(arquivo.readline().upper())
print(arquivo.readline().upper())
arquivo.seek(0)
# fechando o arquivo
arquivo.close()

# a keyword WITH cria um contexto com que fecha automaticamente este recurso
# similar ao USING em C#

with open("arquivos/poema.txt") as arquivo:
    [print(linha.upper()) for linha in arquivo.readlines() if linha != "\n"]
    print(arquivo.closed)

print(arquivo.closed)
