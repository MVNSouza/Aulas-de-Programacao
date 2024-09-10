def pularLinha():
    print("")
    print("-"*40)
    print("")

while True:
    questao = int(input("Escolha a questão a ser resolvida: "))
        
    if questao == 1:
        # Exercício 1 
        contadorEx1 = 1

        while contadorEx1 <= 5:
            num = int(input("Insira um número: "))
            num = num * 3
            print(num)
            contadorEx1 += 1
        pularLinha()

    elif questao == 2:
        
        # Exercício 2 
        while True:
            continuar = str
            num = int(input("Insira um número: "))
            num = num * 3
            print(f"Resultado: {num}")
            pularLinha()

            while continuar != "ads1":
                confirmar = input("Deseja continuar calculando? [s/n]: ")
                if confirmar == "s" or confirmar == "S":
                    pularLinha()
                elif confirmar == "n" or confirmar == "N":
                    print("--- PROGRAMA ENCERRADO ---")
                    continuar = "ads1"
                else:
                    print("Opção inválida. Digite 's' ou 'n'.")
                break
            
            if continuar == "ads1":
                pularLinha()
                break
            else:
                print()
                pularLinha()
    
    elif questao == 3\

    repetir = int(input("Deseja sair? se sim, digite 1, se não, digite qualquer outro número: "))
    if repetir == 1:
        break