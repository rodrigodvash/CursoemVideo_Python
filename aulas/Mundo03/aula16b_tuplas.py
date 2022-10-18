print('{:#^50}'.format(' AULA SOBRE TUPLAS '))

# Não se soma os conteúdos das tuplas, une uma em sequência da outra;
par   = (0, 2, 4, 6, 8, 0)
impar = (1, 3, 5, 7, 9, 0)
a = par + impar
b = impar + par
# A ordem tem total influência!!
print(a)
print(b)
print(a.count(0)) # Conta quantas vezes temos o valor dentro da tupla;
print(b.index(0)) # Mostra o index do valor na primeira ocorrência;
print(a.index(0, 1)) # Mostra o index a partir da sua primeira ocorrência;
print()

# Tuplas aceitam dados de tipos diferentes;
pessoa = ('Rodrigo', 30, 70.5)
print(pessoa)

# A única modificação possível em uma tupla, é sua eliminação (por inteira):
del(pessoa)
# print(pessoa) Gera um erro, pois a tupla foi apagada e não existe mais na memória;
