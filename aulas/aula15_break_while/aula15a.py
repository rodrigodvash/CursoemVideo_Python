numero = soma = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break  # Comando para interromper um loop;
    soma += numero
print(f'SOMA = {soma};')
