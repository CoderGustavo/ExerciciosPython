from random import randint
vitoria = 0
while True:
    pc = randint(1, 10)
    print('=-='*20)
    print('VAMOS JOGAR PAR OU ÍMPAR!')
    print('=-='*20)
    valor = int(input('Digite um valor: '))
    ip = 'A'
    while ip not in 'IP':
        ip = str(input('Impar ou Par? [I/P]')).strip().upper()[0]
    if (valor+pc) % 2 == 0:
        ipc = 'P'
        ipg = 'Par'
    elif (valor+pc) % 2 == 1:
        ipg = 'Ímpar'
        ipc = 'I'
    print('---' * 10)
    print(f'Você jogou {valor} e o computador jogou {pc}, o total é {valor+pc} deu {ipg}')
    print('---' * 10)
    if ip == ipc:
        print(f'Você ganhou! deu {ipg}')
        vitoria += 1
    else:
        print(f'Você perdeu! deu {ipg}, você venceu {vitoria} vezes seguidas')
        break
    print('Vamos jogar novamente...')
