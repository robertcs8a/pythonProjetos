#Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três. 
#E que se encontram no intervalo de 1 até 500.
s = 0
cont = 0
for n in range(1,501, 2):
    if n % 3 == 0:
       s = s + n
       cont = cont + 1
print(f'soma = {s}')
print(f'encontrados:{cont} multiplos de 3')
       
