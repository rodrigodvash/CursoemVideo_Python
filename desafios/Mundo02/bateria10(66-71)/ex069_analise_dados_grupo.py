print('Ánalise de Dados de um Grupo')
print('-==-' * 20)

maiorIdade = 0 # Contar idades +18;
homem = 0      # Contar homens;
mulher = 0     # Contar mulheres < 20;
while True:
    idade = int(input('\tQual a idade: '))
    sexo = str(input('\tQual o sexo: ')).strip().upper()[0]
    while sexo not in 'FM': # Checar se o sexo foi escrito corretamente;
        sexo = str(input('\tPor favor, qual o sexo: ')).strip().upper()[0]

    if idade >= 18: # Conta quantas pessoas possuem mais de 18 anos;
        maiorIdade += 1

    if sexo in 'Mm': # Conta quantos homens foram cadastrados;
        homem += 1

    if sexo in 'Ff': # Conta quantas mulheres cadastradas tem menos de 20 anos;
        if idade < 20:
            mulher += 1

    cadastro = str(input('\n\tQuer continuar a cadastrar? ')).strip().upper()[0]
    while cadastro not in 'SYN':
        cadastro = str(input('\n\tNão entendi sua resposta, quer continuar a cadastrar? ')).strip().upper()[0]
    if cadastro in 'SY': # Se 'cadastro' for Sim ou Yes;
        continue
    elif cadastro in 'N':
        print('\tOk, até mais!\n')
        break

print(f'\tNeste cadastro existem: {maiorIdade} pessoa(s) com mais de 18 anos.')
print(f'\tForam cadastrados: {homem} pessoa(s) do sexo masculino.')
print(f'\tForam cadastradas: {mulher} mulher(es) com menos de 20 anos.')
print('-==-' * 20)
