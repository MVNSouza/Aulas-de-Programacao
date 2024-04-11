# EXERCICIO 06
# Escreva uma expressão que determina se uma pessoa deve ou não pagar imposto. Considere imposto para quem recebe mais de R$ 1.200,00



print("Você precisa pagar imposto?")

# Entrada

salario = int(input("Para descobrir, insira seu salário abaixo, utilizando apenas números: "))

# Processamento

pagarImposto = salario > 1200

# Saída 

print(pagarImposto)
