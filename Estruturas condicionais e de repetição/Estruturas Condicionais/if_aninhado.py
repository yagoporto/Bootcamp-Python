nome = str(input("Qual seu nome? "))
idade = int(input("Qual sua idade? "))
sexo = str(input("Qual seu sexo Masculina[M] Femino[F]? "))

if sexo == "M":
    if idade < 18:
        print("Não precisa realizar o listamento obrigatorio ")
    else:
        print("Necessário realizar o alistamento obrigatorio")
elif sexo == "F":
    if idade < 18:
        print("Não precisa realizar o listamento obrigatorio ")
    else:
        print("Não precisa realizar o listamento obrigatorio ")
