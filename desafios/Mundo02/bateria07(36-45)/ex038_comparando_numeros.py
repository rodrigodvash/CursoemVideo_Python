print('Comparando números\n')

color = {
    'clear': '\033[m',
    'red': '\033[31m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
}

print('-=-' * 10)
numero_01 = int(input('Informe o primeiro número: '))
numero_02 = int(input('Informe o segundo número: '))
print('-=-' * 10)

if numero_01 > numero_02:
    print(f'O {numero_01} {color["yellow"]}é maior que o{color["clear"]} {numero_02}!')
elif numero_01 < numero_02:
    print(f'O {numero_01} {color["blue"]}é menor que o{color["clear"]} {numero_02}!')
else:
    print(f'São iguais: {color["red"]}{numero_01} = {numero_02}{color["clear"]}!')
print('-=-' * 10)
