# Crie um algoritmo que leia um número inteiro e mostre na tela o seu antecessor e seu sucessor.
n1 = int(input("Digite um número:"))
print('O antecessor de {} é {} e o sucessor é {}'.format(n1, int(n1 - 1), int(n1 + 1)))