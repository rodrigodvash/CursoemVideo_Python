print('-==-' * 30)
print((' ' * 50), 'My Fibonacci Sequence')
print('-==-' * 30)
termo = int(input('\t\t\tQuantos termos deseja ver da sequência? '))

primeiro = 0
segundo = 1
index = 0 # Indexpro loop-While;
print(f'\t{primeiro}, {segundo}, ', end='')

while index <= termo: # Enquanto o index for menor ou igual à quantidade de termos:
    terceiro = primeiro + segundo
    print(f'{terceiro}, ', end='')

    primeiro = segundo
    segundo = terceiro
    index += 1
print('FIM!')
print('-==-' * 30)
