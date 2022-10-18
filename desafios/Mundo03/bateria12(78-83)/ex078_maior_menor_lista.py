print(f'{" Maior e Menor Valor ":#^50}')
valores = list()
# Adicionar cinco valores:
for valor in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {valor+1}: ')))
print(f'Lista criada: {valores}.')
print('#' * 50)

# Pegar o maior valor da lista;
maior = max(valores)
print(f'O maior valor da lista é o {maior}, que está no:')
# E encontrar o seu(s) índex:
for i, v in enumerate(valores):
    if valores[i] == maior:
        print(f'\tindex: {i}', end='; ')

# Pegar o menor valor da lista;
menor = min(valores)
print(f'\nO menor valor da lista é o {menor}, que está no:')
for i, v in enumerate(valores):
    if valores[i] == menor:
        print(f'\tindex: {i}', end='; ')
print()
print('#' * 50)
