# Exercício 4
# Calcule o NOVO SALÁRIO de um funcionário depois do aumento. Para isso, colete o SALARIO ATUAL e o AUMENTO.
# Entrada
salario = float(input("Insira o valor do salário: "))
aumento = float(input("Insira a porcentagem do aumento: "))

# Processamento
novoSalario = salario + (salario*(aumento/100))

# Saída
print(f"Com o aumento, o salário de R$ {salario}, se tornará um salário de R$ {novoSalario}") 
print("---------------------------------------")