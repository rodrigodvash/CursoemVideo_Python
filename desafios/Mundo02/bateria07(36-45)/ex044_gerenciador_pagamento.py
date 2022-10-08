print('Gerenciador de pagamentos\n')

color = {
    'clear': '\033[m',
    'green': '\033[32m',
    'cyan': '\033[36m',
    'blue': '\033[34m',
    'yellow': '\033[33m'
}

print('{:=^40}'.format(' LOJAS RODRIGUEIRA '))
valor = float(input('Qual o valor da compra: '))
print('E em quantas vezes será o pagamento?', end=" ")
parcelas = int(input('À vista: (0 para à dinheiro/cheque e 1 para cartão): '))

if parcelas == 0:
    pagamento = valor - (valor * 0.1)
    print(f'No pagamento à vista no dinheiro/cheque você tem 10% de desconto, '
          f'{color["green"]}no valor de € {pagamento:.2f}{color["clear"]}.')
elif parcelas == 1:
    pagamento = valor - (valor * 0.05)
    print(f'No pagamento à vista no cartão voçê tem 5% de desconto, '
          f'{color["cyan"]}no valor de € {pagamento:.2f}{color["clear"]}.')
elif parcelas == 2:
    print(f'No pagamento em até 2x no cartão {color["blue"]}não serão cobrados juros!{color["clear"]}')
else:
    pagamento = valor + (valor * 0.2)
    print(f'Com essas parcelas, você terá de pagar 20% de juros, '
          f'{color["yellow"]}no valor de € {pagamento:.2f}{color["clear"]}, '
          f'divididos em {color["yellow"]}{pagamento / parcelas} por mês{color["clear"]}.')
