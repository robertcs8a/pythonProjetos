nome1: str
cont = 0
nome1 = input('Nome do aluno : ')
while nome1 != 0:
    cont = cont + nome1:
 print(f'olá {nome1}, seja bem vindo.')
x = float(input(f'entre com a primeira nota do aluno {nome1} :'))
y = float(input(f'entre com a outra nota do aluno  {nome1} :'))
conta1 = (x + y) / 2
if conta1 < 3:
    print('vc foi reprovado')
elif conta1 > 5:
    print('Parabens vc esta aprovado')
else:
    print('vc esta de recuperação')
nota1 = input(f'{nome1} a sua nota media é :{conta1} ')
#----------------------------------------------------------#
nome2 = input('Nome do aluno : ')
print(f'olá {nome2}, seja bem vindo .')
h = float(input(f'entre com a primeira nota de: {nome2} '))
g = float(input(f'entre com a outra nota de : {nome2} '))
conta2 =  (h + g) / 2
if conta2 < 3:
    print('voce esta reprovado')
elif conta2 > 5:
    print('Parabens voce esta aprovado')
else:
    print('voce esta de recuperação')
nota2 = input(f'{nome2} a sua nota media é :{conta2}')
