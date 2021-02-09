from functools import reduce
valor = int(input('Digite um valor: '))
inival = valor
fator = []
while valor != 0:
    fator.append(valor)
    valor -= 1
fatorial = reduce(lambda x,y:x*y, fator)
n = 0
while n != inival:
    print('{}'.format(fator[n]), end='')
    print(' = ' if fator[n]==1 else 'x', end='')
    n+=1
print('{}'.format(fatorial), end='')


