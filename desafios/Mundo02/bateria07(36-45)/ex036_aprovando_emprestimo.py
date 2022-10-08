print('Aprovando empréstimo\n')

# Cores pro terminal;
color = {
    'clear': '\033[m',
    'red': '\033[1;31m',
    'green': '\033[7;32m',
    'yellow': '\033[7;33m',
    'blue': '\033[34m'
}

# Dados do requerinte do empréstimo;
print('Olá, vamos tentar realizar o sonho da casa própria?')
emprestimo = float(input('Qual o valor almejado? € '))
salarioComprador = float(input('E o salário do requerinte? € '))
anos = int(input('E em quantos anos o requerinte pretende pagar? '))

meses = anos * 12
# Valor mensal das parcelas;
mensalidade = emprestimo / meses

      # 30% do salário;
if (salarioComprador * 0.3) < mensalidade:
    print(f'Sinto muito, o valor das parcelas comprometem mais de {color["red"]}30% do seu salário{color["clear"]}!')
    print(f'Tente solicitar um {color["blue"]}valor menor{color["clear"]} para o empréstimo, '
          f'ou {color["blue"]}mais parcelas{color["clear"]}.')

elif emprestimo > 1000000: # Caso o doido peça um empréstimo que ele não pretende pagar...
    print('Solicite um valor mais baixo!!')
else:
    print(f'{color["yellow"]}Parabéns, valor aprovado!{color["clear"]}')
    print(f'Suas mensalidades terão um valor de {color["green"]}€ {mensalidade:.2f}{color["clear"]}.')
