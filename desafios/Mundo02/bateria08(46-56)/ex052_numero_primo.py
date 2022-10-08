print('Número primo\n')

numero = int(input('Informe o número para análise: '))
temp = 0
for i in range(1, numero+1):
    if numero % i == 0: # Aqui o resto da divisão tem que ser sempre 0,
                        # sendo assim dividindo por 1 e por ele mesmo sempre entra na conta;
        print('\033[32m', end=' ') # Quando for divisível, fica VERDE;
        temp += 1 # Aqui contará quantas vezes ocorre a divisão com resto 0;
    else:
        print('\033[31m', end=' ') # Quando não for divisível, fica VERMELHO;
    print(f'{i}', end=' ')

if temp == 2 and numero > 0:
# Aqui só é verdade quando a quantidade de divisões por 0 for igual ou menos que 2x e maior que 0;
    print(f'\n\033[mO número {numero} é primo.')
else:
    print(f'\n\033[mO número {numero} foi divisível {temp} vezes, portanto não é primo.')
