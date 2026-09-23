lista_de_listas_de_inteiros = [

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],

]


def encontrar_duplicado(lista):
    # Cria uma função que recebe uma lista de números
    # e procura o primeiro número que aparece novamente.


    vistos = set()
    # Cria um conjunto vazio.
    # Ele será usado para guardar os números que já encontramos.
    # Diferente de uma lista, um set não permite valores duplicados.


    for numero in lista:
        # Percorre cada número da lista, um por um.


        if numero in vistos:
            # Verifica se o número atual já está dentro do set.
            # Se estiver, significa que esse número já apareceu antes.
            # Portanto, encontramos o primeiro duplicado.


            return numero
            # Retorna o número duplicado e encerra a função.


        else:
            # Se o número ainda não estiver no set...


            vistos.add(numero)
            # Adiciona o número ao conjunto de números já vistos.


    return -1
    # Se terminar de percorrer a lista sem encontrar duplicados,
    # retorna -1.


for lista in lista_de_listas_de_inteiros:
    # Percorre cada lista que está dentro da lista principal.


    resultado = encontrar_duplicado(lista)
    # Envia a lista atual para a função.
    # A função procura o primeiro duplicado e retorna o resultado.


    print(resultado)
    # Exibe o resultado encontrado para aquela lista.


# def encontrar_duplicado(lista):
#     vistos = set()

#     for numero in lista:
#         if numero in vistos:
#             return numero
#         else:
#             vistos.add(numero)

#     return -1


# for lista in lista_de_listas_de_inteiros:
#     resultado = encontrar_duplicado(lista)
#     print(resultado)