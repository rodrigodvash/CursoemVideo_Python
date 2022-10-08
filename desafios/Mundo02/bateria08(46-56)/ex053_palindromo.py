print('Detector de palíndromo\n')
from re import sub # Biblioteca para tratamento de pontuações em strings;
from unicodedata import normalize # Biblioteca para tratar as acentuações;

frase = str(input('Digite a frase para o teste: ')) # Mantenho a frase intacta;
fraseFormatada = frase.strip().lower().replace(' ', '')
# Removendo todos os espaços, deixando tudo minúsculo e trocando os espaços internos para nada;

reFrase = sub(r'[^\w\s]', '', fraseFormatada) # Remover as pontuações da frase;
reFrase2 = normalize('NFKD', reFrase).encode('ASCII','ignore').decode('ASCII') # Remover as acentuações da frase;

j = len(reFrase2) - (len(reFrase2) + 1) # Variável índex, para fazer a busca de trás pra frente da frase;
temp = 0 # Variável que vai contar as vezes que a comparação das letras forem iguais;

for i in range(0, len(reFrase2)):
    if reFrase2[i] == reFrase2[j]: # A primeira e a última letra são iguais? Se sim:
        temp += 1 # Quando as letras forem iguais, esta variável se incrementa;
    j -= 1 # O 'i' sempre incrementa, aqui eu 'incremento' o j para continuar a comparar;

print(f'Sua frase invertida = {reFrase2[::-1].upper()}') # Printa a frase na tela de trás para frente;

if temp == len(reFrase2): # Quando temp for igual ao tamanho da frase (Todas as letras foram comparadas e são iguais):
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')