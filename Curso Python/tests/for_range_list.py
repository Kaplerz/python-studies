produtos = [
        'Mouse',
        'Teclado',
        'Monitor',
        'Headset',
        'Webcam'    
    ]

for indice in range(len(produtos)):
    if produtos[indice] == 'Monitor':
        produtos[indice] = 'Monitor Gamer'
    if indice % 2 == 0:
        print(f'O índice {indice} de {produtos[indice]} é par.')
    else:
        print(f'O índice {indice} de {produtos[indice]} é ímpar.')
print(produtos)
