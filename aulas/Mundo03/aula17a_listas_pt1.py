num = (2, 5, 9, 1)
# num[2] = 3 : Erro!
print(f'{num} que é uma {type(num)}')

num2 = [2, 5, 9, 1]
print(f'{num2} = Lista')

num2[2] = 3 # Permite reatribuição;

# num2[4] = 3 : Isto gera um erro, pois não existe o índice 4 atualmente na lista;

# Para adicionar (ao final da lista), podemos usaro método .append:
num2.append(7)
print(f'{num2} que é uma {type(num2)}')

#também é possível ordenar a lista, igual se faz com as tuplas:
num2.sort()
print(f'Depois do ".sort": {num2}')

num2.sort(reverse=True)# Também é possível fazer a ordenação reversa;
print(f'Ordenação reversa: {num2}')

num2.insert(2, 0) # Inserir valores num índex à escolha;
print(f'Inserindo um valor em um índex (index 2 neste exemplo): {num2}')

print(f'Esta lista tem {len(num2)} elementos.')

num2.pop(2) # Quando passada sem parâmetros (sem o índex), este método elimina o último valor da lista;
print(f'Agora a lista possui {len(num2)} elementos: {num2}')

num2.insert(2, 2)
num2.remove(2) # Elimina o elemento passado como parâmetro (se houverem outros iguais, elimina o primeiro);
print(f'Depois do remove, com mais de um elemento igual: {num2}')

# Se tentar remover um elemento que não exista na lista, é gerado um erro, para isso:
if 4 in num2: # O comando IN é muito útil;
    num2.remove(4)
else:
    print('O valor 4 não consta na lista.')
