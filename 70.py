totalpreco = maior_m = menor_preco = cont = 0
menor_prod = ' '
while True:
    nome = str(input('Digite o nome do produto:'))
    preco = float(input('Digite o preço do produto: [0.0]'))
    continuar = ' '
    cont += 1
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar:')).strip().upper()[0]
    totalpreco += preco
    if preco > 1000.0:
        maior_m += 1
    if cont == 1:
        menor_prod = nome
    else:
        if preco < menor_preco:
            menor_prod = nome
    if continuar == 'N':
        break
print(f'O total gasto foi {totalpreco}!')
print(f'{maior_m} custam mais que 1000 reais!')
print(f'O/A {menor_prod} é o produto mais barato!')