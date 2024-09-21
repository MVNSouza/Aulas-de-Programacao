def pularLinha():
    print("")
    print("-"*40)
    print("")

while True:
    questao = int(input("Escolha a questão a ser resolvida: "))

    # Questão 1    
    if questao == 1:
        # Exercício 1 
        contadorEx1 = 1

        while contadorEx1 <= 5:
            num = int(input("Insira um número: "))
            num = num * 3
            print(num)
            contadorEx1 += 1
        pularLinha()

    # Questão 2
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
    
    # Questão 3
    elif questao == 3:
        
        print("Fatorial de 5!")
        # Váriaveis
        num = 5
        proxnum = num-1

        #Início - repetição
        while proxnum > 0:
            print(f"{num} x {proxnum} = ")
            num = num * proxnum
            print(num)
            print()
            # Criar o sentido de fatorial (n * n-1 * n-2... * 1)
            proxnum -= 1
    
    # Questão 4
    elif questao == 4:
        
        # Váriaveis
        num = int(input("Digite um número e veja seu fatorial: "))
        proxnum = num-1

        #Início - repetição
        while proxnum > 0:
            print(f"{num} x {proxnum} = ")
            num = num * proxnum
            print(num)
            # Criar o sentido de fatorial (n * n-1 * n-2... * 1)
            proxnum -= 1
    
    # Questão 5
    elif questao == 5:
        num = 15 # Contador
        while num <= 200:
            print(f"Quadrado de {num}: ",num**2)
            num += 1
    
    # Questão 6
    elif questao == 6:
        num = 1 # Contador
        total = num
        while num <= 99:
            total += (num + 1)
            print(total)
            num += 1

    # Questão 7
    elif questao == 7:
        num = 1 # Contador
        total = num
        while num <= 499:
            total += (num + 1)
            print(total)
            num += 1
    
    # Questão 8
    elif questao == 8:
        num = 0
        while num < 20:
            num += 1
            if (num % 2) != 0:
                print(num) 
    
    # Questão 9
    elif questao == 9:

        base = 3 
        expoente = 0
        
        while expoente <= 15:
            potencia = 1 # Resultado nulo em multiplicação
            contador = 0 # Contador
            
            while contador < expoente:
                potencia *= base
                contador += 1 # Acréssimo ao contador
                
            print(f"{base}^{expoente} = {potencia}")
            expoente += 1 # Adição do expoente

    # Questão 10
    elif questao == 10:
        base = int(input("Digite a base: ")) 
        expoente = int(input("Digite o expoente: "))
        contador = 0
        potencia = 1
            
        while contador < expoente:
            potencia *= base
            contador += 1 # Acréssimo ao contador
                
        print(f"{base}^{expoente} = {potencia}")

    # Questão 11
    elif questao == 11:
        # Variáveis
        contador = 3
        atual = 1
        anterior = atual
        proximo = 0

        # Print inicial
        print("0")
        print(anterior)
        print(atual)
        
        while contador < 15:
            proximo = atual + anterior
            print(proximo)
            contador += 1
            anterior = atual
            atual = proximo

    # Questão 12
    elif questao == 12:
        c = 10
        f = float

        while c <= 100:
            f = c*(9/5) + 32
            print(f)
            c += 10

    # linha de teste 
    repetir = input("Deseja sair? [s/n]: ")
    if repetir == "S" or repetir == "s":
        break