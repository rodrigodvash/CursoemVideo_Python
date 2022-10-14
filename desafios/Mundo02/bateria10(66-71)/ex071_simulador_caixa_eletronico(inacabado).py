print('\tSimulador de Caixa Eletrônico')
print('-==-' * 20)

saque = int(input('Quando deseja levantar: '))
unidadeSaque = saque // 1 % 10
dezenaSaque = saque // 10 % 10
centenaSaque = saque // 100 % 10
milharSaque = saque // 1000 % 10

unidade = 0
for index in range(0, unidadeSaque):
    unidade += 1
dezena = 0
for index in range(0, dezenaSaque):
    dezena += 1
centena = 0
for index in range(0, centenaSaque):
    centena += 1
milhar = 0
for index in range(0, milharSaque):
    milhar += 1

nota50 = (milhar * 1000 / 50) + (centena * 100 / 50)

if milhar == 0:
    nota50 = centena * 100 / 50

'''
nota20 = 0
if milhar == 0:
    nota50 = centena * 100 / 50
else:
    nota20 = centena * 100 / 20

nota10 = 0
if centena == 0:
    nota20 = dezena * 10 / 20
else:
    nota10 = dezena * 10 / 10
'''

print('-==-' * 20)
print(f'{int(nota50)} notas de cinquenta' if nota50 != 0 else '', end='')
print(f', {int(nota20)} notas de 20' if nota20 != 0 else f'', end='')
'''print(f', {int(nota10)} notas de 10' if nota10 != 0 else '', end='')
print(';' if unidade == 0 else f' e {int(unidade)} notas de 1;')'''
print('-==-' * 20)