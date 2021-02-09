val1 = int(input('Digite 1 valor:'))
val2 = int(input('Digite outro valor:'))
menu = ['Somar','Multiplicar','Maior','Outros Numeros','Sair']
op = 0
while op != 5:
    for n in range (1,6):
        print('[{}] {}'.format(n,menu[n-1]))
    op = int(input('Digite a operação desejada:'))
    if op == 1:
        print('A soma dos valores é: {}\n'.format(val1+val2))
    elif op == 2:
        print('A multiplicação entre os valores é: {}\n'.format(val1*val2))
    elif op == 3:
        if val1>val2:
            maior = val1
        else:
            maior = val2
        print('O maior dos numeros é o: {}\n'.format(maior))
    elif op == 4:
        print('Você irá atualizar os numeros...')
        val1 = int(input('Digite 1 valor:'))
        val2 = int(input('Digite outro valor:'))
    else:
        print('Operação Ínvalida!')
print('Você escolheu sair!')