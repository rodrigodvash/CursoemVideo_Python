print('Progressão Aritmética\n')

print('Precisamos de duas informações:')
primeiro = int(input('Qual é o primeiro termo: ')) # Entra com o primeiro valor da PA;
razao = int(input('E qual é a razão: ')) # Entra com o valor das somas;

print('Vamos à Progressão Aritmética...\n')
ultimo = razao * 11 # Defini aqui o valor final do intervalo, valores muito baixos não chegavam a décima somatória;
# ultimo = primeiro + (10 - 1) * razao;
temp = 1
for i in range(primeiro, ultimo+1, razao):
    if temp <= 10: # Aqui não permite que o valor temporário não ultrapasse os 10 pedidos, e com valores altos, sempre ia até o 11;
        print(f'{temp:2}º valor: {i}')
        temp += 1 # Auto-incremento do valor temporário;
print('Espero ter ajudado.')
