quant_dez = quant_m = quant_f_vinte = 0
sexo = 'A'
c = 'A'
while True:
    print('-' * 10)
    print('CADASTRAR UMA PESSOA')
    print('-' * 10)
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: M/F')).strip().upper()[0]
    while c not in 'SN':
        c = str(input('Você deseja continuar? ')).strip().upper()[0]
    if idade > 18:
        quant_dez += 1
    if sexo == 'M':
        quant_m += 1
    if sexo == 'F':
        if idade < 20:
            quant_f_vinte += 1
    if c == 'N':
        break
    sexo = 'A'
    c = 'A'
print('FIM DO PROGRAMA')
print('')
print(f"""
Possui {quant_dez} pessoas com mais de 18 anos!
Possui {quant_m} homens cadastrados!
Possui {quant_f_vinte} mulheres com menos de 20 anos""")