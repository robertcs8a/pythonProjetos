from random import randint

print('[1] pedra')
print('[2] papel')
print('[3] tesoura')

jogador = int(input('escolha uma opção : '))
pc = randint(1,3)
if pc == 1:                           #condiçôes de a escolha do computador for [1]
    print('computador jogou pedra')
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print(f'jogador venceu')
    else:
        jogador == 3
        print('computador venceu')
#========================================================================================#   
   
elif pc == 2:                        #condiçôes se a escolha do computador for [2]
    print('computador jogou papel')
    if jogador == 2:
        print('EMPATE')
    elif jogador == 3:
        print('jogador venceu')
    else:
        jogador == 1
        print('jogador venceu')
#===========================================================================================#

elif  pc == 3:                        #condiçôes se a escolha do computador for [3]
    print('computador jogou tesoura')
    if jogador == 3:
        print('empate')
    elif jogador == 2:
        print('computador ganhou')
    else:
        jogador == 1
        print('jogador ganhou')
else:
    print('erro execute novamente ')
    
#=========================================================================================#

if jogador == 1:
    print('jogador escolheu pedra')
elif jogador == 2:
    print('jogador escolheu papel')
                            
elif jogador == 3:
    print('jogador escolheu tesoura')
else:
    print('erro escolha outra vez')
    



   
