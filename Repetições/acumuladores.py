def pularLinha():
    print("")
    print("-"*40)
    print("")
# # Exercício 1
# contadorEx1 = 1
# acumulador = 0

# while contadorEx1 <= 3:
#     print("Insira uma nota!")
#     nota = int(input("Nota = "))
#     acumulador += nota
#     contadorEx1 += 1

# media = acumulador/3
# print(media)

# pularLinha()

# Exercício 2

# contadorEx2 = 1
# print("Calculador de impostos!")
# valorinicial = float(input("Insira o valor inicial: "))
# juros = float(input("Insira o valor dos juros: "))
# acumulador = valorinicial

# while contadorEx2 <= 24:
#     juros_Mes = (juros/100) * acumulador
#     acumulador += juros_Mes
#     print(f"Mês {contador} : Valor = {acumulador:.2f}")
#     contadorEx2 += 1

# pularLinha()
    
# Tabuada
    
contadorEx3 = 1
numeroEx3 = int(input("Veja a tabuada de um número até 10!\nInsira o número: "))

print(f"\nTABUADA DO {numeroEx3}:")

while contadorEx3 <= 10:
    resultado = contadorEx3 * numeroEx3
    print(f"{numeroEx3} x {contadorEx3} = {resultado}")
    contadorEx3 += 1