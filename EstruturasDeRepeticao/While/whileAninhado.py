while True:
    print('Dentro do loop_1')
    opcao1 = input('Quer sair do loop_1? (s/n): \n')
    if opcao1 == 's':
        break
    else:
        while True:
            print('Dentro do loop_2')
            opcao2 = input('Quer sair do loop_2? (s/n): \n')
            if opcao2 == 's':
                break
        print('Saiu do loop_2')
print('Saiu do loop_1')