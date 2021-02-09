valor = 0
lista = []
while valor != 999:
    valor = int(input('Digite um valor: [999 para parar] '))
    if valor != 999:
        lista.append(valor)
tamanho = len(lista)
print('Foram digitados {} valores e a soma de todos eles é: {}'.format(tamanho, sum(lista)))