# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas 
 #ainda não atingiram a maioridade e quantas já são maiores.
print('¨'* 95)

print("Esse programa vai coletar 7 datas de nascimento e informar quantos são maior e menor de idade")

print('¨'*95)

from datetime import date
atual = date.today().year
tmaior = 0
tmenor = 0
for pess in range(1,8):
    nasc = int(input(f'Em que ano a {pess}ª pessoa nasceu? \33[0;0m'))
    idade = atual - nasc
    
    if idade >= 21:
        tmaior += 1
    else:
       tmenor += 1
print(f"Pessoas  maiores de idade {tmaior}")
print(f"Pessoas menores de iadade {tmenor}")
       