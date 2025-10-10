#Programa média de alunos
print('[---Calculadora de média escolar---]')

aluno = input('Digite o nome do aluno:')
n1 = float(input('Digite a primeira nota de {}:'.format(aluno)))
n2 = float(input('Digite a segunda nota de {}'.format(aluno)))

#calculo da média:
m = (n1 + n2) / 2

print('A média de {} é {:.2f}'.format(aluno, m))