# Exercício 9
# Criando um programa que calcule os dias perdidos de vida por um fumante

# Entrada
cigarro = int(input("Quantos cigarros em média você fuma por dia? "))
anos = int(input("Há quantos anos você fuma? "))

# Processamento
# Para descobrir a quantidade de cigarros fumados no ano temos:
# Quantidade de cigarros por dia x 365 (Quantidade de dias no ano)
cigarroAno = cigarro*365

# Para descobrir a quantidade de cigarros fumados na vida temos:
# cigarroAno x anos (variável da quantidade de anos fumados)
totalFumado = cigarroAno*anos

# Calculando a quantidade de minutosPerdidos com a quantidade de totalFumado x 10 (quantidade estimada de minutos perdidos por cigarro.

minutosPerdidos = totalFumado*10

# Por fim, os 'minutosPerdidos' se tornam em 'vidaPerdida', que são os dias de vida perdidos.
# Resultado dos minutos de vida perdido / 1440 (Quantidade de minutos em um dia.)
vidaPerdida = minutosPerdidos/1440

# Saída
print(f"A quantidade de dias perdidos é de: {vidaPerdida}")