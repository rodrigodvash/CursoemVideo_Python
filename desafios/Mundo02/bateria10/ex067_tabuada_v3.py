print(f'Tabuada V3.0'.center(70))
print('-==-' * 20)

while True:
    numero = int(input('\n\t\t\tDeseja ver a tabuada de qual valor? '))
    if numero < 1: # Se o valor for 0 ou menor, o loop é interrompido;
        break
    for index in range(1, 11): # Loop for com intervalo de 1 a 10;
        print(f'\t\t\t{numero} x {index:2} = {numero * index}') # numero x index = produto;
    print('-==-' * 20)

print('\t\t\tAdeus!')
