palavra_secreta = 'python'
letras_acertadas = ''

while True:

    letra = input('Digite uma letra: ')

    if len(letra) != 1:
        print('Digite apenas uma letra.')
        continue

    if letra in palavra_secreta:
        letras_acertadas += letra

    else:
        print(f'A letra {letra} não existe na palavra.')

    palavra_formada = ''

    for letra_secreta in palavra_secreta:

        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta

        else:
            palavra_formada += '*'

    print(f'Palavra: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        print('Parabéns! Você descobriu a palavra!')
        break