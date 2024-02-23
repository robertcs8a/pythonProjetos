velocit = int(input('o carro esta há km :'))
limit = 80 
if velocit > 80 :
   print(f'seu veiculo sera multado pois está acima de {limit}! Velocidade = {velocit}')
   multa = (velocit - limit) * 7.00
   print(f'Valor da multa {multa}')
   if velocit > 100:
     print(f'sua habilitatação  esta suspensa')

else:
   print(f'voce esta dentro do limite permitido')  
   
