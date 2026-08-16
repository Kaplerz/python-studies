# ============================================================
# PYTHON - ANOTAÇÕES E EXERCÍCIOS DE ESTUDO
# ============================================================
#
# Este arquivo contém exercícios estudados até agora.
#
# Principais assuntos:
# - Variáveis
# - Tipos de dados
# - Conversão de tipos
# - Operadores matemáticos
# - input()
# - if, elif e else
# - Operador módulo %
# - Formatação com .format()
# - Formatação com f-strings
#
# ============================================================


# ============================================================
# 1. VARIÁVEIS E TIPOS DE DADOS
# ============================================================

# Uma variável serve para guardar um valor na memória.

# idade = 22
# Aqui, 22 é um número inteiro.
# O tipo desse valor é int.

# idade = 22

# numero = "22"
# Aqui, "22" é um texto, mesmo contendo números.
# O tipo desse valor é str (string).

# numero = "22"


# ============================================================
# 2. OPERAÇÕES COM INT E STR
# ============================================================

# idade = 22
# numero = "22"

# Podemos somar números inteiros:

# print(idade + 5)

# Resultado:
# 27


# Com strings, o operador + junta textos.
# Isso é chamado de concatenação.

# print(numero + "5")

# Resultado:
# 225


# ============================================================
# 3. CONVERSÃO DE TIPOS - int()
# ============================================================

# numero = "10"
#
# Inicialmente, "10" é uma string.
#
# Usamos int() para converter a string em número inteiro.

# numero = int(numero)

# Agora podemos fazer operações matemáticas:

# print(numero + 5)

# Resultado:
# 15


# Outro exemplo:

# valor = "100"

# int() transforma a string "100" no inteiro 100.

# valor_inteiro = int(valor)

# print(valor_inteiro)

# type() mostra qual é o tipo do valor.

# print(type(valor_inteiro))

# Resultado:
# <class 'int'>


# ============================================================
# 4. CONVERSÃO PARA STRING - str()
# ============================================================

# numero = 50

# str() transforma um número em texto.

# texto = str(numero)

# print(texto)

# Agora podemos verificar o tipo:

# print(type(texto))

# Resultado:
# <class 'str'>


# ============================================================
# 5. OPERAÇÕES MATEMÁTICAS BÁSICAS
# ============================================================

# numero1 = 10
# numero2 = 5

# Soma:
# resultado = numero1 + numero2

# print(resultado)

# Resultado:
# 15


# Também podemos guardar cada operação em uma variável.

# soma = numero1 + numero2
# subtracao = numero1 - numero2
# multiplicacao = numero1 * numero2
# divisao = numero1 / numero2

# print("Soma:", soma)
# print("Subtração:", subtracao)
# print("Multiplicação:", multiplicacao)
# print("Divisão:", divisao)

# Resultado:
#
# Soma: 15
# Subtração: 5
# Multiplicação: 50
# Divisão: 2.0


# ============================================================
# 6. MULTIPLICAÇÃO DE PREÇO E QUANTIDADE
# ============================================================

# produto = "Mouse"
# preco = 80
# quantidade = 3

# Multiplicamos o preço pela quantidade.

# total = preco * quantidade

# print("Preço total:", total)

# Resultado:
# 240


# Podemos imprimir todas as informações:

# print("Produto:", produto)
# print("Preço unitário:", preco)
# print("Quantidade:", quantidade)
# print("Preço total:", total)


# Outro exemplo:

# produto = "Teclado"
# preco = 150
# quantidade = 2

# total = preco * quantidade

# print("Produto:", produto)
# print("Preço unitário:", preco)
# print("Quantidade:", quantidade)
# print("Preço total:", total)


# ============================================================
# 7. OPERADORES MATEMÁTICOS
# ============================================================

# numero1 = 20
# numero2 = 4

# + = soma
# - = subtração
# * = multiplicação
# / = divisão normal
# // = divisão inteira

# soma = numero1 + numero2
# subtracao = numero1 - numero2
# multiplicacao = numero1 * numero2

# A divisão inteira remove a parte decimal.

# divisao = numero1 // numero2

# print("Soma:", soma)
# print("Subtração:", subtracao)
# print("Multiplicação:", multiplicacao)
# print("Divisão inteira:", divisao)


# ============================================================
# 8. CONVERSÃO DE CELSIUS PARA FAHRENHEIT
# ============================================================

# Fórmula:
#
# Fahrenheit = Celsius * 9 / 5 + 32

# celsius = 30

