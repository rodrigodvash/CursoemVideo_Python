print(f'{" TABELA BRASILEIRÃO 2022 ":^100}')
print('-==-' * 30)

times = ('Palmeiras', 'Internacional', 'Corinthians', 'Flamengo', 'Fluminense',
         'Athletico-PR', 'Atlético-MG', 'América-MG', 'Botafogo', 'Fortaleza',
         'Santos', 'São-Paulo', 'Bragantino', 'Goiás', 'Coritiba',
         'Ceará SC', 'Cuiabá', 'Atlético-GO', 'Avaí', 'Juventude')

print('Os cinco primeiros colocados da tabela (vista no dia 11/10/2022) são em ordem:')
print(f'Ordem dos 5 primeiros colocados: {times[0:5]};\n')
print(f'\t1º colocado: {times[0]} com 67 pontos;\n\t2º colocado: {times[1]} com 57 pontos;\n'
      f'\t3º colocado: {times[2]} com 54 pontos;\n\t4º colocado: {times[3]} com 52 pontos;\n'
      f'\t5º colocado: {times[4]} com 51 pontos;')
print('-==-' * 30)

print('Os últimos quatro colocados da tabela (vista no mesmo dia 11/10/2022) são em ordem:')
print(f'Os quatro últimos: {times[-4:]}\n')
print(f'\t17º colocado: {times[-4]} com 30 pontos;\n\t18º colocado: {times[-3]} com 29 pontos;\n'
      f'\t19º colocado: {times[-2]} com 28 pontos;\n\t20º colocado: {times[-1]} com 20 pontos;')
print('-==-' * 30)

print('Estes times em ordem alfabética ficam:')
print(f'{sorted(times)}')
print('\nE em ordem alfabética ao contrário:')
print(f'{sorted(times, reverse=True)}')
print('-==-' * 30)

print('{:^100}'.format(f'O Corinthians está na {times.index("Corinthians")+1}º posição;'))
print('-==-' * 30)
