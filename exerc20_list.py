import random
n1 = str(input('escreva o seu nome '))
n2 = str(input('escreva o seu nome '))
n3 = str(input('escreva o seu nome '))
n4 = str(input('escreva o seu nome '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('Os nomes em ordem são: {}'.format(lista))