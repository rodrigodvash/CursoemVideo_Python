print('Analisador completo\n')

print('Criando o perfil das 4 pessoas:')

soma = 0
idade_velho = 0
nome_velho = ''
cont = 0
for pessoa in range(1, 5):
    print(f'Nome, Idade e Sexo da {pessoa}º pessoa:')
    nome = str(input('Nome = ')).strip()
    idade = int(input('Idade = '))
    sexo = str(input('Sexo [M/F] = ')).strip().upper()
    print("=========================")

    soma += idade # Determinar a soma das idades de todas as pessoas;

    if pessoa == 1 and sexo == 'M':
        idade_velho = idade
        nome_velho = nome
    if sexo == 'M' and idade > idade_velho:
        idade_velho = idade
        nome_velho = nome

    if sexo in 'Ff' and idade < 20:# Conta as mulheres com menos de 20 anos;
        cont += 1

print(f'A média das idades do grupo é de {soma / 4:.1f}')
print(f'O homem mais velho é o {nome_velho} com {idade_velho}')
print(f'Total de mulheres com menos de 20 anos = {cont}')

