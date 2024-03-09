# comando randonico sorteio aleatorio
import random
print('sorteio do professor para escolher aluno que pode ajuda-lo')
p1 = input('aluno um :')
p2 = input('aluno dois :')
p3 = input('aluno três :')
p4 = input('aluno quatro :')
lista = [p1, p2, p3, p4]
sorteio = random.choice(lista)
print(f'o aluno que vai apagar a lousa é : {sorteio}')
