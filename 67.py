while True:
    valor = int(input('Você quer ver a tabuada de qual valor? '))
    if valor < 0:
        break
    print('=-='*10)
    for n in range(1, 11):
        print(f'{valor} x {n} = {valor*n}')
    print('=-=' * 10)
