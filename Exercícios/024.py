# Exercicio 024 - Verificando o início de um nome de cidade
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cidade = input('Digite o nome de uma cidade: ').strip()
print(cidade[:5].upper() == 'SANTO')