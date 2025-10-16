
for raiz in range(32, 100):
    num = raiz * raiz
    maior = num // 100
    menor = num % 100
    if (menor + maior) == raiz:
        print(num)
        print(menor)
        print(maior)
        print(raiz)
print('Fim')
print(f'Saiu {raiz}')