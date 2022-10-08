from math import hypot, sqrt, pow

print('Hipotenusa')
catOposto = float(input('Qual o cateto oposto: '))
catAdjacente = float(input('Qual o cateto adjacente: '))
hipotenusa = hypot(catOposto, catAdjacente)
print(f'A hipotenusa de {catOposto:.2f} com {catAdjacente:.2f} é: {hipotenusa:.2f}')
print(f'Assim também é possível: {sqrt(pow(catOposto, 2) + pow(catAdjacente, 2)):.2f}')
print(f'Assim também é possível: {(catOposto ** 2 + catAdjacente ** 2) ** (1/2):.2f}')

