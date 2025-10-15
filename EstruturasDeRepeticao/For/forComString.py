# Exemplo de uso do for com strings e listas
nome = 'ARTHUR'

print('[--- Verificando letras do nome ---]') 
for letra in nome:
    print(letra) # Imprime cada letra do nome em uma linha diferente

# Exemplo de uso do for com listas
print('\n[--- Sequencia de nomes ---]')
nomes = ['Carlos','Armando','Lucas','Arthur','Rayssa']
for nome in nomes:
    print(nome) # Imprime cada nome da lista em uma linha diferente

# Exemplo de contagem
print('\n[--- Contagem de letras ---]')
texto = str(input('Digite um texto qualquer: ').strip())
letra_para_contar = str(input('Digite a letra que deseja contar no texto: ').strip())
contador = 0

for letra in texto.lower(): # Converte o texto para minúsculas para contar 'r' e 'R' igualmente
    if letra == letra_para_contar.lower():
        contador += 1
print(f'A letra [{letra_para_contar}] aparece [{contador}] vezes no texto.')