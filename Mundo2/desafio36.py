import math
#emprestimo bancario
cliente = str(input('Ola! qual é o seu nome :'))
print(f'tudo bem ! "{cliente}" pode me informar o valor da casa pretendida : ')

casa = float(input('valor:'))
print(f'Ótimo! me informe o seu salario :')
salario = float(input('salario :'))
porcen = (salario * 30 / 100)
print(f'de acordo com seu salario seu limite mensal é de {porcen}')

anos = int(input(f'obrigado! em quantos anos  pretende pagar esse imovel :'))
meses = (12 * anos) 
prestaçao = casa / meses 
if prestaçao < porcen:
 print(f'A quantidade de parcelas do seu contrato será de {meses} vezes de {prestaçao:.2f}')
else:
    print(f'O valor calculado é de {prestaçao} mensais lamento mais excedeu o seu limite ')
