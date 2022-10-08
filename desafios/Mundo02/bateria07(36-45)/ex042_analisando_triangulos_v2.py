print('Analisando triângulosVersão 2.0\n')

color = {
    'clear': '\033[m',
    'red': '\033[31m',
    'green': '\033[32m',
    'blue': '\033[34m',
    'yellow': '\033[33m'
}

# Primeiro descobrir se os segmentos de reta formam um triângulo;
print('Informe os tamanhos dos 3 segmentos (em cm):')
reta_01 = float(input('=====> '))
reta_02 = float(input('=====> '))
reta_03 = float(input('=====> '))

if reta_01 < reta_02 + reta_03 and reta_02 < reta_01 + reta_03 and reta_03 < reta_01 + reta_02:
# Ex.: r1=10, r2=12, r3=15 - 10<27 and 12<25 and 15<22 - triângulo OK;
    print(f'É possível criar um triângulo com essas medidas;')

    if reta_01 == reta_02 == reta_03:
        print(f'=> Que será do tipo {color["green"]}EQUILÁTERO{color["clear"]}.') # As três medidas são iguais;
    elif reta_01 == reta_02 or reta_01 == reta_03 or reta_02 == reta_03:
        print(f'=> Que será do tipo {color["blue"]}ISÓSCELES{color["clear"]}.') # Duas das três medidas são iguais;
    else:
        print(f'=> Que será do tipo {color["yellow"]}ESCALENO{color["clear"]}.') # As três medidas são diferentes;

else:
    print(f'{color["red"]}Não é possível criar um triângulo com estas medidas.{color["clear"]}')
