print(f'{"= Solução mais correta do exercício =":-^50}')

expressao = str(input('Escreva sua expressão: ')).strip()
pilha = list()
for parenteses in expressao:
    if parenteses == '(':
        pilha.append('(')
    elif parenteses == ')':
        if len(pilha) > 0:
            pilha.pop() # Para cada ')', elimina um '(' na lista pilha;
        else:
            pilha.append(')')
            break # Para adicionar 1x e parar;

if len(pilha) == 0: # Se a lista plha estiver vazia, então todos os parênteses foram fechados;
    print('Expressão correta, parabéns!')
else:
    if pilha[0] == '(':
        print('Tem "(" a mais na sua expressão!')
    elif pilha[0] == ')':
        print('Tem ")" a mais na sua expressão!')
