produtos = [
    'Mouse',
    'Teclado',
    'Monitor',
    'Headset',
    'Webcam'
]

contador = 0
for produto in produtos:
    contador += 1
    print(produto)
    if produto == 'Monitor':
        print('Monitor encontrado!')
print(contador)
        
    