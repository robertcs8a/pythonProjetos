#calculo de tarifa de viagem por kilometragem
viagem = float(input(f'Informe a Kilometragem da Viagem :'))
if viagem <= 200:
  passagem = 0.50
  tarifa = (viagem * passagem) 
  print(f'tarifa da viagem = {tarifa:.2f}')
  print(f'foi cobrado R$ 0.50 por kilometros nesta viagem')
if viagem >=200:
    passagem = 0.45
    tarifa1 = (viagem * passagem) 
    print(f'tarifa da viagem = {tarifa1:.2f}')
    print('foi cobrado R$ 0.45 por kilometros nesta viagem')