produtos = ['Mouse', 'Teclado', 'Monitor', 'Headset']
for produto in produtos:
    print(produto)
    
produtos = ['Mouse', 'Teclado', 'Monitor', 'Headset']
for indice, produto in enumerate(produtos, start=1):
    print(indice, produto)
    
    
produtos = ['Mouse', 'Teclado', 'Monitor', 'Headset']
for indice in range(len(produtos)):
    if produtos[indice] == 'Monitor':
        produtos[indice] = 'Monitor Gamer'
        print(produtos)


produtos = ['Mouse', 'Teclado', 'Monitor', 'Headset']

contador = 0
for produto in produtos:
    contador += 1
    print(produto)
print(contador)

produtos = ['Mouse', 'Teclado', 'Monitor', 'Headset']

for indice, produto in enumerate(produtos, start=1):
    print(f'O produto na posição {indice} é: {produto}')


produtos = ['Mouse', 'Teclado', 'Monitor', 'Headset']
pesquisa = int(input('Digite o número do produto: '))
indice_py = pesquisa -1
print(f'Produto escolhido: {produtos[indice_py]}')

