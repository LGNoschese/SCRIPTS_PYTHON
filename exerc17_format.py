import math
num1 = float(input('digite o cateto oposto '))
num2 = float(input('digite o cateto adjacent '))
math.hypot (num1, num2)
print ('O cateto oposto é {}, o cateto adjascente é {} e a sua hipotenusa é {}'.format(num1, num2, math.hypot(num1,num2)))