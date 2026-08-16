valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))

if valor1 > valor2:
    print(f'Valor {valor1} é maior que Valor {valor2}')
elif valor1 < valor2:
    print(f'Valor {valor1} é menor que valor {valor2}')
else:
    print('Comparação inválida.')