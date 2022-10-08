from time import sleep

print('-==-' * 14, '\n')
print('\tOlá, seja bem-vindo. Informe os valores para as operações!')
valor01 = int(input('\tVALOR 01: '))
valor02 = int(input('\tVALOR 02: '))

print('''
    \t\t[ 1 ] Somar
    \t\t[ 2 ] Multiplicar
    \t\t[ 3 ] O maior dos dois
    \t\t[ 4 ] Entrar com novos números
    \t\t[ 5 ] Sair
    ''')
menu = int(input('\tE agora a sua opção: '))
valores = 1,2,3,4
#print(type(valores))

# Tratando as opções de, ou ser diferente das outras opções, ou de ser a opção de sair(5):
while menu not in valores: # Caso o usuário informe um valor fora da faixa;
    menu = int(input('ERRO! INFORME UMA OPÇÃO VÁLIDA: '))
if menu == 5: # Caso queira sair após informar as opções;
    print('Ok, até mais!')

soma = 0
produto = 0
while menu in valores:
    if menu == 1 or menu == 2 or menu == 3:
        # Opção da SOMA;
        if menu == 1:
            soma = valor01 + valor02
            print(f'\tA soma de {valor01} com {valor02} é de {soma}')

        # Opção da MULTIPLICAÇÃO;
        elif menu == 2:
            produto = valor01 * valor02
            print(f'\tO produto entre {valor01} com {valor02} é de {produto}')

        # Opção do MAIOR entre os dois;
        elif menu == 3:
            if valor01 > valor02: # valor01 MAIOR que valor02;
                print(f'\tO maior entre os dois valores é o {valor01}')
            elif valor02 > valor01: # valor02 MAIOR que valor01;
                print(f'\tO maior entre os dois valores é o {valor02}')
            else: # Os valores são iguais;
                print(f'\t{valor01} = {valor02}')

    # Opção para nova entrada de valores;
    elif menu == 4:
        valor01 = int(input('\tVALOR 01: '))
        valor02 = int(input('\tVALOR 02: '))

    print('-==-' * 14)
    sleep(1)
    print('''
                \t\t[ 1 ] Somar
                \t\t[ 2 ] Multiplicar
                \t\t[ 3 ] O maior dos dois
                \t\t[ 4 ] Entrar com novos números
                \t\t[ 5 ] Sair
                ''')
    menu = int(input('\tDeseja entrar com outra opção? '))
    # Opção para revalidar as opções do programa;
    while menu > 5 or menu < 1: # Quando a opção for 5, o programa termina;
        menu = int(input('\tERRO! INFORME UMA OPÇÃO VÁLIDA: '))

print('-==-' * 14)
print('\tOk, até mais!')
print('-==-' * 14, '\n')
