saldo = 2000

saque = float(input("Digite o valor que gostaria de sacar: R$"))
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")