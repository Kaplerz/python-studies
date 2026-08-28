numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
soma_par = 0

for numero in range(numero1, numero2 + 1):
    if numero % 2 == 0:
        print(f'O {numero} é par.')
        soma_par += numero
    else:
        print(f'O {numero} é ímpar. ')
        
print(f'A soma dos pares é: {soma_par}')    