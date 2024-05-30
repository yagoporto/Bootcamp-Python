# CONHECENDO MÉTODOS ÚTEIS DA CLASSE STRING

A classe `String` do Python é famosa por ser rica em métodos e possuir uma interface muito fácil de trabalhar.

Em algumas linguagens manipular sequência de caracteres não é um trabalho trivial, porém, em Python esse trabalho é muito simples.

## Maiúscula, minúscula e título

```python
curso = "pYtHon"

print=(curso.upper())
>>> PYTHON

print=(curso.lower())
>>> python

print(curso.title())
>>> Python
```

- `.upper` = Converte todos os caracteres para maiúsculo.
- `.lower` = Converte todos os caracteres para minúsculo.
- `.title` = Converte o todos para minúsculo exceto o primeiro caractere

---

## Eliminando os espaços em branco da String

```python
curso= "  Python "

print=(curso.strip())
>>> "Python"

print=(curso.lstrip())
>>> "Python "

print=(curso.rstrip())
>>> "  Python"
```

- `.strip` = Ira remover o espaço em branco da esquerda e da direita.
- `.lstrip` = ira remover o espaço em branco apenas da esquerda.
- `.rstrip` = ira remover o espaço em branco apenas da direita.

---

## Junções e centralização

```python
curso= "Python"

print(curso.center(10, "#"))
>>> "##Python##"

print(".".join(curso))
>>> "P.y.t.h.o.n"
```

- `.center` = o método `center`  e construído por 2 argumentos, o primeiro é o numero de “casas” que a `String` vai ocupar (incluindo o espaço em branco), e o segundo é o caractere que será concatenado nos espações em branco(opcional)
- `.join` = primeiro você ira passar o caractere que quer juntar na `String` com o `.join` e depois passar a `String` .