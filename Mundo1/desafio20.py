from random import shuffle

a1 = input('Aluno um :')
a2 = input('Aluno dois :')
a3 = input('Aluno três :')
a4 = input('Aluno quatro :')
lista = [a1, a2, a3, a4]
shuffle(lista)

print(f'sequencia para apresentação {lista}')
