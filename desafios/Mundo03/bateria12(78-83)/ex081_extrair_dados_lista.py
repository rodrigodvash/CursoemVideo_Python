print(f'{" Extraindo Dados de uma Lista ":#^70}')

# Entrando com valores e os adicionando numa lista;
lista = list()
while True:
    lista.append(int(input('Informe um valor: ')))

    # Verificar se usuário quer cntinuar a inserir valores na lista;
    loopWhile = str(input('Quer continuar a inserir valores [S/N]? ')).strip().upper()[0]
    while loopWhile not in 'SN':
        loopWhile = str(input('Desculpe-me, mas você quer continuar a '
                              'inserir valores [S/N]? ')).strip().upper()[0]
    if loopWhile == 'S':
        print('#' * 70)
        continue
    else:
        break

print('#' * 70)
print(f'Lista = {lista}, com {len(lista)} valores digitados.')
print(f'A mesma lista, mas em ordem decrescente: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O número 5 consta na lista, no(s) índice(s): ', end='')
    for index, valor in enumerate(lista):
        if valor == 5:
            print(f'Índice [{index}];', end=' ')
    print()
else:
    print('O número 5 não consta na lista!')
