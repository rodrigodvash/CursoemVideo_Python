print('-==-' * 15)
print('SEQUÊNCIA DE FIBONACCI')
print('-==-' * 15)
numero = int(input('De onde se inicia a sequência? '))
quant = int(input('Quantos elementos mostrar na sequência? '))

primeiro = 0                  # Primeiro elemento da sequênia;
segundo = 1                   # Segundo elemento da sequênia;
index = 3                     # Variável do loop (Os dois primeiros elementos já foram criados);

print(f'{primeiro}, {segundo}, ', end='')
while index <= quant:
    terceiro = primeiro + segundo  # Terceiro elemento da sequênia;
    print(f'{terceiro}, ', end='')

    primeiro = segundo  # O primeiro elemento passa a ser o segundo;
    segundo = terceiro  # O segundo passa a ser o terceiro;
    index += 1

# Primeiro definimos o valor dos 2 primeiros;
# Cria-se o loop para o terceiro (as somatórias);
# E depois o terceiro a ser a soma dos 2 anteriores;
# Com o terceiro pronto, redefinimos o primeiro para ser o segundo, e o segundo para ser o terceiro;
# O loop se repete pelo valor de 'quant';
print(f'FIM')
