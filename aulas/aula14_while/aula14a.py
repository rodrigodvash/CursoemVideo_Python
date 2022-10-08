'''
for i in range(1, 10):
    print(c)
print('FIM')
'''

i = 1
while i < 10:
    print(i)
    i += 1
print('FIM')

j = 1
while j != 0:
    j = int(input('NÚMERO: '))
print('FIM')

resposta = 'S'
while resposta == 'S':
    numero = int(input('Digite: '))
    resposta = str(input('Quer continuar? ')).upper()
print('FIM')

x = 1
par = 0
impar = 0
while x != 0:
    x = int(input('Digite um número: '))
    if x != 0:
        if x % 2 == 0:
            par += 1
        elif x % 2 != 0:
            impar += 1
print(f'PARES = {par}\nIMPARES = {impar}\nACABOU!')