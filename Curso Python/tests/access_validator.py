nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
senha = input('Digite sua senha: ')

if nome and senha:
    if idade >= 18:
        if len(senha) >= 8 and '@' in senha:
            print('Acesso permitido.')
            print(f'Bem vindo {nome}!')
        else:
            print('Senha inválida.')
    else:
        print('Menor de idade.')
    
else:
    print('Dados inválidos.')
    