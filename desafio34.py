  # calculando almento de salario
salario = int(input('digite o salario do funcionario :'))
porc_ = (salario / 100) * 10 + salario
porc_1 = (salario / 100) * 15 + salario
if salario > 1250:
    print(f'O Funcinario recebeu :{salario} este mes e teve um aumento de 10% total de : {porc_1}')
if salario < 1250 and salario == 1250:
    print(f' O Funcinario recebeu :{salario} este mês e teve um aumento de 10% total de : {porc_}')
