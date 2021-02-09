from random import randint
val1 = randint(0, 10)
val2 = randint(0, 10)
val3 = randint(0, 10)
val4 = randint(0, 10)
val5 = randint(0, 10)
maior = 0
valores = (val1,val2,val3,val4,val5)
for n in valores:
    print(n, end=' ')

print(f'\nO maior valor aletório foi {max(valores)}')
print(f'O menor valor aleatório foi {min(valores)}')