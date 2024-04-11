# Exercício 3
# Colete 3 valor ANOS, HORAS e SEGUNDOS, transformem todos em SEGUNDOS e apresente na tela

# Entrada
dias = int(input("Insira a quantidade de dias: "))
horas = int(input("Insira a quantidade de horas: "))
segundos = int(input("Insira a quantidade de segundos: "))

# Processamento 

total = (dias*60*60) + (horas*60) + segundos

# Saída 

print(f"O tempo total em segundos é de {total}s")
print("---------------------------------------")