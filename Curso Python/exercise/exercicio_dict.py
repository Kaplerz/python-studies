perguntas = [

    {
        "Pergunta": "Quanto é 2+2?",
        "Opções": ["1", "3", "4", "5"],
        "Resposta": "4",
    },

    {
        "Pergunta": "Quanto é 5*5?",
        "Opções": ["25", "55", "10", "51"],
        "Resposta": "25",
    },

    {
        "Pergunta": "Quanto é 10/2?",
        "Opções": ["4", "5", "2", "1"],
        "Resposta": "5",
    },

]

acertos = 0

for pergunta in perguntas:

    print(pergunta["Pergunta"])

    for numero, opcao in enumerate(pergunta["Opções"], start=1):
        print(numero, opcao)

    while True:
        resposta_usuario = input("Escolha uma opção: ")

        try:
            resposta_usuario = int(resposta_usuario)

        except ValueError:
            print("A opção precisa ser um número, SEU ANIMAL.")
            continue

        if resposta_usuario <= 0 or resposta_usuario > len(pergunta["Opções"]):
            print("Opção inválida.")
            continue

        break

    opcao_escolhida = pergunta["Opções"][resposta_usuario - 1]

    if opcao_escolhida == pergunta["Resposta"]:
        print("Você acertou!")
        acertos += 1
    else:
        print("Resposta errada.")

print(f"Você acertou {acertos} vezes!")