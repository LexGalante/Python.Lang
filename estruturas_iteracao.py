# FOR
palavra = "PALAVRA"
vogais = "AEIOU"

for letra in palavra:
    print(letra)

letras_vogais = [letra for letra in palavra if letra in vogais]
print(letras_vogais)
letras_consoantes = [letra for letra in palavra if letra not in vogais]
print(letras_consoantes)

for indice, valor in enumerate(palavra):
    print(f"{indice} {valor}")

for indice, valor in enumerate(palavra):
    print(f"{indice} {valor}")
    if indice % 2 == 0:
        print("break loop")
        break

# WHILE
iterador = True
contador = 0
while iterador:
    contador += 1
    print(contador)
    parar = input("Deseja parar o loop, informe 1 ou SIM ou OK: ")
    if parar.lower() in ["s", "ok", "blz", "x"]:
        iterador = False
