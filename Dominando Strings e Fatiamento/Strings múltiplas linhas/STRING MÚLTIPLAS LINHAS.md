# STRING MÚLTIPLAS LINHAS

Strings de múltiplas linhas são definidas informando 3 aspas simples ou duplas durante a atribuição. Elas podem ocupar várias linhas do código, e todos os espaços em branco são incluídos na String final.

  

## Strings triplas

```python
nome="Yago"

mensagem = f"""
Olá meu nome é {nome},
Estou estudando Python.
"""

>>> 

		Olá meu nome é Yago,
		Estou estudando Python.
		
mensagem = f'''
		Olá meu nome é {nome},
	Eu estou aprendendo Python
			Essa mensagem tem diferentes recuos.'''
			
>>>
			
		Olá meu nome é Yago,
	Eu estou aprendendo Python
			Essa mensagem tem diferentes recuos.
```