# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho 
# e quantas mulheres têm menos de 20 anos.
somaidade = 0
médiaidade = 0
maioridadehom = 0
nomedomaisvelho = ''
mulher20 = 0

for dados in range(1, 5):
    print(f"--------\33[031{dados}[mª pessoa ----")
    nome = str(input("informe o nome :")).strip()
    idade = int(input("infome a idade :"))
    sexo = str(input("qual é o sexo [M/F]:")).strip()
    print(f"nome = {nome}, idade = {idade}, sexo = {sexo}")   
    somaidade += idade
    print('=' * 35)
    if dados == 1 and sexo in 'MN':
        maioridadehom = idade
        nomedomaisvelho = nome
    if sexo in 'Mn' and idade > maioridadehom:
        maioridadehom = idade
        nomedomaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
        
médiaidade = somaidade / 4
print(f"idade media do grupo é de {médiaidade} anos")
print(f"O nome do homen mais velho é {nomedomaisvelho} e sua idade é {maioridadehom} anos")
print(f"tem no grupo {mulher20} mulher com menos de 20 anos  ")



    
    
    
