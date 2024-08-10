# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

frase = str(input('digite uma frase: ')).strip() .upper() # strip tira espaço antes e depois/ upper torna tudo em maiusculo
palavras = frase.split()                             # split separa as palvras em lista ex:['óla','mundo']
junto = ''.join(palavras)                           # join atribui no espaço entre frases o que estiver no campo '' se vazio elimina espaço
print(f'voce digitou a frase = {junto}')
inverso = ''
for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('não temos um palindromo')
    
