# calculo para identificar se medidas podem formar um  tringulo
a = int(input('digite a primeira medida: '))
b = int(input('digite a segunda medida: '))
c = int(input('digite a terceira medida: '))
triangulo = a + b > c and b + c > a and c + a > b
if triangulo == True:
    print(f'sim as medidas informadas formam um triangulo')
else:
    print('não é possivel formar um triangulo com as medidas infomadas')