# Comentário: Este código solicita o nome do usuário e exibe uma mensagem de boas-vindas personalizada.
nome = input("Digite seu nome: ")
# print("Olá, " + nome + "! Seja bem-vindo(a)!") # Concatenação de strings
print('Olá, {}! Seja bem-vindo(a)'.format(nome)) # Uso de f-strings para formatação de strings