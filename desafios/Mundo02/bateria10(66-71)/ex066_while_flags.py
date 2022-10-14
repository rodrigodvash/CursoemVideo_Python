print(f'Vários Números com Flag'.center(70))
print('-==-' * 20)

soma = cont = 0
while True:
    numero = int(input('\t\t\tNÚMERO (999 para parar): '))
    if numero == 999:
        break
    soma += numero
    cont += 1
print('-==-' * 20)
print(f'\t\t\tSOMA = {soma};\n\t\t\tQUANTIDADES = {cont};')
