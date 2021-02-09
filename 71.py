notacin = notadez = notaum = notavin = 0

print('-=-'*10)
print('BANCO GUSIN')
print('-=-'*10)
saque = int(input('Quando vc deseja sacar? R$'))
notacin = saque/50
if notacin // 1 == notacin:
    print(notacin)
else:
    notavin = (saque - (int(notacin)*50)) / 20
    notadez = (saque - ((int(notacin) * 50)+(int(notavin) * 20))) / 10
    notaum = (saque - ((int(notacin) * 50) + (int(notavin) * 20) + (int(notadez) * 10))) / 1
    if int(notacin) != 0:
        print(f'{int(notacin)} notas de R$50')
    if int(notavin) != 0:
        print(f'{int(notavin)} notas de R$20')
    if int(notadez) != 0:
        print(f'{int(notadez)} notas de R$10')
    if int(notaum) != 0:
        print(f'{int(notaum)} notas de R$1')
print('Volte sempre ai BANCO GUSIN')