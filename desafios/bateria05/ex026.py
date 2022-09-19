print('Primeira e última ocorrência de uma String')
frase = str(input('Digite uma frase: ')).lower().strip()
print(f'Quantas vezes aparece a letra \'A\'? {frase.count("a")}')
print(f'Em qual posição ela aparece pela primeira vez? {frase.find("a") + 1}')
print(f'Em qual posição ela aparece pela última vez? {frase.rfind("a") + 1}')
# Naturalmente, o find inicia pela esquerda, então rfind o inicia pela direita;
