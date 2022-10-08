nome = 'Rodrigo Henique Maia Oliveira'
print(f'NOME COM SPLIT = {nome.split()}')
dividido = nome.split()
print(f'VARIÁVEL RECEBENDO O SPLIT, E IMPRIMINDO OS 2 PRIMEIROS: {dividido[0:2]}')
print(f'NOME COM MAXSPLIT = {nome.split(None, 2)}')
print()
nome1, nome2, nome3, nome4 = nome.split()
print(f'NOMES SEPARADOS EM VARIÁVEIS = {nome1} - {nome2} - {nome3} - {nome4}')
numeros = '1;2;3;4;5;6;7;8;9;0'
print(f"NUMEROS COM SPLIT SEPARAÇÃO DEFINIDO = {numeros.split(';', 5)}")

texto = 'Aaa', 'Bbb', 'Ccc', 'Ddd', 'Eee'
print(f"{' - '.join(texto)}")
