# Definindo função com parâmetros
def taximetro(distancia, multiplicador=1):
    largada = 3
    km_radado = 2
    valor = (largada + distancia * km_radado) * multiplicador
    return valor


distancia = float(input('Digite a distância percorrida em km: '))
bandeira = int(input('Digite a bandeira (1 ou 2): '))

pagamento = taximetro(distancia, bandeira)
print(f'O valor a ser pago é R$ {pagamento:.2f}')