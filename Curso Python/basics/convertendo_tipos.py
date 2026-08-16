nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2

print("Seu nome: ", nome)
print("Sua média: ", media)

if media >= 9:
    print("Excelente.")

elif media >= 7:
    print("Aprovado.")

else:
    print("Reprovado.")
      
print(type(nome))
print(type(nota1))
print(type(nota2))
print(type(media))