# fahrenheit = celsius * 9 / 5 + 32

# print("Celsius:", celsius)
# print("Fahrenheit:", fahrenheit)


# ============================================================
# 9. input() E ENTRADA DE DADOS
# ============================================================

# input() permite que o usuário digite uma informação.
#
# IMPORTANTE:
# Tudo que vem do input() inicialmente é uma string.

# nome = input("Digite seu nome: ")

# Como idade precisa ser usada em cálculos,
# usamos int() para converter o valor digitado.

# idade = int(input("Digite sua idade: "))

# Para números decimais usamos float().

# altura = float(input("Digite sua altura: "))

# print("Olá,", nome)
# print(type(nome))

# print(idade)
# print(type(idade))

# print(altura)
# print(type(altura))


# ============================================================
# 10. CÁLCULO DO ANO DE NASCIMENTO
# ============================================================

# Subtraímos a idade do ano atual.

# ano_nascimento = 2026 - idade

# print("Você nasceu aproximadamente em:", ano_nascimento)


# ============================================================
# 11. PREÇO TOTAL COM DESCONTO FIXO
# ============================================================

# produto = "Mouse"

# preco = int(input("Digite o preço: "))
# desconto = int(input("Digite o desconto: "))
# quantidade = int(input("Digite a quantidade: "))

# Calculamos o preço total sem desconto.

# total_sem_desconto = quantidade * preco

# Neste exemplo, o desconto é aplicado em cada unidade.

# total_com_desconto = (preco - desconto) * quantidade

# print("Produto:", produto)
# print("Quantidade:", quantidade)
# print("Valor total sem desconto:", total_sem_desconto)
# print("Valor total com desconto:", total_com_desconto)


# ============================================================
# 12. MÉDIA DE TRÊS NOTAS
# ============================================================

# nota1 = float(input("Digite sua primeira nota: "))
# nota2 = float(input("Digite sua segunda nota: "))
# nota3 = float(input("Digite sua terceira nota: "))

# Os parênteses são importantes.
#
# Primeiro somamos todas as notas.
# Depois dividimos o resultado por 3.

# media = (nota1 + nota2 + nota3) / 3

# print("Média das notas:", media)


# ============================================================
# 13. CONVERSÃO DE REAL PARA DÓLAR
# ============================================================

# real = float(input("Digite o valor em reais: "))

# A cotação foi definida manualmente neste exemplo.

# cotacao = 5.12

# Para descobrir quantos dólares o valor representa,
# dividimos reais pela cotação.

# dolar = real / cotacao

# print("Valor em dólares:", dolar)


# ============================================================
# 14. DESCONTO EM PORCENTAGEM
# ============================================================

# produto = input("Digite o produto: ")

# Usamos float porque um preço pode ter centavos.

# preco = float(input("Digite o preço: "))

# quantidade = int(input("Digite a quantidade: "))

# desconto = int(input("Digite o desconto em porcentagem: "))

# Calculamos o valor total.

# total = quantidade * preco

# Transformamos a porcentagem em valor.

# Exemplo:
# 10% de 100 = 10
#
# Fórmula:
# total * desconto / 100

# valor_do_desconto = total * desconto / 100

# Subtraímos o desconto do total.

# total_final = total - valor_do_desconto

# print("Produto:", produto)
# print("Preço:", preco)
# print("Quantidade:", quantidade)
# print("Percentual de desconto:", desconto)
# print("Desconto total:", valor_do_desconto)
# print("Total sem desconto:", total)
# print("Total com desconto:", total_final)


# ============================================================
# 15. MÉDIA DE DUAS NOTAS
# ============================================================

# nome = input("Digite seu nome: ")

# nota1 = float(input("Digite sua primeira nota: "))
# nota2 = float(input("Digite sua segunda nota: "))

# media = (nota1 + nota2) / 2

# print("Seu nome:", nome)
# print("Sua média:", media)


# ============================================================
# 16. CONDIÇÕES - if, elif e else
# ============================================================

# if significa:
# "Se esta condição for verdadeira, faça isso."

# elif significa:
# "Se a condição anterior não foi verdadeira,
# verifique esta outra condição."

# else significa:
# "Se nenhuma condição anterior foi verdadeira,
# faça isso."

# if media >= 9:
#     print("Excelente.")

# elif media >= 7:
#     print("Aprovado.")

# else:
#     print("Reprovado.")


# ============================================================
# 17. CALCULADORA SIMPLES
# ============================================================

# numero1 = float(input("Digite um número: "))
# calculo = input("Tipo de cálculo: ")
# numero2 = float(input("Digite outro número: "))

