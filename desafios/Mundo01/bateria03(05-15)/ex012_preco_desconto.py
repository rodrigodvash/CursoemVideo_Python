print('preço e desconto')
preco = float(input('Qual o preço do produto: €'))
novoPreco = preco - (preco * 0.05) # 0.5 = 0.50, o que resultaria em 50% de desconto!
print(f'O preço deste produto com 5% de desconto é de {novoPreco:.2f}€')
