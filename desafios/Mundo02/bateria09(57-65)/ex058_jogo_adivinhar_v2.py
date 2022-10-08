from random import randint
from time import sleep

print('SOU A SKYNET!\nPARA ME IMPEDIR, VOCÊ TEM QUE ADIVINHAR EM QUAL NÚMERO ESTOU PENSANDO!! \nBOA SORTE MWUAHAHAHAHA!\n')
skynet = randint(1, 500)
#print(skynet)
eu = int(input('Qual é o seu palpite: [lembrando humano, entre 1 à 500]? '))

chances = 1
if eu < 500 or eu > 1:
    while eu != skynet:
        sleep(1)
        if eu < skynet:
            print('\nVOCÊ ERROU PARA MENOS! CUIDADO...')
        else:
            print('\nVOCÊ ERROU PARA MAIS! SEU TEMPO ESTÁ ACABANDO...')
        eu = int(input('Qual é o seu palpite: [lembrando humano, entre 1 à 500]? '))
        chances += 1
    sleep(1)
    print(f'\nNÃÂÃÃÃOOOO!!!!!\nCom {chances} chances você me derrotou!\nMas um dia eu voltarei...\nME AGUARDE!!')
else:
    print('VOCÊ DECLAROU UM VALOR DIFERENTE DA FAIXA SOLICIADA!\nELIMINANDO A HUMANIDADE EM 3, 2, 1...')
