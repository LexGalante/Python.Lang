# ESCOPO GLOBAL
variavel_global = "Global"


# ESCOPO FUNCAO
def minha_funcao():
    variavel_local = "Local"
    return variavel_local


# ESCOPO CLASSE
class MinhaClasse:
    meuAttr = "Classe"


print(variavel_global)
print(minha_funcao())
print(MinhaClasse().meuAttr)
