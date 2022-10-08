print('Analisador de textos')
nome = str(input('Digite seu nome completo: ')).strip()
print(f'NOME MAIUSCULO: {nome.upper()}')
print(f'nome minúsculo: {nome.lower()}')
print(f'Total de caracteres do nome: {len(nome)} letras')
print(f'Total de caracteres do seu nome sem espaços: {len(nome.replace(" ", ""))} letras') # Com replace;
print(f'Total de caracteres do seu nome sem espaços: {len(nome) - nome.count(" ")} letras') # Com count;
primeiro = nome.split()
print(f'Total de caracteres do primeiro nome {primeiro[0]}: {len(primeiro[0])} letras') # Com split;
print(f'Total de caracteres do primeiro nome: {nome.find(" ")} letras')
# Ele mostra a posição do primeiro espaço, assim dizendo o total de letras antes dele;
