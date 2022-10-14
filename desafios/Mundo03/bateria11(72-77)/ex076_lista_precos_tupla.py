print(f'{" Lista de Preços com Tuplas ":/^50}')
print()
print('\\' * 50)
materiais = (
    'Lápis', 1.75,
    'Borracha', 2,
    'Caderno', 15.90,
    'Estojo', 25,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90,
)

for item in range(0, len(materiais)):
    if item % 2 == 0:
        print(f'\t{materiais[item]:.<33}', end=' ')
    else:
        print(f'€ {materiais[item]:>6.2f}')
print('\\' * 50)
