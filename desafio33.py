
# calculo de valor maior e menor escolhido de 3 opções
a = int(input('valor  : '))
b = int(input('valor  : '))
c = int(input('valor  : '))
if a > b and a > c:
    print(f'valor maior {a}')
if b > c and b > a:
    print(f'valor maior {b}')
if c > a and c > b:
    print(f'valor maior {c}')
    
if a < b and a < c:
    print(f'valor menor {a}')
if b < c and b < a:
    print(f'valor menor {b}')
if c < a and c < b:
    print(f'valor menor {c}')
    