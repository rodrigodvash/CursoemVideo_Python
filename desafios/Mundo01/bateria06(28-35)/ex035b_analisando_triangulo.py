print('Analisando triângulo')
r1 = float(input('RETA 01: '))
r2 = float(input('RETA 02: '))
r3 = float(input('RETA 03: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima FORMAM um triângulo')
else:
    print('Os segmentos acima NÃO FORMAM um triângulo')