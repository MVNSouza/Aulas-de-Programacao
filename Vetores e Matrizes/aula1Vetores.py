# # Exercício 1
# vetorInteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Exercício 2
# vetorCaracteres = ['M', 'A', 'R', 'C', 'O']

# # Exemplo 1

# vetorExemplo1=[0, 0, 0, 0, 0]
# contadorEx1 = 0
# while contadorEx1 < len(vetorExemplo1):
#     numero = int(input(f"Insira o {contadorEx1 + 1}º valor: "))
#     vetorExemplo1[contadorEx1] = numero
    
#     contadorEx1 += 1

# while True:
#     posicao = int(input(f"Qual posição dos números você quer analisar? [0 a {len(vetorExemplo1) - 1}]: "))
#     if posicao < 0 or posicao >= len(vetorExemplo1):
#         print("O valor inserido não é válido")
#     else:
#         print(f"O valor da posição {posicao} é: {vetorExemplo1[posicao]}")
#         break

# # Exemplo 2
# total = 0 
# contadorEx2 = 0

# while contadorEx2 < len(vetorExemplo1):
#     total += vetorExemplo1[contadorEx2]
#     contadorEx2 += 1

# print(f"A média dos resultados é: {total / len(vetorExemplo1)}")

# Exemplo 3
notaSala = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
notasRecebidas = 0
while notasRecebidas < len(notaSala):
    novaNota = float(input(f"Insira a {notasRecebidas + 1}ª nota: "))
    notaSala[notasRecebidas] = novaNota
    notasRecebidas += 1

totalNotas = 0
notasSomadas = 0
while notasSomadas < len(notaSala):
    totalNotas += notaSala[notasSomadas]
    notasSomadas += 1
 
mediaSala = totalNotas / len(notaSala)
print(f"Média da turma: {mediaSala:.1f}")
