from random import randint
computador = randint(0,5)
print('_' * 35)
print('\033[7;34;46mTente advinhar um numero de 0 a 5\033[m')
print('-' * 35)
jogador = int(input('\033[1;32;41mem que numero eu pensei?\033[m '))
if jogador == computador:
    print('\033[1;34;42mPARABENS! você ganhou \033[m')
else:
    print(f'\033[1;34;42mGanhei escolhi {computador} e nao {jogador} \033[m')