print('Maior e menor')
a = int(input('VALOR A: '))
b = int(input('VALOR B: '))
c = int(input('VALOR C: '))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print(f'O maior é {maior} e o menor é {menor}.')
