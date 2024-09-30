while True:
    
    questao = int(input("Qual questão você deseja acessar? [1 à 22]:  "))

    if questao == 1: 
        # ---------- Questão 1
        vetorA = []
        vetorB = []
        for i in range(10):
            numero = int(input(f"Insira o {i + 1}º número: "))
            vetorA.append(numero)
        

        for item in vetorA:
            if item % 2 == 0:
                item *= 5
                vetorB.append(item)
            
            else:
                item += 5
                vetorB.append(item)

        print(vetorA)
        print(vetorB)

    elif questao == 2:
        # -------- QUESTÃO 2
        vetorA = []
        vetorB = []
        for i in range(5):
            numero = int(input(f"Insira o {i+1}º número:  "))
            if numero % 2 == 0:
                vetorA.append(numero)
            else:
                vetorA.append(numero)
                vetorB.append(numero)
        print(f"Soma do vetor B: {sum(vetorB)}")
    
    elif questao == 3:
        # -------- QUESTÃO 3
        nomes = []

        for i in range (10):
            nome = input(f"Insira o {i+1}º nome:   ")
            nomes.append(nome)
        
        print(nomes)

    
    elif questao == 4:
        # -------- QUESTÃO 4

    
# ------- Encerramento
    print("Encerrar programa? [S/N]")
    while True:
        sair = input(":  ")
        if sair != "S" and sair != "s" and sair != "N" and sair != "n":
            print("Insira um valor válido, 'S' para 'Sim' 'N' para 'Não'.")

        else:
            break
    if sair == "S" or sair == "s":
        break