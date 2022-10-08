print('Somar ímpares e múltiplos de três\n')

print('Somando os números ímpares que são múltiplos de três:')
soma = 0
cont = 0
for i in range(3, 500, 3): # Aqui, com o passo de 3, eliminei um 'if' e 2/3 das iterações!
    if i % 2 != 0:
        # print(f'Valor de i: {i}')
        soma += i
        cont += 1
print(f'A soma de todos os {cont} números ímpares até 500 que são múltiplos de três é igual a {soma}')
