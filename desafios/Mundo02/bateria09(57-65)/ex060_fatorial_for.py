numero = int(input('Valor para o fatorial: '))
fatorial = 1

for i in range(numero, 1, -1):
    fatorial *= i

print(f'{numero}! = {fatorial}')
