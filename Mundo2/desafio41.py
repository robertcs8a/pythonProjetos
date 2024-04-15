# natação categorias 
from datetime import date
atual = date.today().year
nome = str(input('Qual é o nome do atleta: '))
ano = int(input(f'informe o ano de nascimento de {nome} :'))
idade = atual - ano

if idade  <= 9:
    print(f'categoria mirim idade = {idade} anos  apto há treinar nessa base')
elif idade > 9 and idade < 15:
    print(f'categoria infantil idade = {idade} anos apto há treinar nessa base')
elif idade > 14 and idade < 20 :
    print(f'categoria junior idade = {idade} anos apto há treinar nessa base')
elif idade == 20:
    print(f'categoria senior idade = {idade} anos apto há treinar nessa categoria')
else:
    idade > 20
    print(f'categoria master idade = {idade} anos ou maior, livre para atuar.')
    

