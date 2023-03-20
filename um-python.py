#Questão 1 do desafio em python:

#lista de onde vão estar os cinco números informados pelo usuário
numeros = []


#um laço de repetição de 5x para serem informados os números.
for i in range(5):
    numero = int(input("Digite um número: ")) #int por ser um número inteiro e dentro do parentese um input que é o comando p q o usuário faça a inserção
    numeros.append(numero) #append para adicionar itens a lista pré existente, no caso a numeros


#novas listas que vão separar a lista principal dos numeros em pares e ímpares
pares = []
impares = []


#um laço que vai rodar os itens da lista numeros

for numero in numeros:
    if numero % 2 == 0: #verificação para saber se o número da vez é par
        pares.append(numero)
    else:
        impares.append(numero)


media = sum(numeros) / len(numeros) #soma dos números totais dividido pela quantidade de números informados.

print("Números pares: ", pares)
print("Números ímpares: ", impares)
print("Média geral: ", media)