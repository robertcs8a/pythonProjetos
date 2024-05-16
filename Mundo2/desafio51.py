#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.#

primeiro = int(input('primeiro termo :'))
razão = int(input('informe a razão : '))
decimo = primeiro + (10 - 1) * razão
for c in range (primeiro, decimo + razão, razão):
     print (f'  {c} ')