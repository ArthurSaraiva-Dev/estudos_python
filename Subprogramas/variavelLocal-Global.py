# Exemplo de variável local e global em Python
def f1():
    global x  # Declarando x como variável global
    x = 10
    print(f'Valor de x dentro de f1: {x}')
    return x

def f2():
    x = 20 ** 2
    print(f'Valor de x dentro de f2: {x}')

x = 0
 # Variável global
print(f'Valor de vn antes de chamar f1: {x}')
f1()

print(f'Valor de vn depois de chamar f1: {x}')
f2()

print(f'Valor de vn depois de chamar f2: {x}')
print(f'Valor de x fora das funções: {x}')