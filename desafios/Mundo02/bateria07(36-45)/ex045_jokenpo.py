print('Jogo de jokenpô\n')

from random import choice
from time import sleep

color = {
    'clear': '\033[m',
    'backcyan': '\033[7;36m',
    'backwhite': '\033[7;30m',
    'red': '\033[1;31m',
    'yellow': '\033[1;33m',
    'green': '\033[1;32m',
    # Quando a máquina ganhar:
    'backred': '\033[7;31m',
    # Quando o jogador ganhar:
    'backgreen': '\033[7;32m',
    # Quando der um empate:
    'backyellow': '\033[7;33m',
    # Quando o jogador 'der uma' de idiota:
    'backblue': '\033[7;34m'
}

print(f'{color["backcyan"]}-={color["clear"]}' * 25)
print(f'{color["backwhite"]}Olá, vamos jogar Pedra, Papel ou Tesoura?{" " * 9}{color["clear"]}')
print(f'{color["backcyan"]}-={color["clear"]}' * 25)

print(f'\n{color["backwhite"]}Escolha entre um dos 3:{" " * 27}{color["clear"]}')
print(f'\t{color["red"]}Aperte 1 para PEDRA;{color["clear"]}\n'
      f'\t{color["yellow"]}Aperte 2 para PAPEL;{color["clear"]}\n'
      f'\t{color["green"]}Aperte 3 para TESOURA;{color["clear"]}')
jogador = int(input('===> ')) # Tentativa do jogador;

print(f'{color["backwhite"]}-={color["clear"]}' * 25)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
# Leve suspense!

maquina = ['PEDRA', 'PAPEL', 'TESOURA']
jokenpo = choice(maquina) # Escolha da máquina;

if jogador < 4 and jogador > 0: # Resultado deve estar entre 1 E 3;
    if jokenpo == "PEDRA": # A máquina soteia Pedra;
        if jogador == 3: # Jogador tenta Tesoura;
            print(f'{color["backred"]}Eu venci! Tirei {jokenpo} que ganha de TESOURA.{" " * 7}{color["clear"]}')
        elif jogador == 2: # Jogador tenta Papel;
            print(f'{color["backgreen"]}Você venceu! Tirei {jokenpo}, que perde para PAPEL.{" "  * 3}{color["clear"]}')
        elif jogador == 1: # Jogador tenta Pedra;
            print(f'{color["backyellow"]}Opa, tirei {jokenpo} e EMPATAMOS.{" " * 21}{color["clear"]}')

    elif jokenpo == "PAPEL": # A máquina sorteia Papel;
        if jogador == 1: # Jogador tenta Pedra;
            print(f'{color["backred"]}Eu venci! Tirei {jokenpo} que ganha de PEDRA.{" " * 9}{color["clear"]}')
        elif jogador == 3: # Jogador tenta Tesoura;
            print(f'{color["backgreen"]}Você venceu! Tirei {jokenpo}, que perde para TESOURA. {color["clear"]}')
        elif jogador == 2: # Jogador tenta Papel;
            print(f'{color["backyellow"]}Opa, tirei {jokenpo} e EMPATAMOS.{" " * 21}{color["clear"]}')

    elif jokenpo == "TESOURA": # A máquina sorteia Tesoura;
        if jogador == 2: # Jogador tenta Papel;
            print(f'{color["backred"]}Eu venci! Tirei {jokenpo} que ganha de PAPEL.{" " * 7}{color["clear"]}')
        elif jogador == 1: # Jogador tenta Pedra;
            print(f'{color["backgreen"]}Você venceu! Tirei {jokenpo}, que perde para PEDRA. {color["clear"]}')
        elif jogador == 3: # Jogador tenta Tesoura;
            print(f'{color["backyellow"]}Opa, tirei {jokenpo} e EMPATAMOS.{" " * 19}{color["clear"]}')
else:
    print(f'{color["backblue"]}Você é idiota? Eram 3 opções cara, meu Deus.{" " * 6}{color["clear"]}')

print(f'{color["backwhite"]}-={color["clear"]}' * 25)

'''Em todas as tentativas,a ordem ficou como:
A máquina vence, ou o jogador vence, ou gera um empate.'''
