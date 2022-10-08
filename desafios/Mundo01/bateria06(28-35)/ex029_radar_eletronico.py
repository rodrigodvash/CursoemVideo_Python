print('Radar eletrônico')
velocidade = float(input('Qual a velocidade registrada: '))
multa = 0
if velocidade <= 80:
    print('Tudo nos conformes, siga em paz!')
else:
    multa = (velocidade - 80) * 7
    print(f'Acima do limite!\nA multa a pagar é de € {multa:.2f}')
print('Dirija com segurança!')
