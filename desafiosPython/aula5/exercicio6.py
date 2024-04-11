# Exercício 6
# Crie um programa que calcule o tempo de uma viagem de carro, utilizando a DISTÂNCIA e a VELOCIDADE MÉDIA.
# Entrada
distancia = float(input("Insira a distância percorrida em quilometros: "))
velMedia = int(input("Insira a velocidade média em KM/H: "))

# Processamento
tempo = distancia/velMedia
print("")
# Saída
print(f"Sua viagem de {distancia} metros, à {velMedia} km/h, será realizada em {tempo} horas.") 
print("---------------------------------------")