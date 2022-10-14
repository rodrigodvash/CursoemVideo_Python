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

    print('-==-' * 20)
# Resultado do jogo, conforme os valores de ambos os jogadores ///////////////////////////
    soma = valorJogador + valorPC # Verificação do resultado do jogo;
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'

# RESULTADOS! /////////////////////////////////////////////////////////////////////////////
    if resultado == jogador: # Quando o jogador vence;
        cont += 1
        print(f'\t\t\tVocê pediu {jogador}...')
        sleep(2)
        print(f'\t\t\tEeu pedi {valorPC} que deu {soma}; Deu {resultado}, você venceu {cont}x! Parabéns!')
        print('-==-' * 20)

    else:
        print(f'\t\t\tVocê pediu {jogador}...')
        sleep(2)
        print(f'\t\t\tE eu pedi {valorPC} que deu {soma}; Deu {resultado}, você perdeu!')
        print('-==-' * 20)
        break