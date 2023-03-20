# Criando a matriz
matriz_notas = []
for i in range(3):
    nome = input("Digite o nome do aluno: ")
    notas = []
    for j in range(4):
        nota = float(input(f"Digite a nota {j+1} de {nome}: "))
        notas.append(nota)
    matriz_notas.append([nome, notas])

# Calculando a média geral de cada aluno e identificando o aluno com maior e menor média
maior_media = -1
menor_media = 11
aluno_maior_media = ''
aluno_menor_media = ''

for linha in matriz_notas:
    nome = linha[0]
    notas = linha[1]
    media = sum(notas) / len(notas)
    if media > maior_media:
        maior_media = media
        aluno_maior_media = nome
    if media < menor_media:
        menor_media = media
        aluno_menor_media = nome
    print(f"{nome}: média {media}")

# Imprimindo o aluno com maior e menor média
print(f"Aluno com maior média: {aluno_maior_media}")
print(f"Aluno com menor média: {aluno_menor_media}")