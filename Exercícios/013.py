#Programa calculador de aumento de salário

funcionario = input('Digite o nome do funcionário: ')

salario = float(input('Digite o salário atual de {}: '.format(funcionario)))

novo_salario = salario * 1.15

print('O novo salário do funcionário(a) {} com 15% de aumento é: R${:.2f}'.format(funcionario, novo_salario))