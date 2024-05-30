# ESTRUTURAS DE REPETIÇÃO

São utilizadas para repetir um trecho do código um determinado número de vezes, esse número pode ser definido através de uma expressão lógica.

Exemplo sem repetição:

```python
# Receba um número do teclado e exiba os 2 números seguintes
a = int(input("Informe um número inteiro: "))
print(a)

a += 1
print(a)

a += 1
print(a)
```

Exemplo com repetição:

```python
a = int(input("Informe um número inteiro: "))
print(a) 
repita 2 vezes : 
	a+=1
	print(a)
```

## FOR

O comando for é usada para percorrer um objeto interável. Faz sentido usar for quando sabemos o número de exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto interável.

Exemplo:

```python
texto = input("informe um texto: ")
VOGAIS = "AEIOU"
for letra int texto:
	if letra.upper() in VOGAIS
		print(letra, end="")
print()	#quebra de linha	
```

1. Na primeira parte do código `texto = input("informe um texto: ")` Estamos solicitando ao usuário que informe um texto.
2. Nessa parte `VOGAIS = "AEIOU"` estamos declarando uma constante.
3. Aqui iniciamos a estrutura `for` , `for letra int texto:`  ela vai atribuir a variável `letra` o valor de cada letra do texto digitado, vai percorrer o texto 1 a 1.
4. nessa estrutura condicional `if letra.upper() in VOGAIS` , ele vai transformar a letra que estará na variável `letra` naquele momento para maiúscula com o comando `.upper` e depois comparar com a constante `VOGAIS` uma a uma.
5. Nesse trecho `print(letra, end="")` será exibido a variável `letra` caso ela seja igual a uma das letras da constante `VOGAIS` comparada a cima.

## FOR / ELSE

Executa no final do laço

Caso não tenha um valor atribuído a variável, ele executara o final do laço.

<aside>
🚨 O ELSE na estrutura FOR não e muito comum no dia a dia

</aside>

## Função RANGE

Range é uma função built-in do Python, ela é usada para produzir um sequência de números inteiros a partir de um inicio (inclusivo) para um fim (exclusivo). Se usarmos `range(i, j)`  será produzido:

i, i+1, i+2, i+3, …, j-1.

Ela recebe 3 argumentos: `stop` (obrigatório), `start` (opcional) e `step`  (opcional).

```python
# range(stop) -> range object
# range(start, stop[, step]) -> range object

list(range(4))
>>> [0,1,2,3]
```

Utilizando o `range` com o `for` :

```python
for numero in range(0,11)
	print(numero, end=" ")
>>> 0 1 2 3 4 5 6 7 8 9 10

#Exibindo a tabuada do 5
for numero in range(0, 51, 5)
	print(nuemro, end=" ")
>>> 0 5 10 15 20 25 30 35 40 45 50		
```

- `stop` = fim
- `start` = inicio da contagem
- `step` = intervalo

## Comando WHILE

O comando `while`  é usada para repetir um bloco de código várias vezes. Faz sentido usar `while`  quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado.

```python
opcao = -1

while opcao !=0:
	opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
	if opcao == 1:
		print("Sacando...")
	elif opcao == 2:
		print("Exibindo o extrato...")	
```

## WHILE/ELSE

Assim como no `for`Também temos o `else` caso a condição logica for atendida no `while` e executado o final do laço 

```python
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair: "))
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")
else:
    print("Obrigado por utilizar nosso sistema!")
```

## BREAK

É usado para parar um laço, é comumente utilizado em laços de repetições infinitos como  o exemplo a seguir:

O usuário irá digitar um valor, e o programa vai dizer a ele se é par ou impar, caso o usuário digite o número 0 será exibida uma mensagem de agradecimento e ira encerrar o laço.

```python
while True:
    numero = int(input("Digite um número ou [0] para Sair: "))
    if numero == 0:
        print("Obrigado por utilizar o programa!")
        break
    elif numero %2 == 0:
        print("É um número par!")
    else:
        print("É um númemro impar!")
```

Também é possível usar com o for como no exemplo:

```python
for numero in range(100):
    if numero == 10:
        break
    print(numero, end=" ")
```

Também temos a variação do `break`  o `continue` , ele serve para pular uma repetição e dar continuidade na próxima, como no exemplo a seguir:

```python
for numero in range(101):
    if numero  % 2 == 0:
        continue
    print(numero, end=" ")
```

Nesse exemplo será exibido apenas os números impares de 0 a 100, pois estará pulando o loop toda vez que o resto da divisão da variável `numero`  por 2 seja igual a 0.