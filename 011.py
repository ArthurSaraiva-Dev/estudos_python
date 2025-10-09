#Programa quantas latas de tinta são necessários

print('[--- Quantas latas de tinta são necessárias para sua parede: ---]')
print('[Cada lata de tinta cobre 2m²]')
largura = float(input('Digite a Largura da parade em metros: '))
altura = float(input('Digite a Altura da parade em metros: '))

area = largura * altura
latas = area // 2

print('Sua parede tem {:.2f}m², sendo assim, são necessárias {:.1f} latas de tinta'.format(area, latas))