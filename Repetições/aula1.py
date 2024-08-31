# Exemplo 1

contador = 1
while contador <= 3:
    print(contador)
    contador = contador + 1

# Exercício 1

contador = 1
while contador <= 100:
    print(contador)
    contador = contador + 1

# Exercício 2
print("Contagem regressiva de lançamento do foguete...")

contador = 10
while contador >= 0:
    print(contador)
    if contador == 0:
        print("Fogo!")
    contador = contador - 1
    

# Exercício 3
valor = int(input("Valor de entrada: "))
contador = 1
while contador <= valor:
    print(contador)
    contador = contador + 1

# Exercício 4
valor = int(input("Valor de entrada: "))
contador = 0
while contador <= valor:
    if contador % 2 == 0:
        print(contador)
    contador = contador + 1

# Exercício 5
valor = int(input("Valor de entrada: "))
contador = 1
while contador <= valor:
    if contador % 2 != 0:
        print(contador)
    contador = contador + 1

# Exercício 6
valor = int(input("Valor de entrada: "))
contador = 1
while contador <= 10:
    print(contador*valor)
    contador = contador + 1

# Exercício 7
valor = int(input("Valor de entrada: "))
inicio = int(input("Insira o multiplicador inicial: "))
final = int(input("Insira o multiplicador final: "))
while inicio <= final:
    print(inicio*valor)
    inicio = inicio + 1

# Exercício 8
valor = int(input("Insira o primeiro número: "))
valorDeRepeticao = int(input("Insira o segundo número: "))
contador = 1
resultado = valor
while contador <= valorDeRepeticao :
    if contador == valorDeRepeticao:
        print(resultado)
    resultado = resultado + valor
    contador = contador + 1
