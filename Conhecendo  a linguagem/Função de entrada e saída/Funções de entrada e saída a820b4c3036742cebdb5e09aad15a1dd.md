# Funções de entrada e saída

Todas as linguagens tem a função de entrar e saída de dados, também conhecidas como I/0 (input/output).

## INPUT (ENTRADA)

Essa função é usada para entrada de todos os dados vindo do usuário, nome, idade, tamanho, essa entrada recebe um argumento do tipo `string`, que é exibido para o usuário na tela.

```python
nome = input("Informe o seu nome: ")
```

## PRINT (SAIDA)

Essa função e usada para que os dados armazenados em uma variável seja exibido no saída de dados padrão (monitor). Ela recebe um argumento obrigatório do tipo `varargs` de objetos e 4 argumentos opcionais (`sep`, `end`, `file`, e `flush`). Todos os objetos são convertidos para `string`, separados por `sep` e terminados por `end`. A `string` final é exibida para o usuário. 

```python
#Saida de dados
nome = "Yago"
sobrenome = "Porto"

print(nome, sobrenome)
print(nome, sobrenome, end="...\n")
print(nome, sobrenome, sep="#")
```