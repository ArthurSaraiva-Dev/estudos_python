# Definição de função com parâmetros
def calcula_imc (peso, altura):
    return peso * 100 / (altura * 2) # Cálculo do Índice de Massa Corporal (IMC)



peso = eval(input('Digite seu peso em kg: '))
altura = eval(input('Digite sua altura em centimetros: '))
imc = calcula_imc(peso, altura)

print(f'Seu IMC é {imc:.2f}')