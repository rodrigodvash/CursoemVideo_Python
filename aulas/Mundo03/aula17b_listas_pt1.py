valores = list()
'''valores.append(5)
valores.append(3)
valores.append(9)'''
for ler in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print()

# Para mostrar/trabalhar elemento por elemento;
for index, valor in enumerate(valores):
    print(f'Na posicão {index} consta o elemento {valor}.')
