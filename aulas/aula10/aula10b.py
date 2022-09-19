nota01 = float(input('NOTA 01: '))
nota02 = float(input('NOTA 02: '))
media = (nota01 + nota02) / 2
if media >= 6:
    print(f'NOTA FINAL = {media:.1f}, APROVADO!')
else:
    print(f'NOTA FINAL = {media:.1f}, REPROVADO!')
