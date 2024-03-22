students = str(input('Informe o nome do aluno: '))
nota1 = float(input(f'digite a primeira nota do aluno {students} é : '))
nota2 = float(input(f'digite a segunda nota do aluno {students} é : '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'O aluno {students} não atingiu a media e está reprovado com a nota de {media}')
elif media > 5.0 and media < 6.9:
    print(f'O aluno {students} atigiu média condicional a recuperação com a nota de {media}')
else:
    media > 7.0
    print(f'O aluno {students} atigiu a media que o condiciona como aprovado com a nota de {media}')
        