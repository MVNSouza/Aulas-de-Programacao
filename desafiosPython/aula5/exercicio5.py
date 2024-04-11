# Exercício 5
# Crie um programa que colete o PREÇO e o DESCONTO e mostre o VALOR DO DESCONTO e o PREÇO COM DESCONTO.
# Entrada
preco = float(input("Insira o valor do preço: "))
desconto = float(input("Insira o valor do desconto: "))

# Processamento
valorDesconto = preco*(desconto/100)
valorFinal = preco - valorDesconto

# Saída
print(f"O valor de desconto é R$ {valorDesconto}, e o preço com o mesmo fica R$ {valorFinal}") 
print("---------------------------------------")