
# alistamento
data_nac = int(input('Qual é sua data de nascimento? '))
print(f'data de nascimento informada = {data_nac}') 
idade = int(2024 - data_nac)
menor_maior =  int (data_nac - 2006) # resultado = 0 o valor é sempre 18
if idade < 18:
    print(f'sua idade é {idade} anos faltam {menor_maior} anos para voce se alistar')
if idade > 18:
    print(f'voce agora já esta com  {idade} anos e já passou {menor_maior} anos do periodo de se alistar ')
elif menor_maior == 0:
    print('parabens sua idade é 18 anos ideal para se alistar')
    
    
