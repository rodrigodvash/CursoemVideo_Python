print('Aumentos múltiplos')
salario = float(input('SALÁRIO: '))
if salario <= 1250:
    salario = salario + (salario * 0.15)
    print(f'NOVO SALÁRIO: {salario:.2f}€')
else:
    salario = salario + (salario * 0.1)
    print(f'NOVO SALÁRIO: {salario:.2f}€')
