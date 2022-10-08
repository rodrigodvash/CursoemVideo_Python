cores = {
    'negative'  : '\033[7;30m',
    'sublinhado': '\033[4;36;45m',
    'clear': '\033[m'
}

var = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {cores["negative"]}{type(var)}{cores["clear"]}')
print(f'É AlphaNumérico? {cores["sublinhado"]}{var.isalnum()}{cores["clear"]}')
print(f'É Alfabético? {cores["negative"]}{var.isalpha()}{cores["clear"]}')
print(f'Está no Código Padrão Americano? {cores["sublinhado"]}{var.isascii()}{cores["clear"]}')
print(f'É Numérico? {cores["negative"]}{var.isnumeric()}{cores["clear"]}')
print(f'É um Dígito? {cores["sublinhado"]}{var.isdigit()}{cores["clear"]}')
print(f'É um número Real? {cores["negative"]}{var.isdecimal()}{cores["clear"]}')
print(f'Está todo em Maiúsculo? {cores["sublinhado"]}{var.isupper()}{cores["clear"]}')
print(f'Está tdo em Minúsculo? {cores["negative"]}{var.islower()}{cores["clear"]}')
print(f'É "Printável" na tela? {cores["sublinhado"]}{var.isprintable()}{cores["clear"]}')
print(f'Contém somente Letras, Números e "Underline"? {cores["negative"]}{var.isidentifier()}{cores["clear"]}')
print(f'É Vazia? {cores["sublinhado"]}{var.isspace()}{cores["clear"]}')
print(f'Está capitalizada? {cores["negative"]}{var.istitle()}{cores["clear"]}')

