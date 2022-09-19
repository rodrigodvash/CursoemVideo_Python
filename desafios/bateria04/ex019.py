from random import randint, choice

print('Nomes aleatórios')
nome1 = input('Primeiro nome: ')
nome2 = input('Segundo nome: ')
nome3 = input('Terceiro nome: ')
nome4 = input('Quarto nome: ')
nomes = choice([nome1, nome2, nome3, nome4])
print(nomes)
