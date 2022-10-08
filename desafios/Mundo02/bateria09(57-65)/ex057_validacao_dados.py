sexo = str(input('Informe o sexo da pessoa [F/M]: ')).strip().upper()[0] # Assim só pega a primeira letra;

while sexo not in 'FM':
    print('Por favor, informe um valor correto [F/M]: ', end='')
    sexo = str(input('')).strip().upper()[0]

if sexo == 'F':
    sexo1 = 'Feminino'
elif sexo == 'M':
    sexo1 = 'Masculino'
# Fazendo assim, não se altera o valor da variavel 'sexo';
print(f'O sexo da pessoa é {sexo1}.')
