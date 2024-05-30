saldo= 0
limite= 500
extrato=""
numero_saque=1
LIMETE_SAQUE=3

menu='''
=================MENU=================

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
--> '''


while True:
    opcao = int(input(f"{menu}"))
    if opcao == 1:
        valor = float(input("Digite o valor que deseja depósitar: R$"))
        
        if valor > 0:
            saldo += valor
            extrato += f"+ R${valor:.2f}\n"
            print(f'''
=================DEPOSITO=================
            
Realizado deposito no valor de: R${valor:.2f}
==========================================
            ''')
        else:
            print('''
==========================================
Por favor digite um valor maior que 0!
==========================================
''')

    elif opcao == 2:
        saque= float(input("Digite o valor do saque: R$"))
        
        if saque > 500:
            print(f"Limite de saque: R${limite:.2F}")

        elif saque > saldo:
            print("Operação nao realizada, saldo insuficiente")

        elif numero_saque > LIMETE_SAQUE:
            print("Você atingiu o limite de saques diarios")

        elif saque <= 500 and saque <= saldo and numero_saque <= LIMETE_SAQUE:
            numero_saque += 1
            saldo -= saque
            extrato += f"- R${saque:.2f}\n"
            print(f'''
=================SAQUE=================
            
Realizado saque no valor de: R${saque:.2f}
=======================================
            ''')


    elif opcao == 3:
                    print(f'''
=================EXTRATO=================
            
{extrato}
Saldo atual= R${saldo:.2f}
=========================================
            ''')

    elif opcao == 0:
        print("Obrigado por utilizar nosso sistema!")
        break

    else:
        print("Opção invalida, por favor selecione a operação desejada")