# IF ELIF ELSE

idade = int(input("Informe sua idade: "))

maior_idade = "SIM" if idade >= 18 else "NÃO"

if idade < 8:
    print(f"Você é uma criança, Maior de idade: {maior_idade}")
elif idade > 8 and idade < 18:
    print(f"Você é um adolescente, Maior de idade: {maior_idade}")
elif idade > 18 and idade < 30:
    print(f"Você é um jovem, Maior de idade: {maior_idade}")
elif idade > 30 and idade < 50:
    print(f"Você é um adulto, Maior de idade: {maior_idade}")
else:
    print(f"Você é um idoso, Maior de idade: {maior_idade}")




