nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Você é maior de idade, {}.'.format(nome))
else:
    print('Você é menor de idade, {}.'.format(nome))