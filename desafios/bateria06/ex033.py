print('Maior e menor')
numero1 = int(input('NÚMERO 01: '))
numero2 = int(input('NÚMERO 02: '))
numero3 = int(input('NÚMERO 03: '))
if numero1 > numero2 and numero1 > numero3:
    if numero2 > numero3:
        print(f'O número {numero1} foi o maior e o {numero3} o menor.')
    else:
        print(f'O número {numero1} foi o maior e o {numero2} o menor.')

elif numero2 > numero3:
    if numero1 > numero3:
        print(f'O número {numero2} foi o maior e o {numero3} o menor.')
    else:
        print(f'O número {numero2} foi o maior e o {numero1} o menor.')

elif numero1 == numero2 and numero1 == numero3:
    print('São todos iguais')

else:
    if numero1 > numero2:
        print(f'O número {numero3} foi o maior e o {numero2} o menor.')
    else:
        print(f'O número {numero3} foi o maior e o {numero1} o menor.')

