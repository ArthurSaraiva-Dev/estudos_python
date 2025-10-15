# Criando um dicionário com alguns pares chave-valor
dicionario = {
    'nome': 'Arthur',
    'idade': 19,
    'cidade': 'São Gonçalo'
}

# Acessando valores usando chaves
nome = dicionario['nome']
idade = dicionario['idade']
cidade = dicionario['cidade']

print(f'Nome: {nome} \nIdade: {idade} \nCidade: {cidade}')

# Adicionando um novo par chave-valor
dicionario['profissão'] = 'Estudante de ADS'
print(f'\nDicionário atualizado: \n{dicionario}')

# Modificando um valor existente
dicionario['idade'] = 20
print(f'\nDicionário após modificação de idade: \n{dicionario}')

# Removendo um par chave-valor
del dicionario['cidade']
print(f'\nDicionário após a remoção da chave "cidade": \n{dicionario}')

# Mostrando todas as chaves, valores e itens do dicionário
chaves = dicionario.keys()
valores = dicionario.values()
print(f'\nChaves: {list(chaves)} \nValores: {list(valores)}')

# Iterendo sobre o diconário
print('\nIterando sobre o dicionário:')
for chave, valor in dicionario.items():
    print(f'{chave}: {valor}')

# Verificando se uma chave existe no dicionário
print('\nVerificando a existência da chave "nome":')
if 'nome' in dicionario:
    print(f'\nA chave "nome" existe no dicionário. Seu valor é: {dicionario["nome"]}')
else:
    print('\nA chave "nome" não existe no dicionário.')

# Usando o método get para acessar valores de forma segura
print('\nAcessando a chave "profissão" usando get:')
profissao = dicionario.get('profissão', 'Não especificado')
print(f'\nProfissão: {profissao}')

# Limpando o dicionário
dicionario.clear()
print(f'\nDicionário após limpeza: {dicionario}')