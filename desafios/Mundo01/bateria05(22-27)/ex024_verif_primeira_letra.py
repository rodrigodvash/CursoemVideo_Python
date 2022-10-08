print('Verificando primeiras letras')
cidade = str(input('Em qual cidade você nasceu? ')).strip() # Eliminando espaços das bordas;
cidade = cidade.lower() # Deixando tudo em minúsculo;
print(f'{cidade.startswith("santo ")}')
