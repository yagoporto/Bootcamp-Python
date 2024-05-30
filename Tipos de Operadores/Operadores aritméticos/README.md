# OPERADORES ARITMÉTICOS

Os operadores são aqueles que executam operações matemáticas, como adição, subtração, multiplicação e divisão.

## Conhecendo os Operadores

Operadores básicos

| OPERADORES | FUNÇÃO |
| --- | --- |
| + | Adição |
| - | Subtração |
| * | Multiplicação |
| / | Divisão |

Exemplo:

```python
#Adição
print(1 + 1)

#Subtração
print(10 - 2)

#Multiplicação
print(4 * 3)

#Divisão
print(10 / 2)

```

Módulos, exponenciação e divisão inteira

| OPERADORES | FUNÇÃO |
| --- | --- |
| // | Divisão inteira |
| % | Modulo(Resto da divisão) |
| ** | Exponenciação |

Exemplos:

```python
#Divisão inteira
print(10 // 2)

#Módulo
print(10 % 3)

#Exponenciação
print(2 ** 3)
```

---

## Ordem de precedências

Na matemática  existe uma regra que indica a ordem de execução de cada operação. Isso é útil pois ao analisar uma expressão, a depender da ordem das operações o valor pode ser diferente:

x= 10 - 5 * 2

x é igual a 10 ou 0?

A definição indica a seguinte ordem como a correta:

- Parêntesis
- Expoentes
- Multiplicações e divisões(da esquerda para a direita)
- Somas e subtrações (das esquerda para a direita)

```python
print(10 - 5 * 2)

print((10 - 5) * 2)

print(10 ** 2 * 2)

print(10 ** (2 * 2))

print(10 / 2 * 4)
```