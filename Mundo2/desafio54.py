# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas 
 #ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
tmaior = 0
tmenor = 0
for pess in range(1,8):
    nasc = int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
    idade = atual - nasc
    
    if idade >= 21:
        tmaior += 1
    else:
       tmenor += 1
print(f"Pessoas  maiores de idade {tmaior}")
print(f"Pessoas menores de iadade {tmenor}")
       