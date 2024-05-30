# VARIÁVEIS E CONSTANTES

## Variáveis

Em uma linguagem de programação podemos definir valores que podem sofrer alterações durante a execução do programa. Esse valores recebem o nome de variáveis, que nada mais é do que um local na memoria onde será armazenado esses valores durante a execução do programa.

Exemplo:

```python
age = 26
name = 'Yago'
print(f'Meu nome é {name} e eu tenho {age} anos de idade.')

#você tambem pode declarar varías variáveis em apenas 1 linha
#age, name (26,'Yago')
```

### Alterando os valores

Perceba que em Python não precisamos definir o tipo de dado da variável, já e feito isso automaticamente. Por isso não podemos simplesmente criar uma variável sem atribuir um valor. Para alterar o valor da variável basta fazer uma nova atribuição a ela.

```python
age = 26
name = 'Yago'
print(f'Meu nome é {name} e eu tenho {age} anos de idade.')

#você tambem pode declarar varías variáveis em apenas 1 linha
#age, name (26,'Yago')

#Tambem podemos alterar o valores
age = 23
name = 'Priscilla'
print(f'Meu nome é {name} e eu tenho {age} anos de idade')
```

---

## Constantes

Assim como as variáveis, constantes também são espações na memoria para armazenar valores, porém o valor atribuído a ela no inicio permanece ate o fim do programa.

<aside>
🚨 Não existe uma palavra reservada para definir uma constante em Python. Em linguagens como por exemplo: Java e C utilizamos `final`  e `const` , respectivamente para declarar uma constante.
Em Python usamos a convenção que diz ao programador que a variável é uma constante. Para fazer isso, você deve criar a variável com o nome todo em letras maiúsculas.

</aside>

```python
ABS_PATH = '/home/yago/Documents/python_course/'
DEBUG = True
STATES = [
			'SP',
			'RJ',
			'MG'
]
AMOUNT = 30.2			
```

---

## BOAS PRÁTICAS

- O padrão de nomes deve ser “[snake case](https://www.alura.com.br/artigos/convencoes-nomenclatura-camel-pascal-kebab-snake-case)”.
- Escolher nomes sugestivos.
- Nome de constantes todo em maiúsculo.