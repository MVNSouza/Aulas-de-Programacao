#Ex1
a = int(input("Insira um número: "))
b = int(input("Insira um número: "))
soma = a + b
print(f"O resultado de {a} + {b} é = {soma}")

#Ex2
PI = 3.14159
raio = float(input("Insira o valor do raio: "))
area = PI * (raio**2)
print(f"Uma circuferência de raio {raio} tem área de {area}")

#Ex3
materia1 = input("Qual a primeira matéria?: ")
nota1 = float(input("Insira a nota:  "))
peso1 = int(input("Insira o peso:   "))
print()
materia2 = input("Qual a segunda matéria?:  ")
nota2 = float(input("Insira a nota:  "))
peso2 = int(input("Insira o peso:   "))
print()
materia3 = input("Qual a terceira matéria?: ")
nota3 = float(input("Insira a nota:  "))
peso3 = int(input("Insira o peso: "))
print()

mediaPonderada = ((nota1*peso1)+(nota2+peso2)+(nota3*peso3)/(peso1+peso2+peso3))
print("Matéria:         Nota:   Peso:    ")
print(f"{materia1}  :   {nota1} | {peso1}\n{materia2} :   {nota2} | {peso2}\n{materia3} :   {nota3} | {peso3}")
print("-"*30)
print(f"Média final = {mediaPonderada}")
