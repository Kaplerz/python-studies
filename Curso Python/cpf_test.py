cpf = '123.456.789'

cpf_limpo = ''

for caractere in cpf:
    if caractere != '.':
        cpf_limpo += caractere

digitos = []

for numero in cpf_limpo:
    digitos.append(int(numero))


soma = 0

for indice in range(9):
    peso = 10 - indice
    soma += digitos[indice] * peso

resto = soma % 11

if resto < 2:
    primeiro_digito = 0
else:
    primeiro_digito = 11 - resto

digitos.append(primeiro_digito)


soma = 0

for indice in range(10):
    peso = 11 - indice
    soma += digitos[indice] * peso

resto = soma % 11

if resto < 2:
    segundo_digito = 0
else:
    segundo_digito = 11 - resto

digitos.append(segundo_digito)


cpf = ''

for numero in digitos:
    cpf += str(numero)


cpf_formatado = (
    cpf[:3] + '.' +
    cpf[3:6] + '.' +
    cpf[6:9] + '-' +
    cpf[9:]
)

print(cpf_formatado)