# IDENTAÇÃO E BLOCOS

Identar um código uma forma de manter o código fonte mais legível e manutenível. Mas em Python ela exerce um segundo papel, através da identação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.

### BLOCO DE COMANDOS

As linguagens de programação costuma utilizar caracteres ou palavras reservadas para determinar o início e fim do bloco. Em Java e C por exemplo, utilizamos chaves.

Exemplo em Java:

```java
void sacar(double valor) { //início do bloco método
		if (this.saldo >= valor) { //início do bloco if
				this.saldo -= valor;
		} //fim do bloco if
} //fim do bloco do método
```

### UTILIZANDO ESPAÇOS

Existe uma convenção em Python, que define as boas práticas para escrita de código na linguagem. Nesse documento é indicado utilizar 4 espações em branco por nível de identação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco.

Exemplo em Python

```python
def sacar(self, valor: float) None: #início do bloco método
    if self.saldo >= valor: #Início fo bloco if
		    self.saldo -= valor
					
		#fim do bloco if
		
#fim do bloco método
```