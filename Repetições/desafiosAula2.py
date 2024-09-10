# CALCULADORA

while True:
    print('''Calculadora!
    [1] Soma
    [2] Subtração
    [3] Multiplicação
    [4] Divisão
    [0] Sair
    ''')
    
    opcao = int(input("Insira a opção:   "))
    if opcao == 0:
        print("--- FIM DO PROGRAMA ---")
        break
    
    elif opcao == 1:
        print("")
        print("SOMA!")
        num1 = float(input("Número 1: "))
        num2 = float(input("Número 2: "))
        resultado = num1 + num2
        print(f"Resultado da soma = {resultado}")
        print("")
    
    elif opcao == 2:
        print("")
        print("SUBTRAÇÃO!")
        num1 = float(input("Número 1: "))
        num2 = float(input("Número 2: "))
        resultado = num1 - num2
        print(f"Resultado da subtração = {resultado}")
        print("")
    
    elif opcao == 3:
        print("")
        print("MULTIPLICAÇÃO!")
        num1 = float(input("Número 1: "))
        num2 = float(input("Número 2: "))
        resultado = num1 * num2
        print(f"Resultado da multiplicação = {resultado}")
        print("")
    
    elif opcao == 4:
        print("")
        print("DIVISÃO!")
        num1 = float(input("Número 1: "))
        num2 = float(input("Número 2: "))
        resultado = num1 / num2
        print(f"Resultado da divisão = {resultado:.2f}")
        print("")
    
    else:
        print("OPÇÃO INVÁLIDA")