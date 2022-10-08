print('Separando dígitos')
digito = int(input('Digite um número (entre 0 até 9999): '))

unidade = digito // 1 % 10
print(f'UNIDADES: {unidade}')
dezena = digito // 10 % 10
print(f'DEZENAS: {dezena}')
centena = digito // 100 % 10
print(f'CENTENAS: {centena}')
milhar = digito // 1000 % 10
print(f'MILHARES: {milhar}')

