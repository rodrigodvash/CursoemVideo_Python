print('Conversor de bases numéricas')

color = {
    'clear' : '\033[m',
    'red'   : '\033[7;41m',
    'green' : '\033[4;32m',
    'yellow': '\033[4;33m',
    'blue'  : '\033[4;34m'
}

numero = int(input('Informe o número a ser convertido: '))
converter = int(input(f'E a base de conversão '
                      f'({color["green"]}1-Binário{color["clear"]}, '
                      f'{color["yellow"]}2-Octal{color["clear"]}, '
                      f'{color["blue"]}3-Hexadecimal{color["clear"]}): '))

if converter == 1:
    convertido = format(numero, 'b')
    print(f'O número {numero} convertido para o {color["green"]}sistema binário{color["clear"]} fica {color["green"]}{convertido}{color["clear"]}.')
    # A função str(bin()) também converte para binário;

elif converter == 2:
    convertido = format(numero, 'o')
    print(f'O número {numero} convertido para o {color["yellow"]}sistema octal{color["clear"]} fica {color["yellow"]}{convertido}{color["clear"]}.')
    # A função str(oct()) também converte para octal;

elif converter == 3:
    convertido = format(numero, 'x')
  # convertido = format(numero, 'X') Converte o valor para o formato Hex em maiúsculas;
    
    print(f'O número {numero} convertido para o {color["blue"]}sistema hexadecimal{color["clear"]} fica {color["blue"]}{convertido}{color["clear"]}.')
    # A função str(hex()) também converte para hexadecimal;

else:
    print(f'{color["red"]}Você não selecionou nenhuma das opções válidas e vai ficar sem conversão!{color["clear"]}')
