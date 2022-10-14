print('{:-^60}'.format(' SIMULADOR DE CAIXA ELETRÔNICO '))
saque = int(input('\tQuanto deseja sacar? '))
total = saque
cedulas = 100
totalCedulas = 0
while True:
    if total >= cedulas:
        total -= cedulas
        totalCedulas += 1
    else:
        if totalCedulas > 0:
            print(f'\tUm total de: {totalCedulas} cédulas de {cedulas} euros.')

        if cedulas == 100:
            cedulas = 50
        elif cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 5
        elif cedulas == 5:
            cedulas = 1
        totalCedulas = 0

        if total == 0:
            break
print('{:-^60}'.format(' FIM '))