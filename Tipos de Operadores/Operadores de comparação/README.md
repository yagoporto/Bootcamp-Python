# OPERADORES DE COMPARAÇÃO

São operadores utilizados para comparar dois valores

| OPERADOR  | FUNÇÃO |
| --- | --- |
| ==  | Igual  |
| != | Diferente |
| > | Maior  |
| >= | Maior ou igual |
| < | Menor |
| <= | Menor ou igual |

```python
saldo = 450
saque = 200

print(saldo == saque)
"""ira retorna o valor false pois o valor da variável
    saldo não é igual a da variável saque."""

print(saldo != saque)
"""ira retorna o valor true pois o valor da
variavel saldo é diferente da variável saque"""

print(saldo > saque)
"""ira retornar o valor de true, pois o
valor de saldo é maior que de saque"""

print(saldo >= saque)
"""ira retornar o valor de true, pois o
valor de saldo é maior ou igual ao de saque"""

print(saldo < saque)
"""ira retornar o valor de false, pois o
valor de saldo não é menor ao saque"""

print(saldo <= saque)
"""ira retornar o valor de false, pois o
valor de saldo não é menor ou igual ao saque"""
```