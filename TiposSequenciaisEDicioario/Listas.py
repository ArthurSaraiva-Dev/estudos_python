# Lista com alguns elementos
lista = [10, 20, 30, 40, 50]

# Acessando elementos por índice
elemento_0 = lista[0] # Primeiro elemento
elemento_1 = lista[1] # Segundo elemento

# Imprimindo os elementos acessados
print(f'Primeiro elemento: {elemento_0}')
print(f'Segundo elemento: {elemento_1}')

# Adicionando um elemento ao final da lista
lista.append(60)
print(f'Lista após adicionar 60: {lista}')

# Inserindo um elemento em uma posição específica
lista.insert(2, 25) # Insere 25 na posição de índice 2
print(f'Lista após inserir 25 na posição 2 (índice 1): {lista}')

# Removendo um elemento pelo valor
lista.remove(40) # Remove o valor 40
print(f'Lista após remover 40: {lista}')

# Removendo um elemento pelo índice
lista.pop() # Remove o elemento na posição final
print(f'Lista após remover o elemento na posição final: {lista}')

# Acessando sub-grupo da lista
sub_lista = lista[1:4] # Elementos do índice 1 ao 3
print(f'Sub-lista do índice 1 ao 3: {sub_lista}')

# Verificando tamanho da lista
tamanho = len(lista)
print(f'Tamanho da lista: {tamanho}')

# Revertendo a lista
lista.reverse()
print(f'Lista revertida: {lista}')

# Ordenando a lista
lista.sort()
print(f'Lista ordenada {lista}')

# Iterando sobre a lista
print('Iterando sobre a lista:')
for elemento in lista:
    
    print(elemento)


