# Resolução da questão 2


numeros = []  # vetor para armazenar os números

# solicita que o usuário insira 5 números e os adicione ao vetor
for i in range(5):
    num = int(input("Digite um número: "))
    numeros.append(num)

# encontra o menor e o maior número do vetor
maior = max(numeros)
menor = min(numeros)

# imprime o menor e o maior número
print("O número maior é:", maior)
print("O número menor é:", menor)


vetor = []
for i in range(5):
    num = int(input("Digite o número: "))
    vetor.append(num)
print("O valor na posição três é: ", vetor[2])
