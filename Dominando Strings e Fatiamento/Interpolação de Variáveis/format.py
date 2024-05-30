nome="Yago"
idade=26
curso="Python"
nota=10.0

pessoa= {"nome":"Yago", "idade":26, "curso":"Python", "nota":10.0}

print("Olá, me chamo {}, tenho {} de idade. Estou matriculado no curso de {} e a nota do curso é {}"
    .format(nome, idade, curso, nota))

print()

print("Olá, me chamo {2}, tenho {3} de idade. Estou matriculado no curso de {0} e a nota do curso é {1}"
    .format(curso, nota, nome, idade))

print()

print("""Olá, me chamo {nome}, tenho {idade} de idade. Estou matriculado no curso
    de {curso} e a nota do curso é {nota}"""
    .format(curso=curso, nota=nota, nome=nome, idade=idade))

print("""Olá, me chamo {nome}, tenho {idade} de idade. Estou matriculado no curso
    de {curso} e a nota do curso é {nota}"""
    .format(**pessoa))