# OPERADORES DE ASSOCIAÇÃO

São operadores utilizados para verificar se um objeto está presente em uma sequência.

| OPERADOR | FUNÇÃO |
| --- | --- |
| in | Está na sequencia |
| in not | Não esta na sequencia |

```python
curso = "curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

print("Python" in curso)

print("maçã" not in frutas)

print(200 in saques)
```

<aside>
🚨 Essa comparação é [**Case-sensitive**](https://pt.wikipedia.org/wiki/Case-sensitive)

</aside>