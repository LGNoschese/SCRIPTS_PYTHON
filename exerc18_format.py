import math
angulo = float(input('digite o angulo '))
cosseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('o angulo é {},\n o cosseno desse angulo é {},'.format(angulo, cosseno),end='')
print('o seno desse angulo é {},\n e a tangente desse angulo é {},'.format(seno, tangente))