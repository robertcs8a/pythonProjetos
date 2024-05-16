'''Exercício Python 50: Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.'''
s = 0
cont = 0
for c in range (1, 7):
    number = int(input(f'digite o {c}º valor : '))
    if number % 2 == 0:
        s = s + number
        cont = cont + 1
print(f'numeros pares digitados {cont} a soma dos numeros é : {s}')
    
   