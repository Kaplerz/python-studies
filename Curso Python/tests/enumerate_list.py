produtos = [
    'Mouse',
    'Teclado',
    'Monitor',
    'Headset',
    'Webcam'
]

for indice, produto in enumerate(produtos, start=1):
    if produto == 'Monitor':
        print(f'Monitor encontrado na posição: {indice}')
    print(indice, produto)