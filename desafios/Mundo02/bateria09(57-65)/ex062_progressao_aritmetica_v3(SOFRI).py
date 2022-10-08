print('-==-' * 15)
print('\tProgressão aritmética V3')
print('-==-' * 15)
primeiro = int(input('\tQual é o primeiro termo? '))
razao = int(input('\tE a razão (intervalos)? '))

# Variável a somatória do primeiro com a razão, iniciada com o valor do primeiro termo;
termo = primeiro
# Index do loop, quando seu valor for igual ao da razão, ele finaliza o while da somatória;
index = 1
# Total de termos da P.A. Sempre que desejar continuar com a PA, ele se incrementa;
total_termos = 0
# Variável para adicionar termos à PA. Se reinicia quando o utilizador desejar mais termos;
add_termos = 10

# Na primeira vez, vale 10, nas próximas vale o valor de entrada do utilizador;
while add_termos != 0:
    total_termos += add_termos # total = total + adicionar (0 = 0 + 10 na primeira vez!);
    print('\t', end='')
    # Loop das somas. Finaliza quando o index for maior que o valor total de termos;
    while index <= total_termos:
        print(f'{termo}, ', end='')
        termo += razao # termo = termo + razao;
        index += 1 # auto-incremento de index;
    print('PAUSA...\n' + ('-==-') * 15)
    add_termos = int(input('\tQuantos termos quer mostrar a mais? '))
print('-==-' * 15)
print(f'\tP.A. = {termo}, com {total_termos} termos.')
print('-==-' * 15)
