print('Soma dos pares\n')

soma = 0
cont = 0
for i in range(1, 7):
    numero = int(input(f'Digite o {i}º número: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print(f'A soma dos {cont} números pares que você digitou deu {soma}.')