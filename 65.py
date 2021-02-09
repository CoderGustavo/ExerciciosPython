vezes = soma = maior = menor = 0
continuar = 'S'
while continuar in 'S':
    valor = int(input('Digite um valor: '))
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    vezes += 1
    soma += valor
    if vezes == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
print('Foram digitados {} numeros'.format(vezes))
print('A soma dos valores é: {}'.format(soma))
print('A média dos valores é: {}'.format(soma/vezes))
print('O maior valor é: {}'.format(maior))
print('O menor valor é: {}'.format(menor))