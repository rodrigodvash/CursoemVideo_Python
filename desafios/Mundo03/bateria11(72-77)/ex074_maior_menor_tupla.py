print(f'{" Maior e Menor valor em uma Tupla ":-^50}')
from random import randint

# Eu nunca penso na solução mais óbvia...
tupla = (randint(0, 10), randint(0, 10), randint(0, 10),
         randint(0, 10), randint(0, 10))

# Descobrir o maior valor criado;
maior = sorted(tupla, reverse=True)
# Descobrir o menor valor criado
menor = sorted(tupla)
print('-=-' * 17)
print(f'A tupla criada aleatoriamente foi: {tupla};')

print(f'O maior valor desta tupla é o {maior[0]};')
print(f'O maior valor sorteado foi o {max(tupla)}')######
print(f'O menor valor desta tupla é o {menor[0]};')
print(f'O menor valor sorteado foi o {min(tupla)}')######
