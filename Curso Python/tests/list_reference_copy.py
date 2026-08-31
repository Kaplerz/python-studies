lista_a = ['Mouse', 'Teclado']
lista_b = lista_a
lista_a.append('Webcam')
print(f'Lista A: {lista_a}, Lista B: {lista_b}')
print(lista_a is lista_b) # é apenas uma lista, pois não foi criado uma cópia referenciada usando copy(), ou seja, o boolean retornará True, pois são iguais

lista_a1 = ['Fone', 'Console']
lista_b1 = lista_a1.copy()
lista_a1.append('Webcam')
print(f'Lista A1: {lista_a1}, Lista B1: {lista_b1}') # as duas listas são iguais, porém separadas, ou seja, o valor adicionado com append em uma, não afetará a outra, e o boolean retornará False, pois não são iguais.
print(lista_a1 is lista_b1)