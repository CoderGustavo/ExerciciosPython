extenso = ('zero','um', 'dois', 'treis', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
numero = int(input('Digite um numero entre 0 e 20: '))
while numero >20:
    numero = int(input('numero incorreto! Digite um numero entre 0 e 20: '))
while numero <0:
    numero = int(input('numero incorreto! Digite um numero entre 0 e 20: '))
print(f'O numero digitado foi {extenso[numero]}')