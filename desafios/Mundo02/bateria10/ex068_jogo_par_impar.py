from random import randint, choice
from time import sleep

print(f'Jodo de Par ou Ímpar'.center(70))
print('-==-' * 20)

sorteio = ['PAR', 'IMPAR'] # Escolhas do PC;
soma = 0                   # Resultado do par ou ímpar;
empate = 0                 # Se empatar mais de 3x, o jogo termina;
cont = 0                   # Conta quantas vezes seguidas o jogador venceu;

while True:
# Dados do jogador /////////////////////////////////////////////////////////////////////
    valorJogador = int(input('\t\t\tDiga um valor: '))
    jogador = str(input('\t\t\tPAR ou ÍMPAR [P/I]? ')).strip().upper()[0]
    while jogador not in 'PI': # Garantir que o jogador escolha ou par ou ímpar;
        jogador = str(input('\t\t\tÉ PAR ou É ÍMPAR [P/I]! ')).strip().upper()[0]
    if jogador == 'P':
        jogador = 'PAR'
    elif jogador == 'I':
        jogador = 'IMPAR'

# Dados do PC ////////////////////////////////////////////////////////////////////////////
    valorPC = randint(0, 10) # Faixa de valores para a soma do PC;
    pc = choice(sorteio)      # Escolha do PC: par ou impar;
    print(f'\t\t\tEu vou pedir...', end='')
    sleep(1.5)
    print(f' {pc} ', end='')
    print(f'e vou jogar...', end='')
    sleep(1.5)
    print(f' {valorPC}!')
    sleep(1)

# Resultado do jogo, conforme os valores de ambos os jogadores ///////////////////////////
    soma = valorJogador + valorPC # Verificação do resultado do jogo;
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'

# RESULTADOS! /////////////////////////////////////////////////////////////////////////////
    if resultado == jogador and resultado != pc: # Quando o jogador vence;
        cont += 1
        print(f'\t\t\tEu pedi {pc} e você {jogador}...')
        sleep(2)
        print(f'\t\t\tDeu {soma} que é {resultado}, você venceu {cont}x! Parabéns!')

    elif resultado != jogador and resultado == pc: # Quando o PC vence;
        print(f'\t\t\tEu pedi {pc} e você {jogador}...')
        sleep(2)
        print(f'\t\t\tDeu {soma} que é {resultado}, você perdeu! Adeus!')
        break

    else: # Quando gera um empate;
        if empate < 3:
            sleep(2)
            print(f'\t\t\tDeu {soma} que é {resultado}, pedi {pc} e você {jogador} e EMPATAMOS.')
            print('-==-' * 20)
            # Num empate, será perguntado ao jogador se ele deseja uma 'revanche';
            again = str(input('\t\t\tQuer jogar mais uma vez? ')).strip().upper()[0]
            if again in 'SY': # Se sim;
                empate += 1
                continue
            elif again in 'N': # Se não;
                print('\t\t\tOk, até mais!')
                break
            else: # Se ele for estúpido;
                print('\t\t\tNão entendi sua resposta, entõ estou de partida, adeus!')
                break
        else: # Mais de 3 empates;
            print(f'\t\t\tEmpatamos {empate}x, vamos considerar um empate de uma vez por todas...')
print('-==-' * 20)
