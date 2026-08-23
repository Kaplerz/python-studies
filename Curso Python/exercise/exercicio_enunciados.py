"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# try:
#     numero = int(input('Digite um número: '))

#     if numero % 2 == 0:
#         print('O número é par.')
#     else:
#         print('O número é ímpar.')

#     print('O número é inteiro.')

# except:
#     print('O número não é inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# horario = float(input('Digite o horário (ex: 12.32): '))

# if horario >= 0 and horario <= 11.59:
#     print('Bom dia!')
    
# elif horario >= 12.00 and horario <= 17.59:
#     print('Boa tarde!')

# elif horario >= 18.00 and horario <= 23.59:
#     print('Boa noite!')



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('Seu nome é muito curto.')
    
elif len(nome) >= 5 and len(nome) <=6:
    print('Seu nome é normal.')
    
else:
    print('Seu nome é muito grande.')