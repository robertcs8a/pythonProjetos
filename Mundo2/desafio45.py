from random import randint

print('[1] pedra')
print('[2] papel')
print('[3] tesoura')
print('JO')
print('KEN')
print('PO!!!')

jogador = int(input('escolha uma opção : '))
pc = randint(1,3)
if pc == 1:                           #condiçôes se a escolha do computador for [1]
    print('computador jogou pedra')
    if jogador == 1:
        print('EMPATE')
        print('jogador jogou pedra')
    elif jogador == 2:
        print(f'jogador venceu')
        print('jogador jogou papel')
    else:
        jogador == 3
        print('computador venceu')
        print('jogador jogou tesoura')
#========================================================================================#   
   
elif pc == 2:                        #condiçôes se a escolha do computador for [2]
    print('computador jogou papel')
    if jogador == 2:
        print('EMPATE')
        print('jogador jogou papel')
    elif jogador == 3:
        print('jogador venceu ')
        print('jogador jogou tesoura')
    else:
        jogador == 1
        print('computador  venceu')
        print('jogador jogou pedra')
#===========================================================================================#

elif  pc == 3:                        #condiçôes se a escolha do computador for [3]
    print('computador jogou tesoura')
    if jogador == 3:
        print('empate')
        print('jogador jogou tesoura')
    elif jogador == 2:
        print('computador ganhou')
        print('jogador jogou papel')
    else:
        jogador == 1
        print('jogador ganhou')
        print('jogador jogou pedra')
else:
    print('numero errado')
    
#=========================================================================================#

