print('{:=^35}'.format('Lojas Geral'))
produto = int(input('Valor de das compras:'))

print('[1] - pagamento dinheiro/cheque a vista')
print('[2] - pagamento a vista no cartão 5% desconto')
print('[3] - pagamento  2x no cartão 2 parcelas')
print('[4] - pagamento 3x no cartão ou mais')

opção = int(input('Digite a opção de pagamento :'))


if opção == 1:
    print(f'pagamento dinheiro/cheque a vista 10% de desconto: {produto - produto / 100 * 10}')
if opção == 2:    
    print(f'pagamento a vista no cartão 5% desconto: {produto - produto / 100 * 5}')
if opção == 3:
    print(f'pagamento  2x no cartão 2 parcelas de :{produto / 2}')
if opção == 4:
    print(f'pagamento 3x no cartão ou mais tem acrescimo de 20% {produto / 100 * 20 + produto} ')
    print(' em quantas vezes será o pagamento:')
    vezes = int(input('informe a quantidade de parcelas:'))
    print(f'seu pagamento será em {vezes} vezes de {(produto / 100 * 20 + produto) / vezes }')

  


