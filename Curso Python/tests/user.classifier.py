nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
profissao = input('Digite sua profissão: ')

if nome and idade and profissao:
    if 'Developer' in profissao:
        print('Área de T.I detectada.')
    else:
        print('Área de T.I não identificada.')
            
    if idade >= 60:
        print('O usuário é idoso.')
    elif idade >= 18:
        print('O usuário é adulto.')
    else:
        print('Usuário menor de idade.')
else:
    print('Dados inválidos.')
