
#conversão binaria,octa e hexa 
nunber = int(input('digite um numero inteiro:'))
num = ('''escolha uma opcão para conversão:
[1] Binario
[2] Octadecimal
[3] hexadecimal
''')
opção = int(input('escolha a opção: '))

bin = (bin(nunber)[2:])
if opção == 1:
    print(f'o numero binario de {nunber} é = {bin[2:]}') # carrega direto no python valor binario
oct = (oct(nunber)[2:])
if opção == 2:
    print(f'o numero octadecimal de {nunber} è = {oct[2:]}') # carrega direto no python valor octadecimal
hex = (hex(nunber)[2:])
if opção == 3:
    print(f'A represatação hexadecimal de {nunber} é = {hex[2:]}') # carrega direto no python representação hexadecimal
else:
    print('opção invalida. digite outra vez')