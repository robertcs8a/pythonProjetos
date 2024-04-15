'''

'''

import math
nome = input('Qual é o seu nome ')

print(f'Olá {nome} pode me informar seu peso :')
peso = float(input('digite aqui seu peso (KG) = '))

print('Qual é a sua altura? ')
altura = float(input('digite aqui sua altura (m) = '))

calculo = (peso / altura**2)
print(f'IMC calculado: {calculo:.2f} veja sua classificação')

if calculo < 18.5:
    print('Voce esta baixo do peso')
elif calculo >= 18.5 and calculo < 25:
    print('seu peso é o ideal')
elif calculo >= 25 and calculo < 30:
    print(' Voce esta com sobrepeso')
elif calculo >= 30 and calculo < 40:
    print(' Seu IMC indica obesidade')   
else:
    calculo >= 40
    print(' Seu IMC esta acima de 40 voce esta com Obesidade mórbida')