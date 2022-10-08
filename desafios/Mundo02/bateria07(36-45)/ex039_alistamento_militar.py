print('Alistamento militar')

from datetime import date

color = {
    'clear': '\033[m',
    'red': '\033[30;41m',
    'cyan': '\033[36m',
    'green': '\033[32m',
    'yellow': '\033[33m'
}

ano_nasc = int(input('Em que ano o jovem nasceu? '))
ano_atual = date.today().year # Pegar o ano atual do PC;
idade = ano_atual - ano_nasc # Descobrir a idade do jovem;

if idade < 18:
    print(f'O jovem possui {idade} anos, {color["cyan"]}faltam {18 - idade} anos para o seu alistamento{color["clear"]}.')
elif idade == 18:
    print(f'O jovem tem {idade} anos! {color["green"]}Está na hora de seu alistamento!!{color["clear"]}')
elif idade > 18 and idade <= 100:
    print(f'O \'jovem\' tem {idade} anos... {color["yellow"]}Se passaram {idade - 18} anos do seu alistamento!{color["clear"]}\n'
          f'Procure um posto militar para prestar declarações.')
else:
    print(f'{color["red"]}O que o senhor veio fazer aqui?{color["clear"]}')