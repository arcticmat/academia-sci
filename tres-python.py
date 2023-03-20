#Resolução questão 3


while True:
    nome = input("Digite o nome do aluno: ")
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a {i+1}ª nota: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    print(f"{nome} teve média {media:.2f}.")
    if media >= 6:
        print("Aprovado!")
    else:
        print("Reprovado!")
    opcao = input("Deseja encerrar o programa? (s/n) ")
    if opcao.lower() == "s":
        break