print(f'{" Lista Ordenada sem Repetições ":#^70}')

lista = list()
for i in range(0, 5):
    numero = int(input(f'Digite o {i+1}º valor: '))
    # Primeira adição: Ou é no index 0, ou é maior que o último valor da lista:
    if i == 0 or numero > lista[-1]:
        lista.append(numero)
        print(f'Valor adicionado ao final da lista, no index {lista.index(numero)}.')

    else:
    # Condição só ocorre quando o valor é menor que o último
        cont = 0
        # Variável contadora. Sempre que o 'loop-for' completar uma iteração, ela volta para 0;
        while cont < len(lista):
        # Enquanto 'cont' for menor que o tamanho da lista:
            if numero <= lista[cont]:
            # O valor digitado é menor ou igual ao valor da lista no índice do 'cont'?
                lista.insert(cont, numero)
            # Se sim, ele entra no índice correspondente ao valor de 'cont';
                print(f'Valor adicionado na posição {lista.index(numero)}.')
#               print(f'Valor adicionado na posição {cont}.')
                break # Só precisa inserir 1x;
            cont += 1
            # Se não, ela incrementa para comparar novamente;
print(f'Lista: {lista}')
