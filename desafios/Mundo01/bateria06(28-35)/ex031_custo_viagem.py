print('Custo da viagem')
distancia = float(input('Qual a distância a percorrer: '))
if distancia <= 200:
    print(f'O valor a pagar é de {distancia * 0.5}€!')
else:
    print(f'O valor a pagar é de {distancia * 0.45}€!')
