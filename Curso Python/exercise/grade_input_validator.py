# Exercício 1: Validador de Entrada e Processador de Notas
# Objetivo: Praticar while, try/except, tratamento de exceções e manipulação de listas.

# Enunciado: Crie um programa que permita cadastrar notas de alunos (de 0 a 10).

# O programa deve pedir a nota no terminal dentro de um laço contínuo.

# Se o usuário digitar um valor que não seja número ou um valor fora do intervalo de 0 a 10, exiba uma mensagem de erro com try/except e peça a entrada novamente.

# O laço encerra quando o usuário digitar 'fim'.

# Ao final, exiba:

# A quantidade total de notas válidas inseridas.

# A média das notas (com duas casas decimais).

# A maior e a menor nota digitada.

# Caso nenhuma nota válida tenha sido inserida, exiba um aviso.





notas = []

while True:
    entrada = input('Digite suas notas, para sair, digite "sair". : ').lower()
    if entrada == 'sair':
        print('Você saiu.')
        break
    try:
        nota_int = int(entrada)   
        if nota_int < 0 or nota_int > 10:
            print('A nota precisa ser entre 0 e 10.')
            continue
        notas.append(nota_int)
    except ValueError:
        print('Você precisa digitar um número.')
        continue
if notas == []:
    print('Você precisa digitar uma nota.')
else:
    quantidade = len(notas)
    soma = 0
   
    total_notas = quantidade
    for nota in notas:
        soma += nota
    media = soma / quantidade
    maior_nota = max(notas)
    menor_nota = min(notas)
    print(f'Seu total de notas é: {total_notas}')
    print(f'Sua média é: {media:.2f}')
    print(f'A sua maior nota é: {maior_nota:.2f}')
    print(f'A sua menor nota é: {menor_nota:.2f}')
    


