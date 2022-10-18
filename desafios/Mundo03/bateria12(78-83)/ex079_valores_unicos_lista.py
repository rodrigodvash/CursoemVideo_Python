print(f'{" Valores Únicos em uma Lista ":=^50}')

valores = list()
while True:
    # Adicionando valores;
    numero = int(input('\nDigite o valor: '))

    if numero in valores:
        print('Valor já adicionado. ', end='')
    else:
        valores.append(numero)

    # Checar se usuário quer continuar a adicionar valores;
    continuar = str(input('Deseja continuar a adicionar valores? ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar a adicionar valores? ')).strip().upper()[0]
    if continuar == 'S':
        continue
    else:
        break
print('=' * 50)
print(f'Lista criada, em ordem crescente: {sorted(valores)}.')
print('=' * 50)
