quant_val = soma = 0
while True:
    valor = int(input('Digite um numero: [999 para parar]'))
    if valor == 999:
        break
    quant_val +=1
    soma +=valor
print(f'Foi digitados {quant_val} e a soma desses valores é: {soma}')