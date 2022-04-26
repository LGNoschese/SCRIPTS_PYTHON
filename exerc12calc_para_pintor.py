n1 = float(input('insira a largura da parede em metros '))
n2 = float(input('insira a altura da parede em metros '))
area = n1 * n2
result = area / 2
print('A metregem quadrada da parede à ser pintada é {:.2f} m2,\n e a quantidade de tinta necessária para a pintura dessa parede é {:.2f} litros.'.format(area, result))