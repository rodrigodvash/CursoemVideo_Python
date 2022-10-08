print('Fatorial!\n')

# Valor de entrada;
numero = int(input('Valor para o fatorial: '))
# Index para contagem do loop;
index = numero
# Fator neutro da multiplicação;
fatorial = 1

# Enquanto index mnor que 0 (sempre -1 que o valor de entrada);
while index > 0:
    print(f'{index}', end='')
    print(' x ' if index > 1 else ' => ', end='')
    fatorial *= index # 1 * index (5, por exemplo);
    index -= 1

print(f'{numero}! = {fatorial}.')
