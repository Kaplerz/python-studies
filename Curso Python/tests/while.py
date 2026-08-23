# numero = 1

# while numero <= 50:
#     if numero % 3 == 0 and numero % 5 == 0:
#         print(f'O número {numero} é divisível por 3 e por 5.')
#     elif numero % 3 == 0:
#         print(f'O número {numero} é divisível por 3.')
#     elif numero % 5 == 0:
#         print(f'O número {numero} é divisível 5.')
#     else:
#         print(f'O número {numero} não é divisível nem por 3 nem por 5.')
        
#     numero = numero + 1 
    
autorizado = False 

while not autorizado:
    idade = int(input('Digite sua idade: '))
    
    if idade <=0:
        print('Idade inválida, tente novamente.')
        
    else:
        print(f'Idade válida: {idade}')
        
        autorizado = True
        
    
