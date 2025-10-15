# O código acima imprime apenas os números ímpares de 1 a 10.
for num in range(1, 11):
    if num % 2 == 0:
        pass # Ignora os números pares
    else:
        print(num)
print('Fim do laço')

s = 0
a = 1

while s < 5:
    s = 3*a
    a += 1
    print(s)