# Exercício 1
def par_Ou_Impar(num):
    if num % 2 == 0:
        print(f"{num} é par")
        
    
    else:
        print(f"{num} é ímpar")
        

numero = int(input("Insira um número e descubra se é par ou ímpar: "))
par_Ou_Impar(numero)

# Exercício 2

def Maior_Numero_Entre(num1, num2):
    if num1 > num2:
        print(num1)
    else:
        print(num2)
    
Maior_Numero_Entre(7, 3)
Maior_Numero_Entre(1, 3)

# Exercício 3

def Verifica_Multiplos(multiplo, numero):
    if multiplo % numero == 0:
        return True
    else:
        return False

print(Verifica_Multiplos(10, 4))
print(Verifica_Multiplos(10, 5))

# Exercicio 4
def Area_Quadrada(lado):
    area = lado * lado
    print(f"Área igual a {area}")

Area_Quadrada(4)

# Exercício 5
def Area_Triangulo(base, altura):
    area = (base * altura)/2
    print(f"A área do triângulo é igual a {area}")
Area_Triangulo(2, 10)