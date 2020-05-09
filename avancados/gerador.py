def contador(maximo):
    """A palavra reservada YELD acumula vários retornos"""
    contador = 1
    while contador <= maximo:
        yield contador
        contador += 1


gerador = contador(20)
print(type(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
for numero in gerador:
    print(numero)
