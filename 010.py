#Programa "Quanto posso comprar em dólar?"
print('[--- Qaunto em Dólar ---]')

real = float(input('Digite quanto você tem em reais: R$'))
dolar = real / 5.33

print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))