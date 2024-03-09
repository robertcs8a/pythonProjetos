
# calculo de valor maior e menor escolhido de 3 opções
a = int(input('valor  : '))
b = int(input('valor  : '))
c = int(input('valor  : '))
# valor maior

maior = a   
if  b > a and b > c:
    print(f'valor maior {b}')
if c > a and c > b:
    print(f'valor maior {c}')
 # valor menor
 
menor = a   
if b < a and b < c:
    print(f'valor menor {b}')
if c < a and c < b:
    print(f'valor menor {c}')
    