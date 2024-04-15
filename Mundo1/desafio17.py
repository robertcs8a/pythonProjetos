#cauculo de hipotenusa (hypot importação direta da biblioteca math)
import math
cat_opost = float(input('imforme a medida do cateto oposto :'))
cat_adjacent = float(input('informe a medida do cateto ajacente :'))
hi = math.hypot(cat_opost, cat_adjacent)
print(f'a hipotenusa é = {hi:.2}  ')
