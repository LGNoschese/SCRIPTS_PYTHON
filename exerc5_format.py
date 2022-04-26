n1= int(input('digite um valor '))
n2= int(input('digite outro valor '))
s = n1 + n2
m = n1*n2
d = n1/n2
d1= n1//n2
e = n1**n2
print('A soma é {},\n o produto é {}, \n a divisão é {:.4f}'.format(s, m , d), end=' ')
print('a divisão inteira é {},\n e a potência é {}'.format(d1, e))