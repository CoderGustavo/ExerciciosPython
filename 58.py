from random import randint
pc = randint(1, 10)
palpites = 0
tentativa = 0
print('Eu sou seu computador...\nPensei em um número entre 1 e 10\nVocê consegue adivinhar?')
while tentativa != pc:
    tentativa = int(input('Digite seu palpite: '))
    if tentativa != pc:
        print('Errou!')
        if tentativa > pc:
            print('Menos...')
        else:
            print('Mais...')
    palpites += 1
print('Parabens! você acertou utilizando {} palpites!'.format(palpites))