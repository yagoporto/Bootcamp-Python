# Modo interativo | DIR | HELP

O modo interativo tem como objetivo rodas os comandos da linguagem sem precisar passar pelo arquivo py, existem 2 maneiras de fazer isso?

- Usando o terminal você pode digitar `python` e ele entrará no modo interativo.
- Usando o terminal aberto na pasta onde esta o arquivo, é só digitar `python -i (nome do arquivo)` ele executara o arquivo .py e rodar as linhas de comandos que esta dentro dele.

## DIR

O comando `dir` permite listar os nomes dos atributos e métodos disponíveis em um objeto ou módulo específico. 

como por exemplo você pode usar o comando dir na seguinte forma `dir()` , ira listar todos o atributos do escopo do arquivo. 

Também pode usar assim `dir(100)` irá fazer o mesmo para o objeto “100”.

## HELP

Invoca o sistema de ajuda integrado. é possível fazer buscar em modo interativo ou informar por parâmetro qual o nome do módulo, função, classe, método ou variável. 

`help()`

`help(100)`