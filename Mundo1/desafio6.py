from math import ceil
n = float( input('digite um numero: '))
dobro: float = (n * 2)
triplo: float = (n * 3)
raiz: float = n ** (1/2)
print(f' o dobro de {n} é  {dobro} \n o triplo de {n} é {triplo}\n a raiz quadrada de {n} é {ceil(raiz)}')