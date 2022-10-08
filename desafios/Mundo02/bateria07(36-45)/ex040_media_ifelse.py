print('Media com estrutura de controle IF')

color = {
    'clear': '\033[m',
    'green': '\033[7;42m',
    'yellow': '\033[7;43m',
    'red': '\033[7;41m'
}

nota01 = float(input('Qual a primeira nota: '))
nota02 = float(input('Qual a segunda nota: '))
# Média do aluno;
media = (nota01 + nota02) / 2

if media < 5:
    print(f'Nota: {media:.1f} - {color["red"]}REPROVADO{color["clear"]}')
elif media < 7 and media >= 5:
    print(f'Nota = {media:.1f} - {color["yellow"]}RECUPERAÇÃO{color["clear"]}')
else:
    print(f'Nota: {media:.1f} - {color["green"]}APROVADO{color["clear"]}')
