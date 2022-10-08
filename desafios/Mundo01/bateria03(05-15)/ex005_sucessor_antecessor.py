numero = int(input('NÚMERO = '))
print('O antecessor de {}{}{} é {}{}{},'.format("\033[0;37;44m", numero, '\033[m', "\033[1;33;41m", numero-1, '\033[m'), end=" ")
print('e em contrapartida, seu sucessor é {}{}{}.'.format("\033[1;34;42m", numero+1, '\033[m'))
