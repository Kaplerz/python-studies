nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
email = input('Digite seu email: ')
senha = input('Digite sua senha: ')
confirmar_senha = input('Confirme sua senha: ')


if len(nome) < 3:
    print('Nome inválido, o nome precisa ter no mínimo 3 caracteres.')
    
elif idade < 18:
    print('Acesso negado, usuário menor de idade.')
    
elif '@' not in email or '.' not in email:
    print('Email inválido, o email precisa conter @ e ponto.')
    
elif ('@' not in senha and '#' not in senha) or len(senha) < 8:
    print('Senha inválida, a senha precisa conter no mínimo 8 caracteres, incluindo símbolos.')
    
elif senha != confirmar_senha:
    print('As senhas não coincidem')
    
else:
    print('Cadastro realizado com sucesso!')
    