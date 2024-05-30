# FATIAMENTO DE STRING

O fatiamento de strings é uma técnica utilizada para retornar substrings (parte da String original), informando início (start), fim (stop) e passo (step): [start: stop [, step]].

## Fatiamento

```python
nome ="Yago de Souza Freitas Porto"

nome[0]
>>> "Y"

nome[:5]
>>> "Yago"

nome[9:]
>>> "Souza Freitas Porto"

nome[23:28]
>>> "Porto"

nome[23:28:2]
>>> "Pro"

nome[:]
>>> "Yago de Souza Freitas Porto"

nome[ :: -1]
>>> "otroP satierF azuoS ed ogaY"
```