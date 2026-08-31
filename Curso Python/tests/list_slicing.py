produtos = [
    'Mouse',
    'Teclado',
    'Headset',
    'Webcam',
    'Microfone',
    ]
print(produtos[:3])
print(produtos[-1:-4:-1])
print(produtos[1:4])

produtos_copia = produtos[:]
produtos_copia.append('Ipad')

print(f'Produtos A: {produtos}, Produtos Atualizados: {produtos_copia}')
print(produtos is produtos_copia)