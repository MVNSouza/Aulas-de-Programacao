# Exercicios Aula 11

# Exercicio 1
idadeCarro = int(input("Digite a idade do seu carro em anos: "))

if idadeCarro <= 3:
    print("Seu carro é novo")

if idadeCarro > 3:
    print("Seu carro é velho")

print("")
# Desafio 1

velocidadeDoCarro = int(input("Insira a velocidade do seu carro em Km/h: "))
valorDaMulta = int 
print()
if velocidadeDoCarro <= 80:
    print(f"Você está a {velocidadeDoCarro} Km/h, continue assim!")

if velocidadeDoCarro > 80:
    valorDaMulta = (velocidadeDoCarro - 80) * 5
    print(f"UIU UIU UIU UIU! \nVOCÊ ESTÁ MULTADO EM R${valorDaMulta}.00\nVai devagar garotão")

print("")
# Desafio 2

salarioAtual = float(input("Insira o seu salário atual: "))
valorDoAumento = float

if salarioAtual > 1250:
    valorDoAumento = salarioAtual * 0.1
    print(f"O valor do seu aumento será R$ {valorDoAumento}!")

if salarioAtual <= 1250:
    valorDoAumento = salarioAtual * 0.15
    print(f"O valor do seu aumento será R$ {valorDoAumento}!") 

print("")
# Desafio 3

distanciaDesejada = int(input("Insira a distância de viagem desejada (em Km): "))
valorDaViagem = float

if distanciaDesejada <= 200:
    valorDaViagem = distanciaDesejada * 0.50
    print(f"O custo da viagem fica por R$ {valorDaViagem}")

else:
    valorDaViagem = distanciaDesejada * 0.45
    print(f"O custo da viagem fica por R$ {valorDaViagem}")

print("")
# Exemplo 2

operacao = int(input("QUAL OPERAÇÃO VOCÊ QUER EFETUAR?\n\n1- Soma\n2- Subtração\n3- Divisão\n4- Multiplicação\n\nInsira a opção: "))
if operacao < 1 or operacao > 4:
    print("Operação inválida. Digite um número de 1 a 4")
    quit()

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if operacao == 1:  # soma
    resultado = a + b
    print(f"O resultado da soma é {resultado}")

elif operacao == 2: # subtracao
    resultado = a - b
    print(f"O resultado da subtração é {resultado}")

elif operacao == 3: # divisao
    resultado = a/b
    print(f"O resultado da divisão é {resultado}")

elif operacao == 4: # multiplicacao
    resultado = a*b
    print(f"O resultado da multiplicação é {resultado}")