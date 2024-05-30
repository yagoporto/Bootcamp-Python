saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp_1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp_1)

exp_2 = (saldo >= saque and saque <=limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_saldo_suficiente = exp_2 = (saldo >= saque and saque <=limite)
conta_especial_saldo_suficiente = (conta_especial and saldo >= saque)

exp_3 = conta_normal_saldo_suficiente or conta_especial_saldo_suficiente
print(exp_3)