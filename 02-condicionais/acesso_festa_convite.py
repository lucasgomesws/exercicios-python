idade = int(input("Qual é a sua idade? "))
possui_convite = True
if idade >= 18:
    print("maior de idade. verificando convite")
    if possui_convite:
        print("convite aprovado")
    else:
        print("convite negado")
else:
    print("acesso negado. evento apenas para maiores de 18 anos")
