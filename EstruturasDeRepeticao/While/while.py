print('Antes de while')
palavra = input('Digite uma palavra: ')

while palavra != 'sair':
    print('Dentro do while')
    palavra = input('Digite [sair] para sair do loop: ')
print('Você saiu do laço while')