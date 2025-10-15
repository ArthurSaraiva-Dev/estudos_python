texto = 'Olá, Mundo!'

# Acessando caracteres individuais
primeiro_caractere = texto[0]  # 'O'
ultimo_caractere = texto[-1]    # '!'

print(f'Primeiro caractere: {primeiro_caractere}')
print(f'Último caractere: {ultimo_caractere}')

# Fatiamento de strings
subtexto = texto[5:10]  # 'Mundo'
print(f'Subtexto: {subtexto}')

# Dividindo em lista

lista_palavras = texto.split()
print(f'Lista de palavras: {lista_palavras}')

# Substituindo partes da string
novo_texto = texto.replace('Mundo', 'Python')
print(f'Novo texto: {novo_texto}')

# Convertendo para maiúsculas e minúsculas
texto_maiusculo = texto.upper()
texto_minusculo = texto.lower()
print(f'Texto em maiúsculas: {texto_maiusculo}')
print(f'Texto em minúsculas: {texto_minusculo}')

# Removendo espaços em branco
texto_com_espacos = '   Olá, Mundo!   '
texto_sem_espacos = texto_com_espacos.strip()
print(f'Texto sem espaços: "{texto_sem_espacos}"')
