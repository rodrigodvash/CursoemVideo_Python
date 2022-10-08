print(('Classificando atletas'))

from datetime import date

color = {
    'clear': '\033[m',
    'black': '\033[7;30m',
    'red': '\033[7;31m',
    'yellow': '\033[7;33m',
    'purple': '\033[7;35m',
    'blue': '\033[7;34m',
    'green': '\033[7;32m'
}

ano_nasc = int(input('Qual o ano de nascimento do atleta? '))
ano_atual = date.today().year # Ano atual da máquina;
idade = ano_atual - ano_nasc
# Descobrir a idade do atleta fazendo a diferença entre o ano de nascimento com o ano atual;

if idade < 10: # Até 09 anos;
    print(f'Idade do atleta - {color["black"]}{idade} anos{color["clear"]}: '
          f'categoria {color["green"]}MIRIM{color["clear"]}')
elif idade < 15: # Até 14 anos;
    print(f'Idade do atleta - {color["black"]}{idade} anos{color["clear"]}: '
          f'categoria {color["blue"]}INFANTIL{color["clear"]}')
elif idade < 19: # Até 18 anos;
    print(f'Idade do atleta - {color["black"]}{idade} anos{color["clear"]}: '
          f'categoria {color["purple"]}JUNIOR{color["clear"]}')
elif idade < 26: # Até 25 anos;
    print(f'Idade do atleta - {color["black"]}{idade} anos{color["clear"]}: '
          f'categoria {color["yellow"]}SÊNIOR{color["clear"]}')
else: # Com 20 anos ou mais;
    print(f'Idade do atleta - {color["black"]}{idade} anos{color["clear"]}: '
          f'categoria {color["red"]}MASTER{color["clear"]}')