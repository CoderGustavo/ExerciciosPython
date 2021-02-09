valores = list()
for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {v}:')))
maior = max(valores)
menor = min(valores)
for i, v in enumerate(valores):
    if maior == v:
        posimaior = i
    if menor == v:
        posimenor = i

print(f'Na posição {posimaior} foi digitado {maior} o maior número')
print(f'Na posição {posimenor} foi digitado {menor} o menor número')