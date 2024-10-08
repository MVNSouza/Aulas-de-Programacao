# $ Questão 1

totalTemperaturas = []
menorTemperatura = float
maiorTemperatura = 0

for i in range(10):
    temperatura = float(input(f"Insira a {i + 1}º temperatura (em ºC):  "))
    totalTemperaturas.append(temperatura)

maiorTemperatura = totalTemperaturas[0]
menorTemperatura = totalTemperaturas[0]

for temperatura in totalTemperaturas:
    if menorTemperatura > temperatura:
        menorTemperatura = temperatura


for temperatura in totalTemperaturas:
    if maiorTemperatura < temperatura:
        maiorTemperatura = temperatura

somaTotalTemperaturas = 0
for temperatura in totalTemperaturas:
    somaTotalTemperaturas += temperatura

mediaTemperaturas = somaTotalTemperaturas / len(totalTemperaturas)

print()
print(f"Menor temperatura registrada: {menorTemperatura}ºC")
print(f"Maior temperatura registrada: {maiorTemperatura}ºC")
print(f"Média das temperaturas registradas: {mediaTemperaturas:.1f}ºC")

# $ Questão 2

numeros = []
for i in range(10):
    numero = int(input(f"Insira o {i+1}º número: "))
    numeros.append(numero)

numerosImpares = []
for numero in numeros:
    if (numero % 2) == 1:
        numerosImpares.append(numero)

totalNumerosImpares = len(numerosImpares)
totalNumerosPares = len(numeros) - totalNumerosImpares
porcentagemNumerosImpares = (totalNumerosImpares / len(numeros)) * 100 <<<<<<<<<<<<<<<<<<<<<<<<<

print(f"Total números pares: {totalNumerosPares}")
print(f"Total números ímpares: {totalNumerosImpares}")
print(f"Porcentagem de números ímpares: {porcentagemNumerosImpares}%")

# $ Questão 3

vetorA = []
for i in range(10):
    itemA = float(input(f"Insira o {i+1}º valor: "))
    vetorA.append(itemA)

vetorB = []
acessadorDeIndice = 9
while acessadorDeIndice >= 0:
    vetorB.append(vetorA[acessadorDeIndice])
    acessadorDeIndice -= 1 

print(f"Vetor A = {vetorA}")
print(f"Vetor B = {vetorB}")


# $ Questão 4

vetorA = []
vetorB = []

for i in range(10):
    num = int(input(f"Insira o {i+1}º número: "))
    vetorA.append(num)

indice = 0
while indice < len(vetorA):
    contador = vetorA[indice]
    numero = 0
    while contador >= 1:
        numero += contador
        contador -= 1
    vetorB.append(numero)

    indice += 1

print(vetorA)
print(vetorB)

# $ Questão 5

vetorA = []
vetorB = []
vetorC = []

# Vetor A

    
contador = 1
while True:
    numeroPar = int(input(f"Insira o {contador}º número par: "))
    if (numeroPar % 2) != 0:
        print("Insira um número par")
    else:
        vetorA.append(numeroPar)
        contador += 1       
        if contador == 6:
            break
        

# Vetor B
contador = 1
while True:
    numeroImpar = int(input(f"Insira o {contador}º número ímpar: "))
    if (numeroImpar % 2) != 0:
        vetorB.append(numeroImpar)
        contador += 1
        if contador == 6:
            break
    else:
        print("Insira um número ímpar")

# Vetor C
vetorC = vetorA + vetorB

# Saída

print(f"Vetor A (Pares): {vetorA}")
print(f"Vetor B (Ímpares: {vetorB}")
print(f"Vetor C (Vetor A & B): {vetorC}")