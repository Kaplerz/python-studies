nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if nome and idade:
    if len(nome) >= 3:

        print(f'Seu nome é: {nome}, e sua idade é: {idade}')
        print(f'Seu nome invertido: {nome[::-1]}')
        print(f'Seu nome tem {len(nome)} letras.')
        print(f'A primeira letra do seu nome é: {nome[0]}')
        print(f'A última letra do seu nome é: {nome[-1]}')
        if ' ' in nome:
            print('Seu nome contém espaço.')
        else:
            print('Seu nome não contém espaço.')
    else:
        print('O nome precisa ter no mínimo 3 caracteres.')
   
else:
    print('Dados inválidos.')