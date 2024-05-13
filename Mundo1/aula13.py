'''for t in range(0,5 +1): # CONDIÇÃO 1, variavel t conta de 0 a 4 (com +1 conta ate 5)
    print(t)
print('FIM')'''


'''n = int (input('informe um numero: '))#CONDIÇÃO 2, variavel [c] conta de 0 ate numero digitado em variavel n
for c in range(0, n+1):                 #variavel n acrescida de +1 conta de 0 ate numero final digitado
    print(c)
print('fim')'''


'''i = int(input('inicio: '))
f = int(input('Fim: '))   #CONDIÇÃO 3 variavel [f] recebe o +1 para condiderar numero final
p = int(input('Passo: '))  # variavel [p]estipula quantas vezes será o intervalo 
for c in range(i, f+1, p):
    print(c)
print('Fim')'''



s = 0                               #CONDIÇÃO 4 valor digitado em [n] o numero de vezes solicitado
for all in range (0,4):                
    n = int(input('digite um valor:')) 
    s += n                              #nessa linha essa condição é a mesma coisa  s = s + n
print(f'a soma dos numeros é = {s}')    #                                           0 = 0 + n