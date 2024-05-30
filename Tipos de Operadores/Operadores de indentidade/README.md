# OPERADORES DE IDENTIDADE

São operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória.

| OPERADOR  | FUNÇÃO |
| --- | --- |
| is | Ocupa a mesma posição |
| is not | Não ocupa a mesma posição |

```python
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print(curso is nome_curso)

print(curso is not nome_curso)

print(saldo is limite)
```