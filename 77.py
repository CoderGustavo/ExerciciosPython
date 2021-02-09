palavras = ('Cagar', 'peidar', 'nanar', 'andar', 'aprender', 'cheirar')
cont = 0
for n in palavras:
    print(f'Na palavra {n} temos as vogais: ', end='')
    for letra in n:
        if letra in 'aeiou':
            print(letra, end=' ')
    print('\n')
    cont += 1



