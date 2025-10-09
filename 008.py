#Programa conversor de metros para centímetros e milímetros
print('[---Conversor de medidas---]')

metros = float(input('Digite o valor em metros:'))

cm = metros * 100
mm = metros * 1000

print('{} metros equivalem a {:.0f} em centímetros e {:.0f} em milímetros'.format(metros, cm, mm))