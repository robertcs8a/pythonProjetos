#calculo de SENO, COSENO e TANGENTE
import math
a = float(input('digite o angulo desejado: '))
seno = math.sin(math.radians(a))
print(f'o angulo de {a} tem o SENO de {seno:.2}')
coseno = math.cos(math.radians(a))
print(f'o angulo de {a} tem o COSENO de {coseno:.2}')
tangente = math.tan(math.radians(a))
print(f'o angulo de {a} tem a TANGENTE de {tangente:.2}')