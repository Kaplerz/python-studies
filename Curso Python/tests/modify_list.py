lista = ['Mouse', 'Teclado', 'Monitor']
print(lista)
lista[1] = 'Headset'
print(lista)

lista.append('Webcam')
print(lista)
produto_removido = lista.pop()
print(lista)
print(f'Lista: {lista}, Produto removido: {produto_removido}')