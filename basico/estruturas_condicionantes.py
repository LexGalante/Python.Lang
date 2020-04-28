# IF ELIF ELSE

idade = int(input("Informe sua idade: "))

if idade < 8:
    print("Você é uma criança")
elif idade > 8 and idade < 18:
    print("Você é um adolescente")
elif idade > 18 and idade < 30:
    print("Você é um jovem")
elif idade > 30 and idade < 50:
    print("Você é um adulto")
else:
    print("Você é um idoso")




