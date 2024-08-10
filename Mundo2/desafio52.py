# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.#
# números em azul divisiveis, apenas duas vezes indicam números primo.#


núm = int(input("digite um número: "))
total = 0
for c in range(1, núm + 1):
    if núm % c == 0:
       print ("\033[34m", end='')
       total += 1
    else:
       print("\033[32m" , end='')
    print(f"{c} ", end='')
print(f'\n \033[0;0mO número {núm} foi divisivel {total} vezes')
if total == 2:
    print(f'por isso o número: ({núm}) é um primo.')
else:
    print(f'por isso o número: ({núm}) não é um primo.')

