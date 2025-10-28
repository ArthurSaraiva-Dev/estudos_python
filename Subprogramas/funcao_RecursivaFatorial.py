def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

vfat = fatorial(5)
print(f'Resultado recursiva: {vfat}')

# Função fatorial não recursiva

def fatorial_NR(n):
    fat = 1
    if n == 1 or n == 0:
        return fat
    else:
        for x in range(2, n + 1):
            fat = fat * x
        return fat
    
vfatNR = fatorial_NR(5)
print(f'Resultado iterativa: {vfatNR}')