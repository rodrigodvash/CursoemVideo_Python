frase = '   Curso em Vídeo Python   '
print(frase[3]) #Slice na quarta letra;
print(frase[9:14]) # Slice somente na palavra 'Vídeo';
print(frase[:10]) # Slice do início até a nona (a décima não é contada);
print(frase[10:]) # Slice iniciando na décima posição e indo até o final;
print(frase[3:18:3]) # Slice da terceira até a décima-quinta, de três-em-três;
print(frase[5::2]) # Slice da quinta posição até a última, de dois-em-dois;
print(frase[::4]) # Slice do início ao fim, de quatro-em-quatro;
print()
print(f'Qual o tamanho da frase? {len(frase)}')
print(f'E agora, qual o tamanho da frase (sem os espaços)? {len(frase.strip())}')
print(f'Quantos \'és\' há na frase? {frase.count("e")}')
print(f'Quantos \'Ós\' há na frase? {frase.count("O")}')
print(f'Agora, quantos \'Ós\' há na frase, hein? {frase.upper().count("O")}')
print(f'Substituir Python por Android: {frase.replace("Python", "Android")}')
print(f'Tamanho novo: {len(frase)}')
print(frase) # Strings são imutáveis, ==> frase[0] = 'J' <== resulta em um erro!
# Por isso que, mesmo após aplicar o 'strip', se imprimir a variável frase, ela mostra com os espaços;
frase = frase.replace('Python', 'Android').strip()
print(f'Agora sim, ele mostra com o \'strip\' e com o \'replace\': {frase}, tamanho: {len(frase)}')
print(f'A palavra Curso existe na frase? {"Curso" in frase}')
print(f'Onde inicia a palavra Curso na frase? {frase.find("Curso")} index.')
print(f"Onde inicia a palavra vídeo (minúsculo) na frase? {frase.lower().find('vídeo')}, haha, o .lower()")
