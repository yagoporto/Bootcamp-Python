saldo = 1000
saque = 200
limite = 100

print(saldo >= saque)

print (saque <= limite)

print(saldo >= saque and saque <= limite)
"""Nessa operação ambas as condições precisam serem verdadeiras"""

print (saldo >= saque or saque <= limite)
"""Nessa operação apenas uma das condições precisam ser verdadeiras"""

print (not 1000 > 1500)
"""Nessa operação o resultado vai
dar verdadeiro pois tem o operador de negação"""
