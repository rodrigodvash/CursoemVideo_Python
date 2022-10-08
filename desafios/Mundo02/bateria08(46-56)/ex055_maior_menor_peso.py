print('Maior e menor peso da sequência\n')

maior = 0
menor = 0
for i in range(0, 5):
    print(f'Digite o peso do {i + 1}º', end=' ')
    peso = float(input())
    if i == 0:  # o primeiro peso será o maior e menor no primeiro laço, depois ele ira analisar os proximos pesos.
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'{maior}')
print(f'{menor}')
