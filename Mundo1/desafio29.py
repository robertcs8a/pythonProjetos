#calculo de multa por km
print('¬' * 25)
velocit = int(input('\033[1;40mo carro esta há km :\033[m '))
print('¬' * 25)
limit = 80 
if velocit > 80 :
   print(f'\033[30;41mseu veiculo sera multado pois está acima de {limit}KM/H Velocidade registrada = {velocit}KM/H\033[m')
   multa = (velocit - limit) * 7.00
   print(f'Valor da multa  R$ {multa:.2f} reais')
   if velocit > 100:
     print(f'sua habilitatação perdeu 20 pontos ')
if velocit > 150:
        print('sua habilitação sera suspensa procure um orgão responsavel')

else:
   print(f'voce esta dentro do limite permitido') 
   print('Boa Viagem....!') 
   
