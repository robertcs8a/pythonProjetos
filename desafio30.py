# localiza numeros (par) e (impar)
n = int(input(f'\033[1;34;43minforme um numero:\033[m '))
print(f' numero escolhido {n} ')
if n % 2 == 0:
  print(f'{n} = numero par')
else:
  print(f'{n} = numero impar')
