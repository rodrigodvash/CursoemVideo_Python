nome = str(input('Qual é o seu nome? ')).strip()
if nome == "Rodrigo":
    print('Estou torcendo por você!')
elif nome == 'Maria' or nome == 'Ana' or nome == 'Gabi':
    print('Olá moça!')
elif nome in 'Pedro João José':
    print('Olá cara!')
else:
    print('Olá estranho(a)!')
print(f'Tenha um bom dia, {nome}!')
