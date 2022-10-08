print('Conversor de medida')
valor = float(input('Informe o valor em METROS: '))
decametro = valor / 10
hectometro = decametro / 10
kilometro = hectometro / 10
decimetro = valor * 10
centimetro = decimetro * 10
milimetro = centimetro * 10
print(f'Convertendo {valor:.1f}m, temos:\n' +
      f'{kilometro:.3f}km;\n' +
      f'{hectometro:.2f}hm;\n' +
      f'{decametro:.1f}dam;\n'
      f'{decimetro:.1f}dm;\n' +
      f'{centimetro:.1f}cm;\n' +
      f'{milimetro:.1f}mm;')
