'''Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
# alistamento
atual = date.today().year 

data_nasc = int(input('Qual é a sua data de nascimento? '))

print(data_nasc)

idade = (atual - data_nasc)

print(idade)

if idade == 18:
    
    print(f'quem nasceu em {data_nasc} tem {idade} anos em {atual}.\nE esta no momento exato para se alistar ')
    
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(f' quem nasceu em  {data_nasc} tem {idade} anos e já passou  {saldo} anos\n E deveria se alistar em {ano} ')
    
else:
    saldo =  18 - idade
    ano = atual + saldo
    print(f' quem nasceu em  {data_nasc} tem {idade} anos e ainda faltam  {saldo} anos\n E deve se alistar em {ano}  ')