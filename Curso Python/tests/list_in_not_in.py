produtos = [
    'Mouse'.lower(),
    'Teclado'.lower(),
    'Monitor'.lower(),
    'Headset'.lower(),
    'Webcam'.lower()
]
print('Mouse'.lower() in produtos)
print('Notebook'.lower() not in produtos)

produto = (input('Digite o produto: '))
produto = produto.lower()
if produto in produtos:
    print('Produto disponível.')
else:
    print('Produto indisponível.')
    