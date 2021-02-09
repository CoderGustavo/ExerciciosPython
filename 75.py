val1 = int(input('Digite um valor: '))
val2 = int(input('Digite um valor: '))
val3 = int(input('Digite um valor: '))
val4 = int(input('Digite um valor: '))
valores = (val1,val2,val3,val4)
print(f'Existem {valores.count(9)} noves na tupla!')
if 3 in valores:
    print(f'Foi digitado o numero 3 na {valores.index(3)+1}° posição')
else:
    print('Foi digitado nenhum numero 3')
print(f'Os numeros pares sao: ', end=' ')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
    else:
        print(0, end=' ')