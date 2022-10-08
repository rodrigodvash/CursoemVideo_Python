for i in range(1, 6):
    print(f'Informe o peso da {i}º pessoa:', end=' ')
    peso = float(input())

    if i == 1:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso
print(f'MAIOR = {maior:.1f}')
print(f'MENOR = {menor:.1f}')