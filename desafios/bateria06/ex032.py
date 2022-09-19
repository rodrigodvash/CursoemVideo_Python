from datetime import date # Biblioteca para pegar a data atual da máquina;

print('Ano Bissexto')
ano = int(input('Qual o ano para verificar? Digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
    # Pega o ano atual o PC e faz a troca para a variável ano;

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO É BISSEXTO')
