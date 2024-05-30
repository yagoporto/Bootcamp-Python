while True:
    numero = int(input("Digite um número ou [0] para Sair: "))
    if numero == 0:
        print("Obrigado por utilizar o programa!")
        break
    elif numero %2 == 0:
        print("É um número par!")
    else:
        print("É um númemro impar!")