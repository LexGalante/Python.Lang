"""
MODULOS
São os arquivos com funcoes, classes etc ... disponiveis
"""
import random  # modulo builtin
import modulo_matematica  # primeira forma
from modulo_matematica import soma  # segunda forma, tem melhor performance
from modulo_matematica import media, mediana  # busca somente oq é necessário
from pacote import modulo_um
from pacote.modulo_dois import funcao, dois
from random import randint as rdi  # atribuindo um alias a importação de um modulo
from colorama import Fore, Back, Style
from colorama import init  # importando modulo instalado via pip
init()

print(__name__)
if __name__ == "__main__":  # ao ser executado como main
    print(Fore.RED, random.random())
    print(Fore.BLUE, modulo_matematica.soma(list(range(25, 1, -1))))
    print(Fore.CYAN, modulo_matematica.media(list(range(1, 10, 5))))
    print(Fore.MAGENTA, modulo_matematica.mediana(list(range(5, 50, 7))))

    print(Fore.YELLOW, soma([5, 6, 7, 7, 88, 99]))
    print(Fore.WHITE, media([3, 4, 5, 6, 777, 991]))
    print(Fore.LIGHTBLUE_EX, mediana([55, 66, 77, 88, 99, 100, 230, 250]))
    print(Fore.MAGENTA, rdi(1, 10))

    print(Fore.BLUE, modulo_um.funcao(modulo_um.um))
    print(Fore.YELLOW, funcao(dois))
