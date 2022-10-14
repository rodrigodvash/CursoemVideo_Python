print('{:#^50}'.format(' AULA SOBRE TUPLAS '))
# Tuplas são IMUTÁVEIS!
# Index:      #0          #1       #2      #3
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') # Tuplas ficam entre parentêses;
print(lanche)
print(lanche[3])
print(lanche[-4])
print(lanche[1:3])
print(lanche[:2])
print(lanche[2:])
print(lanche[-3:])
print()
# lanche[1] = 'Refrigerante' // Gera um erro!

#///////////////////////////////////////////////////////////////////////////////////////////////////////
for comida in lanche:
    print(f'Eu vou degustar um(a) {comida}!')
print()

for posicao, comida in enumerate(lanche):
    print(f'Eu vou degustar um(a) {comida} na posição {posicao};')
print()
# Possuem a mesma sintaxe, mas caso necessitar da posição, precisará do enumerate, ou do exemplo abaixo;
#///////////////////////////////////////////////////////////////////////////////////////////////////////

# Caso ncessite da posição, esta é uma boa opção;
animais = ('Besouro', 'Canário', 'Golfinho', 'Gato', 'Cavalo')
for index in range(0, len(animais)):
    print(f'Eu vi um {animais[index]}.')
print()

# Caso necessitar mostrar a tupla em ordem:
print(sorted(lanche)) # Ele só mostra, não altera o dado!
print(type(sorted(lanche)))
print(sorted(animais))
print(type(sorted(animais)))
print(f'Tupla 1: {lanche} e Tupla 2: {animais}')
