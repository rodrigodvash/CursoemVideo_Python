from math import trunc
print('Porção inteira')
real = float(input('Qual o número: '))
print(f'A parte inteira de {real}: {trunc(real)}/{int(real)}!')
# Na primeira, função trunc de Math; Na segunda, o casting de float para int;

