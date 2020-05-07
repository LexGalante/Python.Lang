with open("arquivos/poema_escrita.txt", mode='w') as arquivo:
    arquivo.write("teste.....")
    arquivo.write("teste1.....")
    arquivo.write("teste2.....")
    arquivo.write("teste3.....")
    arquivo.write("teste4.....")

with open("arquivos/poema_escrita.txt") as arquivo:
    print(arquivo.read())

with open("arquivos/poema_escrita.txt", mode="a") as arquivo:
    while True:
        linha = input("Escreva uma linha ou digite sair: ")
        if linha != "sair":
            arquivo.write(linha)
            arquivo.write("\n")
        else:
            break

with open("arquivos/poema_escrita.txt") as arquivo:
    print(arquivo.read())