# O programa verifica qual operação foi escolhida.

# if calculo == "+":
#     print(numero1 + numero2)

# elif calculo == "-":
#     print(numero1 - numero2)

# elif calculo == "*":
#     print(numero1 * numero2)

# elif calculo == "/":

#     # Antes de dividir, verificamos se o divisor é zero.
#     # Divisão por zero gera um erro no Python.

#     if numero2 == 0:
#         print("Não é possível dividir por 0.")

#     else:
#         print(numero1 / numero2)

# else:
#     print("Operação inválida.")


# ============================================================
# 18. OPERADOR MÓDULO %
# ============================================================

# O operador % retorna o RESTO da divisão.

# Exemplo:
#
# 10 % 2 = 0
#
# Isso significa que 10 é divisível por 2.


# ============================================================
# 19. VERIFICANDO SE UM NÚMERO É PAR OU ÍMPAR
# ============================================================

# numero = int(input("Digite um número: "))

# Se o resto da divisão por 2 for 0,
# o número é par.

# if numero % 2 == 0:
#     print("O número é par.")

# else:
#     print("O número é ímpar.")


# ============================================================
# 20. VERIFICANDO SE UM NÚMERO É DIVISÍVEL POR 5
# ============================================================

# numero = int(input("Digite um número: "))

# Se o resto da divisão por 5 for 0,
# significa que ele é divisível por 5.

# if numero % 5 == 0:
#     print("É divisível por 5.")

# else:
#     print("Não é divisível por 5.")


# ============================================================
# 21. NÚMERO POSITIVO, NEGATIVO OU ZERO
# ============================================================

# numero = int(input("Digite um número: "))

# if numero > 0:
#     print("O número é positivo.")

# elif numero < 0:
#     print("O número é negativo.")

# else:
#     print("O número é zero.")


# Também podemos verificar se ele é par ou ímpar:

# if numero % 2 == 0:
#     print("O número é par.")

# else:
#     print("O número é ímpar.")


# ============================================================
# 22. FORMATAÇÃO DE STRINGS COM .format()
# ============================================================

# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))

# Os {} funcionam como espaços reservados.
#
# .format() coloca os valores dentro deles.

# print("Olá {}, você tem {} anos.".format(nome, idade))


# ============================================================
# 23. FORMATAÇÃO DE STRINGS COM f-strings
# ============================================================

# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))

# O f antes das aspas permite colocar variáveis
# diretamente dentro de {}.

# print(f"Olá {nome}! Você tem {idade} anos.")


# ============================================================
# 24. f-strings COM OPERAÇÕES MATEMÁTICAS
# ============================================================

# numero1 = int(input("Digite um número: "))
# numero2 = int(input("Digite outro número: "))

# soma = numero1 + numero2

# print(f"A soma de {numero1} + {numero2} é igual a {soma}")


# ============================================================
# 25. CALCULADORA FINAL
# ============================================================
#
# Projeto que reúne vários conceitos estudados:
#
# - input()
# - float()
# - variáveis
# - operadores matemáticos
# - if
# - elif
# - else
# - comparação ==
# - prevenção de divisão por zero
# - f-strings
#
# ============================================================


numero1 = float(input("Digite um número: "))

calculo = input("Digite o tipo de cálculo (+, -, / ou *): ")

numero2 = float(input("Digite outro número: "))


# Se o usuário escolher +, fazemos uma soma.

if calculo == "+":
    print(
        f"O resultado da soma de {numero1} + {numero2} "
        f"é: {numero1 + numero2}"
    )


# Se escolher -, fazemos uma subtração.

elif calculo == "-":
    print(
        f"O resultado da subtração de {numero1} - {numero2} "
        f"é: {numero1 - numero2}"
    )


# Se escolher /, verificamos primeiro se numero2 é 0.

elif calculo == "/":

    # numero2 é o divisor.
    # Não é possível dividir um número por zero.

    if numero2 == 0:
        print("Não é possível dividir por 0.")

    else:
        print(
            f"O resultado da divisão de {numero1} / {numero2} "
            f"é: {numero1 / numero2}"
        )


# Se escolher *, fazemos uma multiplicação.

elif calculo == "*":
    print(
        f"O resultado da multiplicação de {numero1} * {numero2} "
        f"é: {numero1 * numero2}"
    )


# Se o usuário digitar qualquer outro símbolo,
# nenhuma condição acima será verdadeira.

else:
    print("Tipo de cálculo inválido.")