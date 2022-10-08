print('-=-' * 20)
print('Tratando Valores')
numero = int(input('Entre com um valor [escolha 999 para sair]: '))
soma = 0
cont = 0
while numero != 999: # Condição de parada do While: 999;
    soma += numero
    cont += 1
    print(f'\tSOMA ATUAL: {soma}\n\tCONTAGEM ATUAL: {cont}')
    numero = int(input('Entre com outro valor [escolha 999 para sair]: '))
print('-==-' * 20)
print(f'\tSOMA DOS VALORES ESCOLHIDOS = {soma}')
print(f'\tQUANTIDADE DE VALORES: {cont}')
print('-==-' * 20)