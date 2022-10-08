num01 = int(input('NUMERO 1 = '))
num02 = int(input('NUMERO 2 = '))
colors = {
    'clear': '\033[m',
    'red'  : '\033[31m',
    'green': '\033[32m'
}
print(f'SOMA DE {colors["red"]}{num01}{colors["clear"]} com {colors["red"]}{num02}{colors["clear"]} '
      f'= {colors["green"]}{num01 + num02}{colors["clear"]}')
