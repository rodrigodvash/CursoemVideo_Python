print(f'{" Contando Vogais em Tupla ":#^40}')
print()

tupla = (
    'aprender', 'programar', 'linguagem', 'python',
    'curso', 'gratis', 'estudar', 'praticar',
    'trabalhar', 'mercado', 'programador', 'futuro'
)

# Primeiro, um loop para percorrer a tupla;
for palavra in tupla:
        print(f'Na palavra {palavra.upper()} temos as vogais: ', end="")
        # Depois um segundo loop para percorrer cada palavra isolada (que naturalmente é uma lista de letras);
        for letra in palavra:
            # Verificando palavra por palavra da tupla;
            if letra in 'aeiou':
                # Se houver a condição 'aeiou' na palavra, ele somente irá imprimir a vogal correspondente;
                print(letra.lower(), end=' ')
        print()
