print('Primeiro e último nome')
nome = str(input('Digite seu nome completo: ')).strip()
separar = nome.split()
print(f'Seu primeiro nome é {separar[0]}')
print(f'Seu último nome é {separar[len(separar)-1]}')