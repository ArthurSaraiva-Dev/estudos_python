escolha = input('Digite uma opção de função 1 ou 2: ')

if escolha == '1':
    def funcao1(x):
        return x + 1
    s = funcao1(10)

elif escolha == '2':
    def funcao2(x):
        return x + 2
    s = funcao2(10)