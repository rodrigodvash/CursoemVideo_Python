print('\tEstatística de Produtos')
print('-==-' * 20)

total = 0           # Total da compra;
precoAlto = 0       # Preço dos valores acima de 1000;
nomePrecoAlto = []  # Lista para os nomes dos produtos com preços acima de 1000;
precoBaixo = 0      # Preço do valor mais baixo;
nomePrecoBaixo = '' # Nome do produto com preço mais baixo;
while True:
    produto = str(input('\tQual o nome do produto: ')).strip()
    preco = float(input('\tQual o preço do produto: '))
    print()

    total += preco # Total gasto na compra;

    if preco > 1000:
        nomePrecoAlto.append(produto) # Lista com nomes dos produtos com preço maior do que 1000;
        precoAlto += 1                # Conta quantos produtos tem o valor maior do que 1000;

    if precoBaixo == 0 or preco < precoBaixo: # Grava o produto com preço mais baixo, ou;
        precoBaixo = preco            # Atualiza: quando o preço atual for menor que o preço mais baixo;
        nomePrecoBaixo = produto

    # Loop para saber se o utilizador quer ou não continuar os cadastros;
    continuar = str(input('\tDeseja continuar o cadastro? ')).strip().upper()[0]
    while continuar not in 'SYN': # Loop para quando o valor digitado não for (Sim, Yes, Não/No);
        continuar = str(input('\tVocê deseja continuar o cadastro? ')).strip().upper()[0]
    if continuar in 'SY':
        continue
    elif continuar == 'N':
        print('\tSeus dados são:')
        break

print('-==-' * 20)
print(f'\tO total gasto na compra foi de € {total:.2f};')
print(f'\tUm total de {precoAlto} produtos custam mais de € 1000,00, sendo eles:')
print(f'\t\t{nomePrecoAlto}')
print(f'\tO {nomePrecoBaixo} é o produto mais barato do cadastro;')
print('-==-' * 20)
print('{:-^40}'.format(' FIM DO PROGRAMA '))
