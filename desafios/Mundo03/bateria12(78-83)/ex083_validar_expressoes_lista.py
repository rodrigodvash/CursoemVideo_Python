print(f'{"= Validando Expressões Matemáticas =":-^50}')

while True:
    # Strings são listas de caracteres!
    expressao = str(input('Digite a expressão: ')).strip()

    # Variáveis para contar os caracteres '(' e ')';
    contAberto = 0
    contFechado = 0
    for caracteres in expressao:
        if caracteres == '(':
            contAberto += 1
        elif caracteres == ')':
            contFechado += 1
    # Se as quantidades estiverem iguais, então a expressão está correta;
    if contAberto == contFechado:
        print('Sua expressão está correta, parabéns!')
    else:
        if contAberto > contFechado:
            print('Sua expressão está errada! Falta fechar algum(ns) parênteses.')
        elif contFechado > contAberto:
            print('Sua expressão está errada! Há ")" a mais na sua expressão.')

    # Verificar se utilizador quer continuar a verificar as suas expressões;
    loopWhile = str(input('Quer continuar a verificar expressões [S/N]? ')).strip().upper()[0]
    while loopWhile not in 'SN':
        loopWhile = str(input('Quer continuar a verificar expressões [S/N]? ')).strip().upper()[0]
    if loopWhile == 'S':
        print('-' * 50)
    else:
        break
print('Adeus!')
