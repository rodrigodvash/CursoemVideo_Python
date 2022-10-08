print('Contagem regressiva')
from time import sleep
import emoji

print(f'CONTAGEM REGRESSIVA'.center(40))

# Emojis
dez = emoji.emojize(f' :guitar: DEZ :keycap_10: DEZ :guitar: ', language='alias')
nove = emoji.emojize(f' :musical_score: NOVE :keycap_9: NOVE :musical_score: ', language='alias')
oito = emoji.emojize(f' :drum: OITO :keycap_8: OITO :drum: ', language='alias')
sete = emoji.emojize(f' :saxophone: SETE :keycap_7: SETE :saxophone: ', language='alias')
seis = emoji.emojize(f' :microphone: SEIS :keycap_6: SEIS :microphone: ', language='alias')
cinco = emoji.emojize(f' :banjo: CINCO :keycap_5: CINCO :banjo: ', language='alias')
quatro = emoji.emojize(f' :violin: QUATRO :keycap_4: QUATRO :violin: ', language='alias')
tres = emoji.emojize(f' :musical_keyboard: TRÊS :keycap_3: TRÊS :musical_keyboard: ', language='alias')
dois = emoji.emojize(f' :trumpet: DOIS :keycap_2: DOIS :trumpet: ', language='alias')
um = emoji.emojize(f' :headphone: UM :keycap_1: UM :headphone: ', language='alias')

for i in range(10, 0, -1):
    if  i == 10:
        print(f'{"{}"}'.format(dez.center(38)))
        sleep(1.5)
    elif i == 9:
        print(f'{"{}"}'.format(nove.center(40)))
        sleep(1.5)
    elif i == 8:
        print(f'{"{}"}'.format(oito.center(40)))
        sleep(1.5)
    elif i == 7:
        print(f'{"{}"}'.format(sete.center(40)))
        sleep(1.5)
    elif i == 6:
        print(f'{"{}"}'.format(seis.center(40)))
        sleep(1.5)
    elif i == 5:
        print(f'{"{}"}'.format(cinco.center(40)))
        sleep(1.5)
    elif i == 4:
        print(f'{"{}"}'.format(quatro.center(40)))
        sleep(1.5)
    elif i == 3:
        print(f'{"{}"}'.format(tres.center(40)))
        sleep(1.5)
    elif i == 2:
        print(f'{"{}"}'.format(dois.center(40)))
        sleep(1.5)
    elif i == 1:
        print(f'{"{}"}'.format(um.center(40)))
        sleep(1.5)
print(f'FELIZ ANO NOVO, SEUS PUTOS'.center(40))