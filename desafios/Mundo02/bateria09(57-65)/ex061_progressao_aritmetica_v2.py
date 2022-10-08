print('PROGRESSÃO ARITMÉTICA\n')

primeiro = int(input('Qual o primeiro termo da P.A.: '))
razao = int(input('E a razão da P.A: '))
termo = primeiro
index = 0

while index < 9:
    termo = termo + razao
    index += 1
print(f'A P.A. de {primeiro} com razão {razao} é = {termo}')