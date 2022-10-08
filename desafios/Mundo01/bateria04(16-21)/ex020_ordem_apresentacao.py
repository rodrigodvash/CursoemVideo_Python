from random import shuffle

print('Ordem de apresentação')
nome1 = input('Primeiro nome: ')
nome2 = input('Segundo nome: ')
nome3 = input('Terceiro nome: ')
nome4 = input('Quarto nome: ')
sorteio = [nome1, nome2, nome3, nome4]
shuffle(sorteio)
print(f'A ordem de apresentação ficou como: {sorteio}')
