print('\033[31mOlá, mundo!\033[m')  # Letras vermelhas;
print('\033[31:43mOlá, mundo!\033[m')  # Letras vermelhas, fundo amarelo;
print('\033[1;31;43mOlá, mundo!\033[m')  # Letras em negrito, vermelhas e fundo amarelo;
print('\033[4;30;45mOlá, mundo!\033[m')  # Letras sublinhadas, brancas e fundo magenta;
print(
    '\033[30mOlá, mundo!\033[m')  # Letras brancas (Meu terminal é branco por padrão, por isso a inversão da inversão);
print('\033[7;30mOlá, mundo!\033[m')  # Letras negativas brancas;
print()
a = 3
b = 5
print(f'Os valores de a e b: \033[32ma: {a}\033[m e \033[31mb: {b}\033[m.')
print()

nome = 'Rodrigo'
sobrenome = 'Maia'
cores = {  # Um dicionário para importar as cores;
    'lear': '\033[m',
    'cyan': '\033[36m',
    'red': '\033[31m'
}
print(f'Olá, prazer em te conhecer {cores["red"]}{nome}{cores["clear"]} {cores["cyan"]}{sobrenome}{cores["clear"]}')
# dict:                               dict 'red';        dict 'clear';    dict 'cyan';             dict 'clear';
print('Olá, prazer em te ver por aqui {}{}{}.'.format('\033[1;34m', nome, '\033[m'))
