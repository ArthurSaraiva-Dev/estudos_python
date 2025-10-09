#Programa reajuste de preços (%5)

print('[--- Reajusto de Preços ---]')
produto = input('Digite o nome do produto: ')
preco = float(input('Digite o preço do produto: R$'))

novo_preco = preco + (preco * 0.05)

print('O novo preço do produto ({}) com 5% de aumento é R${:.2f}:'.format(produto, novo_preco))