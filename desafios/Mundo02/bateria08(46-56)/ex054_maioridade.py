print('Grupo da maioridade\n')
from datetime import date

ano_atual = date.today().year # Ano atual da máquina;
print('Diga quando você e mais seis amigos teus nasceram:')

menor = 0
maior = 0
for i in range(1, 8):
    print(f'Diga o ano de nasc. do {i}º: ', end='')
    ano = int(input()) # Entrada doano de nascimento;
    idade = ano_atual - ano # Idade da pessoa;

    if idade < 18: # 18 anos é a maioridade;
        menor += 1 # Conta quantos são menores de acordo com a idade;
    else:
        maior += 1 # Conta quantos são maiores de acordo com a idade;

print(f'Entre vocês, {menor} é menor de idade e {maior} é maior de idade.')