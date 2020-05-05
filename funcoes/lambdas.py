"""
Expressões anomimas
Intepratadas em sua execução
"""


expressao = lambda numero: numero * numero
print(expressao(5))
expressao = lambda numero, elevacao: numero ** elevacao
print(expressao(5, 5))
expressao = lambda nome = "teste": nome.title() 
print(expressao())
linguagens = ["Python", "C#", "Java", "Golang", "Julia", "R"]
print(linguagens)
linguagens.sort(key=lambda linguagem: linguagem[0])
print(linguagens)