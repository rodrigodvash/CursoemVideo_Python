# import math
from math import sqrt

num = int(input('Digite um número: '))
# raiz = math.sqrt(num)  Quando a biblioteca é toda importada, é assim que se chama uma das funções;
raiz = sqrt(num)  # Quando se importa somente uma função específica basta chamá-la;

#print(f'A raiz de {num} é {math.ceil(raiz)}')  Arredonda para cima;
#print(f'A raiz de {num} é {math.floor(raiz)}')  Arredonda para baixo;
print(f'A raiz de {num} é {raiz:.2f}')

