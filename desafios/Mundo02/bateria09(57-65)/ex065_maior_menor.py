print('-==-' * 20)
print('Maior e Menor valores (quantidade e média)\n')
print('-==-' * 20)

soma = media = cont = maior = menor = 0
continuar = 's'
while continuar == 's':
    numero = int(input('\tDigite um valor: '))

    if continuar == 's':
        soma += numero # Somatória dos números digitados;
        cont += 1      # Quantidade de números digitados;

    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        else:
            menor = numero

    continuar = str(input('Deseja continuar a adicionar números? ')).strip().lower()[0]

media = soma / cont # Média dos números digitados;
print('-==-' * 20)
print(f'\t\tVocê digitou {cont} números, com média de {media:.1f};')
print(f'\t\tO {maior} é o maior e o {menor} é o menor entre eles;')
print('-==-' * 20)