a = [2, 3, 4, 7]
# b = a: No Python, isso significa que criamos uma ligação entre a lista a e b:
#        Se alterar uma, a outra também se altera:
b = a
b[2] = 9
print(f'Lista A: {a}')
print(f'Lista B: {b}\n')

# Para criar uma cópia de uma lista, usamos o fatiamento da seguinte forma:
c = a[:]
c[2] = 1
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')
