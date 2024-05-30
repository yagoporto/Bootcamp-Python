# ESTRUTURAS CONDICIONAIS

São estruturas de blocos que precisam atender uma  determinada condição para que aquilo que esteja dentro do bloco seja executado.

## IF

Para criar uma estrutura condicional simples, composta por um único desvio, podemos utilizar a palavra reservada `if` . O comando irá testar a expressão lógica e em caso de retorno verdadeiro as ações presentes no bloco de código do `if`  serão executadas.

Exemplo:

```python

idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("Parabéns você pode tirar sua CNH!")

if idade < 18:
    print("Sinto muito, você ainda nao atingiu a maior idade")
```

---

## IF/ELSE

Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas `if`  e `else` . Como sabemos se a expressão lógica testada no if for verdadeira, então o bloco de código do `if` será executado. Caso contrário o bloco de código do `else` será executado.

Exemplo

```python
numero = 7
resp = int(input("Tente advinhar o numero de 0 a 10: "))

if resp == 7:
    print("Parabéns você acertou, o numero é 7")
else:
    print("Infelizmente voce nao conseguiu acertar")
```

---

## IF/ELIF/ELSE

Em alguns cenários queremos mais de dois desvios, para isso podemos utilizar a palavra reservada `elif` . O `elif` é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro o bloco de código do `elif` será executado. Não existe um número máximo de `elif`  que podemos utilizar, porém evite criar grandes estruturas condicionais, pois elas aumentam a complexidade do código.

```python
import sys

opcao = int(input("Informe uma opção: [1] Saque \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    sys.exit("Opção inválida")
```

---

## IF ANINHADO

Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas `if` / `elif`/`else`  dentro do bloco de código de estruturas  `if` / `elif`/`else`.

Exemplo:

```python
nome = str(input("Qual seu nome? "))
idade = int(input("Qual sua idade? "))
sexo = str(input("Qual seu sexo Masculina[M] Femino[F]? "))

if sexo == "M":
    if idade < 18:
        print("Não precisa realizar o listamento obrigatorio ")
    else:
        print("Necessário realizar o alistamento obrigatorio")
elif sexo == "F":
    if idade < 18:
        print("Não precisa realizar o listamento obrigatorio ")
    else:
        print("Não precisa realizar o listamento obrigatorio ")

```

---

## IF TERNÁRIO

O `if` ternário permite escrever uma condição e uma única linha. Ele é composto por três partes, a primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão não seja atendida.

```python
status = "Sucesso" if saldo >= saque else "Falha
print(f"{status} ao realizar o saque!")
```