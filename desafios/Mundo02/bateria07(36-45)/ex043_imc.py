print('IMC\n')

color = {
    'clear': '\033[m',
    'red': '\033[7;31m',
    'blue': '\033[7;34m',
    'green': '\033[7;32m',
    'yellow': '\033[7;33m',
    'purple': '\033[7;35m'
}

print('-=-' * 10)
print('Descobrindo seu IMC!')
print('-=-' * 10, '\n')

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura * altura) # Fórmula do IMC;

if imc < 18.5:
    print(f'{color["blue"]}Você está abaixo do peso ideal!{color["clear"]}')
elif imc < 25:
    print(f'{color["green"]}Você está com o peso ideal!{color["clear"]}')
elif imc < 30:
    print(f'{color["yellow"]}Você está acima do peso ideal!{color["clear"]}')
elif imc < 40:
    print(f'{color["purple"]}Você está com obesidade!{color["clear"]}')
else:
    print(f'{color["red"]}Você está com obesidade mórbida!{color["clear"]}')