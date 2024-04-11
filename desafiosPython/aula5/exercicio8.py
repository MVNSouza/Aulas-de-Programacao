# Exercício 8
# Criação de um programa que calcule o total de aluguel de um carro em que: dia alugado = R$ 60,00 e Km rodado = R$ 0,15

# Entrada
km = int(input("Insira a quantidade de quilometros rodados: "))
dias = int(input("Insira a quantidade de dias: "))

# Processamento
valorKm = km * 0.15
valorDia = dias * 60
valorTotal = valorKm + valorDia

# Saída
print(f"O valor total do aluguel é de R$ {valorTotal}.")
print("---------------------------------------")
