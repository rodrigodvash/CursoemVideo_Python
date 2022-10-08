from math import sin, cos, tan, radians
# O radians converte de graus para radianos (raio);

print('Seno, cosseno e tangente')
angulo = float(input('Qual o ângulo a ser calculado? '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'Seno: {seno:.2f};\nCosseno: {cosseno:.2f};\nTangente: {tangente:.2f};')