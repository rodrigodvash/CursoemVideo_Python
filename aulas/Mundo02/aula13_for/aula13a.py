for i in range(0, 6):
    print(f'Oi + {i}')
print('FIM\n')

for i in range(10, 0, -1):
    print(f'Numero {i}')
print()

for i in range(0, 21, 2):
    print(f'Par {i}')
print()

num = int(input('NÚMERO: '))
for i in range(1, num+1):
    print(f'Do 1 ate o {i}')
print()

start = int(input('INÍCIO = '))
end = int(input('FIM = '))
passs = int(input('PASSO = '))
for index in range(start, end+1, passs):
    print(f'From {start} to {end}, {passs} by {passs}: {index}')

