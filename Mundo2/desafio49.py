'''Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher
só que agora utilizando um laço for.'''

n = int(input('type a number : '))
for c in range(1,11):
    print(f' {n:2} x  {c} = {n * c:2}') #range de a 1,11 multiplica a variavel n por c que recebe numeros do forgi