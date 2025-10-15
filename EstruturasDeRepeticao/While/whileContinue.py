# O comando continue faz com que o laço pule a iteração atual e vá para a próxima.
for num in range(1, 11):
    if num == 5:
        continue # Pula o número 5
    else:
        print(num)
print('Saiu do laço')