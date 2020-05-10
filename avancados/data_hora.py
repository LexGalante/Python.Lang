"""
Modulo builtin para usar data e hora chamado DateTime
"""
import datetime
from textblob import TextBlob

print(dir(datetime))
print(datetime.MINYEAR)
print(datetime.MAXYEAR)
print(datetime.datetime.now())
inicio = datetime.datetime(2020, 12, 31)
print(inicio)
# operações com data
nascimento = "12/04/1993"
print(nascimento)
nascimento = [int(x) for x in nascimento.replace("/", "-").split("-")]
print(nascimento)
data_nascimento = datetime.datetime(
    year=nascimento[2],
    month=nascimento[1],
    day=nascimento[0])
print(data_nascimento)
if data_nascimento.weekday() == 0:
    print("Você nasceu em uma segunda")
if data_nascimento.weekday() == 1:
    print("Você nasceu em uma terca")
if data_nascimento.weekday() == 2:
    print("Você nasceu em uma quarta")
if data_nascimento.weekday() == 3:
    print("Você nasceu em uma quinta")
if data_nascimento.weekday() == 4:
    print("Você nasceu em uma sexta")
if data_nascimento.weekday() == 5:
    print("Você nasceu em um sabado")
if data_nascimento.weekday() == 6:
    print("Você nasceu em um domingo")
data_atual = datetime.datetime.now()
print(data_atual - data_nascimento)
data_teste = datetime.timedelta(days=3)
print(data_teste)
print(data_atual + data_teste)
# combinando datas
data_agendameto = datetime.datetime.combine(
    date=(data_atual + datetime.timedelta(days=5, hours=18)),
    time=datetime.time())
print(data_agendameto)
print(data_atual.weekday())
# formantado datas
print(data_agendameto.strftime("%d/%m/%Y"))


def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B').translate(to='pt-BR'))} de {data.year}"


print(formata_data(data_nascimento))
