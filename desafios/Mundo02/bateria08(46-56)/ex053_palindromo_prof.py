frase = str(input('Digite sua frase: ')).strip().upper()

palavras = frase.split() # Separou a frase em uma lsiata de palavras;
juntas = ''.join(palavras) # Junta as palavras com o ''(sem espaçamento);
# Tem 3 variáveis, 1 com o input, outra com a separação das palavras e uma terceira com a junção das palavras sem espaços;

# inverso = juntas[::-1] # Isto substitui o loop For!
inverso = '' # Variável que vai receber a frase invertida, iniciada vazia;

for letra in range(len(juntas)-1, -1, -1):
# Inicia com a quantidade de caracteres da variável ('juntas', -1),vai até o elemento 0 (0 = -1), indo do último ao primeiro (de -1 em -1);
    inverso += juntas[letra]
    # Pega a última letra de 'juntas' e coloca na primeira posição de 'inverso', e segue assim até o último elemento de 'juntas';

print(f'\nO inverso de {juntas} é {inverso}.\n')

if inverso == juntas:
    print('A frase é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')