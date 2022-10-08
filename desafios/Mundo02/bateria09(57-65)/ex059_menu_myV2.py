from time import sleep

print('-==-' * 15)
print('\tPara acessar o menu, entre com as informações:')
num01 = int(input('\tPrimeiro valor: '))
num02 = int(input('\tSegundo valor: '))

loopWhile = 0
while loopWhile != 5:

    if loopWhile == 1:
        print(f'\tSOMA: {num01} + {num02} = {num01 + num02};')
    elif loopWhile == 2:
        print(f'\tPRODUTO: {num01} x {num02} = {num01 * num02};')
    elif loopWhile == 3:
        if num01 > num02:
            print(f'\tMAIOR: {num01};')
        elif num02 > num01:
            print(f'\tMAIOR: {num02};')
        else:
            print('\tSÃO IGUAIS!')
    elif loopWhile == 4:
        num01 = int(input('\tPrimeiro valor: '))
        num02 = int(input('Segundo valor: '))

    print('-==-' * 15)
    print('''
        \t [ 1 ] SOMAR:
        \t [ 2 ] MULTIPLICAR:
        \t [ 3 ] O MAIOR:
        \t [ 4 ] NOVOS VALORES:
        \t [ 5 ] SAIR:
        ''')
    loopWhile = int(input('\tAgora escolha uma opção: '))
    while loopWhile > 5 or loopWhile < 1:
        print('\tOpção inexistente!', end=' ')
        loopWhile = int(input('Agora escolha uma opção VÁLIDA: '))
    sleep(1)

print('\tAdeus!\n')
print('-==-' * 15)
