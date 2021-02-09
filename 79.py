valores = list()
valores.append(int(input('Digite um valor: ')))
while True:
    continuar = str(input('Deseja continuar? [S/N] '))
    while continuar not in 'SsNn':
        continuar = str(input('Algo deu errado! Deseja continuar? [S/N] '))
    if continuar in 'Ss':
        valor = int(input('Digite um valor: '))
        if valor in valores:
            print('Valor já digitado')
        else:
            valores.append(valor)
    else:
        break
print('Foi ditatado os valores: ', end='')
for v in sorted(valores):
    print(f'{v}...', end='')



