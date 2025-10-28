def taximetro(distancia):
    def calculaMult():
        if distancia < 5:
            return 1.5
        else:
            return 1.2

    multiplicador = calculaMult()
    largada = 3.0
    km_rodado = 2.0
    valor = (largada + (distancia * km_rodado)) * multiplicador
    return valor

dist = eval(input('Entre com a distância a ser percorrida em km (quilômetros): '))
pagamento = taximetro(dist)
print(f'O valor a ser pago é R$ {pagamento:.2f}')
