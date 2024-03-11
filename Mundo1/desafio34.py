  # calculando aumento de salario
salario = int(input('digite o salario do funcionario :'))
porc_ = salario + (salario * 10 / 100 ) 
porc_1 = salario + (salario * 15 / 100 ) 
if salario <= 1250:
    print(f'O Funcinario recebeu :{salario} este mes e teve um aumento de 15% total de :\033[33m {porc_1}\033[m')
if salario >= 1250 :
    print(f' O Funcinario recebeu :{salario} este mês e teve um aumento de 10% total de :\033[33m {porc_}\033[m')
