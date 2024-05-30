# CONVERSÃO DE TIPOS

Em alguns momentos é necessário convertes o tipo de uma variável para manipular de forma diferente. Por exemplo:

Variáveis do tipo `string` , que armazenam números e precisamos fazer alguma operação matemática com esse valor.

```python
#varíavel do tipo inteiro
preco = 10
print(preco)

#podemos converter o tipo dela dessa forma
preco = float(preco)
print(preco)

preco = 10 / 2
print(preco)

preco = 10.30
preco = int(preco)
print(preco)
```

Como converter essa variável para string 

```python
#convertendo para string
preco = 10.50
idade = 28

print(str(preco))
print(str(idade))

texto = f"idade {idade} preco {preco}"
print(texto)
```

Convertendo String para número

```python
#convertendo string para número
preco = "10.50"
idade = "26"

print(float(preco))
print(int(idade))

```