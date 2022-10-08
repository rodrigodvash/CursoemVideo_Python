print('Analisando triângulo')
reta01 = float(input('RETA 01: '))
reta02 = float(input('RETA 02: '))
reta03 = float(input('RETA 03: '))
if abs(reta02 - reta03) < reta01 and reta01 < reta02 + reta03:
    if abs(reta01 - reta03) < reta02 and reta02 < reta01 + reta03:
        if abs(reta01 - reta02) < reta03 and reta03 < reta01 + reta02:
            print('É possível criar o triângulo')
else:
    print('Não é possível criar o triângulo.')