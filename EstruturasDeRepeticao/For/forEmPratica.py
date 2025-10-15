#calculando o quadrado dos núemeros

print('[--- Calculando o quadrado dos números ---]')

numero = [1,2,3,4,5,6,7,8,9,10]

for num in numero:
    quadrado = num ** 2
    print(f'O quadrado de {num} é igual a {quadrado}')

# Tabuada
print('\n[--- Tabuada ---]')
n = int(input('Digite um número para obter sua tabuada: '))

for i in range(1, 11):
    tabuada = n * i
    print(f'{n} X {i} = {tabuada}')

