print('Procurar uma String dentro de outra')
nome = str(input('Informe seu nome: ')).strip()
print(f'O nome possui o nome \'Silva\'? {"silva" in nome.lower().split()}')
# O 'in' verifica se existe dentro da String a ocorrência;
# O split não permite a ocorrência de True em Silvano, por exemplo;
