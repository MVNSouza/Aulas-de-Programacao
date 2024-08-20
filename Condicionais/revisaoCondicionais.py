# # Exercicio 1

# a = float(input("Insira um número: ")) 
# b = float(input("Insira um número: ")) 
# produto = a+b

# if produto > 10:
#     print(produto)
# print("-"*30)
# print()
# # Exercicio 2

# a = float(input("Insira um número: ")) 
# b = float(input("Insira um número: ")) 
# produto = a+b

# if produto > 10:
#     print(produto+5)

# else:
#     print(produto-7)
# print("-"*30)
# print()
# # Exercicio 3

# valor = int(input("Digite um valor numérico inteiro: "))

# if valor == 1:
#     print("Você entrou com o valor 1")
# elif valor == 2:
#     print("Você entrou com o valor 2")
# elif valor < 1:
#     print("Você entrou com um valor muito baixo")
# else:
#     print("Você entrou com um valor muito alto")

# print("-"*30)
# print()
# # Exercicio 4

# salario = float(input("Digite o salário do colaborador: R$ "))
# if salario < 500:
#     aumento = 0.15
# elif salario <= 1000:
#     aumento = 0.10
# else:
#     aumento = 0.05

# novo_salario = salario * (1 + aumento)

# print(f"Percentual de aumento: {aumento * 100:.0f}%")
# print(f"Novo salário: R$ {novo_salario:.2f}")
# print("-"*30)
# print()
# # Exercicio 5

# numeroMes = int(input("Digite o número do mês: "))

# if numeroMes == 1:
#     print(f"O {numeroMes}º mês é janeiro!")

# elif numeroMes ==  2 :
#     print(f"O {numeroMes}º mês é fevereiro!")

# elif numeroMes ==  3 :
#     print(f"O {numeroMes}º mês é março!")

# elif numeroMes ==  4 :
#     print(f"O {numeroMes}º mês é abril!")

# elif numeroMes ==  5 :
#     print(f"O {numeroMes}º mês é maio!")

# elif numeroMes ==  6 :
#     print(f"O {numeroMes}º mês é junho!")

# elif numeroMes ==  7 :
#     print(f"O {numeroMes}º mês é julho!")

# elif numeroMes ==  8 :
#     print(f"O {numeroMes}º mês é agosto!")

# elif numeroMes ==  9 :
#     print(f"O {numeroMes}º mês é setembro!")

# elif numeroMes ==  10 :
#     print(f"O {numeroMes}º mês é outubro!")

# elif numeroMes ==  11 :
#     print(f"O {numeroMes}º mês é novembro!")

# elif numeroMes ==  12 :
#     print(f"O {numeroMes}º mês é dezembro!")

# else:
#     print("Valor inválido")
# print("-"*30)
# print()

# # Exercicio 06

# numero = int(input("Digite um número: "))

# if numero >= 20 and numero <= 90:
#     print("Número permitido")

# else:
#     if numero < 20:
#         print("Número é menor que o permitido")
#     else:
#         print("Número é maior que o permitido")
# print("-"*30)
# print()

# Exercicio 07

sexo = input("INSIRA O SEU SEXO: ([M] para Masculino & [F] para Feminino)")

if sexo == "M" or sexo == "m":
    sexo = "Masculino"
    print(f"Sexo válido \n")