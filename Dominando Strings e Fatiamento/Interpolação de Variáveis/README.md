# INTERPOLAÇÃO DE VARIÁVEIS

Em Python temos 3 formas de interpolar variáveis em `String` , a primeira é usando o sinal `%`, a segunda é utilizando o método `format` e a última é utilizando `f strings` .

<aside>
🚨 A primeira não é atualmente recomendada e seu uso em Python 3 é raro.

</aside>

## Old style %

```python
nome= "Yago"
idade= 26
profissao= "TI"
curso= "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." %(nome, idade, profissao, curso))

>>> Olá, meu nome é Yago. Eu tenho 26 anos de idade, trabalho com TI e estou matriculado no curso de Python.
```

- para interpolar (concatenar) os valores devemos colocar dentro do texto a ser exibido o sinal `%` , logo depois colocamos a letra que representa o  tipo da variável, após escrever todo o texto passamos as variáveis que queremos concatenar.

| CODIGO | FUNÇÃO |
| --- | --- |
| %d  | para valores do tipo Inteiros |
| %s | para valores do tipo String |
| %f  | para valores tipo float |

---

## Método format

```python
nome="Yago Porto"
idade=26
profisso="TI"
curso="Python"

print("Olá me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}.".format(nome, idade, profissao, curso)

print("Olá me chamo {3}. Eu tenho {0} anos de idade, trabalho com {2} e estou matriculado no curso de {1}.".format(idade, curso, profissao, nome)

>>> Olá, meu nome é Yago. Eu tenho 26 anos de idade, trabalho com TI e estou matriculado no curso de Python.
```

- Funciona da mesma forma que o old style, porém ao invés de utilizar %, iremos utilizar as chaves {}, colocamos o `.format` e passar as variáveis.
    
    Também podes numerar as chaves que corresponderá a ordem das variáveis passadas.
    

Também conseguimos passar essas variáveis de forma nomeada como no exemplo a seguir:

```python
print("Olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {curso}.".format(nome=nome, idade=idade, profissao=profissao, curso=curso))

>>> Olá, meu nome é Yago. Eu tenho 26 anos de idade, trabalho com TI e estou matriculado no curso de Python.

```

ou também:

```python
print("Olá me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}.".format(**pessoa))

>>> Olá, meu nome é Yago. Eu tenho 26 anos de idade, trabalho com TI e estou matriculado no curso de Python.
```

---

## F-STRING

```python
nome="Yago Porto"
idade=26
profisso="TI"
curso="Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho na aréa de {profissao} e estou matriculado no curso de {curso}."

>>> Olá, meu nome é Yago. Eu tenho 26 anos de idade, trabalho com TI e estou matriculado no curso de Python.
```

- Nesse método você só precisa colocar `f` no inicio da `string` e passar as variáveis dentro das chaves.

---

## Formatar strings com f-string

```python
PI= 3.14159

print(f"Valor de PI: {PI:.2f}")
>>> "Valor de PI: 3.14"

print(f"Valor de PI: {PI:10.2F}")
>>> "Valor de PI:         3.14"
```

- O numero antes do f representa a quantidade de casas que será mostrada após o “.”.
- O número antes do “.” representa a quantidade de espações em brancos a ser exibindo antes do valor da variável.