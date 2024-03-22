
#conversão binaria,octa e hexa 
nunber = int(input('digite um numero inteiro:'))
bin = (bin(nunber)[2:])
print(f'o numero binario de {nunber} é = {bin}') # carrega direto no python valor binario
oct = (oct(nunber)[2:])
print(f'o numero octadecimal de {nunber} è = {oct}') # carrega direto no python valor octadecimal
hex = (hex(nunber)[2:])
print(f'A represatação hexadecimal de {nunber} é = {hex}') # carrega direto no python representação hexadecimal