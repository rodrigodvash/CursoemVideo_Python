from random import randint
from time import sleep

print('Adivinhar\n')
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, qual você acha que é?')
print('-=-' * 20)

numero = int(input('=> ')) # Número do jogador;
print('PROCESSANDO...')
sleep(2) # Pausa que o PC faz;

adivinhar = randint(0, 5) # Número do PC;
if numero == adivinhar:
    print('-=-' * 20)
    print('\w/ \w/  Acertô, mizeravi!  \\\o \o/ o//')
    print('-=-' * 20)
else:
    print('-=-' * 20)
    print(f'Fuon, fuon, fuononuonuon... Você errou! Pensei no {adivinhar}!!')
    print('-=-' * 20)
