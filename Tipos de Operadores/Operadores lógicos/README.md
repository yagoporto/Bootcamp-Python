# OPERADORES LÓGICOS

São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica. Quando um operador de comparação é utilizado, o resultado é um boleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos, exemplo:

`op_comparacao + op_logico + op comparacao… N …`

```python
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
 
```

### Parênteses

```python
saldo = 1000
saque = 250
limite = 200
conta_especial = True

print(saldo >= saque and saque <= limite 
or conta_especial and saldo >= saque)

print((saldo >= saque and saque <=limite)
 or (conta_especial and saldo >= saque))

```

<aside>
🚨 Segue a ordem de precedência

</aside>