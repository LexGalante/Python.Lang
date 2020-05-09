import os
import sys

print(dir(os))
# exibe o diretorio de execução atual
print(os.getcwd())
# nome do sistemas operacional
print(os.name)
print(os.uname_result)
print(os.path.isabs("C:\\Teste"))
print(sys.platform)
print(os.path.join(os.getcwd(), "teste"))
print(os.listdir("C:\\"))
c = [x.name for x in list(os.scandir("C:\\")) if x.is_dir]
print(c)
for arquivo in os.scandir("C:\\"):
    print(f"-> {arquivo.name}")

# verificando se um diretorio existe
print(os.path.exists("arquivos/teste"))
# criando um diretorio
os.mkdir("arquivos/teste")
print(os.path.exists("arquivos/teste"))
with open("arquivos/teste/arquivo_gerado.txt", 'w') as arquivo:
    arquivo.write("Criando diretorio e criando o arquivo")

os.unlink("arquivos/teste/arquivo_gerado.txt")
os.rmdir("arquivos/teste")
