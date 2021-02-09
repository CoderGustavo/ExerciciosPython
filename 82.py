valores = list()
pares = list()
impares = list()
valor = int(input('Digite um valor: '))
valores.append(valor)
if valor % 2 == 0:
    pares.append(valor)
else:

    impares.append(valor)
while True:
    continuar = str(input('Deseja continuar? [S/N] '))
    while continuar not in 'SsNn':
        continuar = str(input('Algo deu errado! Deseja continuar? [S/N]'))
    if continuar in 'Ss':
        valor = int(input('Digite um valor: '))
        valores.append(valor)
        if valor % 2 == 0:
            pares.append(valor)
        else:
            impares.append(valor)
    else:
        break

print(f'Os valores da lista Valores são respectivamente: {valores}')
print(f'Os valores pares da lista Valores são respectivamente: {pares}')
print(f'Os valores impares da lista Valores são respectivamente: {impares}')
