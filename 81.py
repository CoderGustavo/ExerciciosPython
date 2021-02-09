valores = list()
valores.append(int(input('Digite um valor: ')))
while True:
    continuar = str(input('Deseja continuar? [S/N] '))
    while continuar not in 'SsNn':
        continuar = str(input('Algo deu errado! Deseja continuar? [S/N]'))
    if continuar in 'Ss':
        valores.append(int(input('Digite um valor: ')))
    else:
        break
print('=-='*10)
print(f'Foi digitado {len(valores)} números!')
print(f'Os números digitados em ordem decrescente foi: {sorted(valores, reverse=True)}')
if 5 in valores:
    print(f'O valor 5 está na lista!')
else:
    print(f'O valor 5 NÃO está na lista!')
print('=-='*10)
