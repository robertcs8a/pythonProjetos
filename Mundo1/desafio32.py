print('programa que informa anos bissexto')
ano = int(input('digite aqui o ano para ser analizado :'))
if ano % 4 == 0 or ano % 400 == 0 and ano % 100 !=0:     
       print(f'sim {ano} é um ano bisexto')
else:
       print(f'não {ano} não é um ano bisexto')
     
       