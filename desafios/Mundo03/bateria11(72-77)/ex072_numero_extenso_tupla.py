print(f'{" NÚMEROS POR EXTENSO ":=^40}')

# Tupla com números por extenso;
numeros = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO',
           'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE',
           'DOZE', 'TREZE', 'CATORZE', 'QUIZE', 'DEZESSEIS',
           'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    numDigitado = int(input('Digite um número entre 0 e 20: '))
    # Tratando a variável numDigitado para receber somente os valores do intervalo;
    while True:
        if numDigitado > 20 or numDigitado < 0:
            numDigitado = int(input('Por favor, digite um número entre 0 e 20: '))
        else:
            break
    # Print com o resultado:
    print(f'Você digitou o número {numeros[numDigitado]}')

    # Perguntar se o utilizador quer continuar com o programa;
    continuar = str(input('Você deseja continuar com o programa [S/N]? ')).strip().upper()[0]
    if continuar in 'Ss':
        continue
    else:
        break

'''a = ''
if numDigitado == numeros[0]:
    a = 'ZERO'
elif numDigitado == numeros[1]:
    a = 'UM'
elif numDigitado == numeros[2]:
    a = 'DOIS'
elif numDigitado == numeros[3]:
    a = 'TRÊS'
elif numDigitado == numeros[4]:
    a = 'QUATRO'
elif numDigitado == numeros[5]:
    a = 'CINCO'
elif numDigitado == numeros[6]:
    a = 'SEIS'
elif numDigitado == numeros[7]:
    a = 'SETE'
elif numDigitado == numeros[8]:
    a = 'OITO'
elif numDigitado == numeros[9]:
    a = 'NOVE'
elif numDigitado == numeros[10]:
    a = 'DEZ'
elif numDigitado == numeros[11]:
    a = 'ONZE'
elif numDigitado == numeros[12]:
    a = 'DOZE'
elif numDigitado == numeros[13]:
    a = 'TREZE'
elif numDigitado == numeros[14]:
    a = 'QUATORZE'
elif numDigitado == numeros[15]:
    a = 'QUINZE'
elif numDigitado == numeros[16]:
    a = 'DEZESSEIS'
elif numDigitado == numeros[17]:
    a = 'DEZESSETE'
elif numDigitado == numeros[18]:
    a = 'DEZOITO'
elif numDigitado == numeros[19]:
    a = 'DEZENOVE'
elif numDigitado == numeros[20]:
    a = 'VINTE'
print(f'Você digitou o número {a}.')'''
