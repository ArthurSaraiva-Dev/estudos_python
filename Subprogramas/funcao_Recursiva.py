def regressiva(x):
    print(x)
    if x > 0:
        regressiva(x - 1)
    else:
        print('Fim.')

regressiva(10)

# não recursivo

for y in range(10, -1, -1):
    print(y)