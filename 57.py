sexo = str(input('Digite o sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    print('Foi digitado um valor invalido!')
    sexo = str(input('Digite o sexo: [M/F]')).strip().upper()
if(sexo == 'M'):
    print('Sexo: Masculino')
else:
    print('Sexo: Feminino')