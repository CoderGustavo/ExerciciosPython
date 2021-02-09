prods = ('lápis', 1, 'borracha', 2)
for pos, n in enumerate(prods):
    if pos % 2 == 0:
        print(f'{n:.<30}', end='')
    elif pos % 2 == 1:
        print(f'R${n:>1.2f}')