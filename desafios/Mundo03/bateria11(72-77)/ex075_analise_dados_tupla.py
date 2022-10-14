print(f'{" Análise de Dados em uma Tupla ":+^50}')

# Criação da tupla;
tupla = (int(input('Valor 1: ')), int(input('Valor 2: ')),
         int(input('Valor 3: ')), int(input('Valor 4: ')))
print(f'A tupla digitada foi: {tupla};')
print('x' * 50)

# Contagem dos números 9 na tupla;
print(f'O número 9 aparece {tupla.count(9)}x;')

# Checar se há número 3 na tupla, se sim, mostrar onde aparece pela primeira vez;
if 3 in tupla:
    print(f'O número 3 aparece primeiro na posição {tupla.index(3)+1};')
else:
    print('Não há o número 3 na tupla criada;')

# Verificar se existem números pares, se sim, exibí-los ta tela;
pares = 0
for numero in tupla:
    if numero % 2 == 0:
        pares += 1
print('Os números pares criados foram: ', end='')
# Se houverem:
if pares > 0:
    for numero in tupla:
        if numero % 2 == 0:
            print(f'{numero};', end=' ')
    print()
# Se não houverem:
else:
    print('nenhum;')
print('x' * 50)
