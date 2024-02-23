print('Analise da quantida, posiçao inicial e final que aparece a letra "a" no texto ')

frase = str(input('informe um texto a ser verificado : ')).upper().lower().strip()

print(f'A letra a aparece {frase.count('a')} vezes no texto')
print(f'A primeira letra a aparece na posição {frase.find('a')+1} ')
print(f'A segunda letra a aparece na posição {frase.rfind('a')+1}')
###Nessa aula, vamos aprender operações com String no Python. As principais operações  ###