# triangulos m2
a = int(input('digite a primeira medida: '))
b = int(input('digite a segunda medida: '))
c = int(input('digite a terceira medida: '))
equilatero = a == b == c
isósceles = a == b != c 
escaleno = a != b != c
triangulo = a + b > c and b + c > a and c + a > b
if triangulo == True == equilatero:
    print(f'sim as medidas informadas formam um triangulo equilatero ')
if triangulo == True == isósceles:
    print(f'sim as medidas informadas formam um triangulo isósceles ')
if triangulo == True == escaleno:
    print(f'sim as medidas informadas formam um triangulo escaleno ')
elif triangulo == False:
    print('não é possivel formar um triangulo com essas medidas')
    
    
