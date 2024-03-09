# classificando numero por unidades
number = int(input('Informe um numero :'))
unit = number // 1 % 10
dez = number // 10 % 10
cent = number // 100 % 10
milhar = number // 1000 % 10
print(f'Unidade: {unit}')
print(f'Dezena: {dez}')
print(f'Centena: {cent}')
print(f'Milhar: {milhar}')