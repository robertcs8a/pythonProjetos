# natação categorias 
nome = str(input('Qual é o nome do atleta: '))
ano = int(input(f'informe o ano de nascimento de {nome} :'))
idade = 2024 - ano
print(f'idade = {idade}')
if idade  <= 9:
    print(idade)
    print(f'categoria mirim idade = {idade} anos  apto há treinar nessa base')
if idade > 9 and idade < 15:
    print(idade)
    print(f'categoria infantil idade = {idade} anos apto há treinar nessa base')
if idade > 14 and idade < 20 :
    print(idade)
    print(f'categoria junior idade = {idade} anos apto há treinar nessa base')
if idade == 20:
    print(idade)
    print(f'categoria senior idade = {idade} anos apto há treinar nessa categoria')
if idade > 20:
    print(idade)
    print(f'categoria master idade = {idade} anos ou maior, livre para atuar.')
    

