print(f'{" Dividindo Valores em Várias Listas ":/^50}')

# Ler vários números e armazená-los numa lista;
listaNumeros = list()
while True:
    listaNumeros.append(int(input('Digite o valor desejado: ')))

    # Verificar se usuário quer continuar a inserir valores;
    loopWhile = str(input('Deseja continuar a inserir valores [S/N]? ')).strip().upper()[0]
    while loopWhile not in 'SN':
        loopWhile = str(input('Por favor, informe uma opção válida!'
                              '\nDeseja continuar a inserir valores [S/N]? ')).strip().upper()[0]
    if loopWhile in 'S':
        print('/' * 50)
    else:
        break

# Criação das listas de valores pares e ímpares;
listaPares   = list()
listaImpares = list()
for valor in listaNumeros:
    if valor % 2 == 0:
        listaPares.append(valor)
    else:
        listaImpares.append(valor)

print('/' * 50)
print(f'{"Lista Completa ":=<19} {listaNumeros};')
print(f'{"Lista dos Pares ":=<19} {listaPares};')
print(f'{"Lista dos Impares ":=<19} {listaImpares};')
