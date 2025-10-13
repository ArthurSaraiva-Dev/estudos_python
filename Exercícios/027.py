#Programa que lê o nome completo de uma pessoa e mostra:
# O primerio e o último nome separadamente.

nome = input('Digite seu nome completo: ').strip()
nome_separado = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(nome_separado[0]))
print('Seu último nome é {}.'.format(nome_separado[len(nome_separado) - 1]))