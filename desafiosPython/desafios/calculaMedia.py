# Programa para calcular a média de matérias, deixando o aluno escolher quantas matérias ele quer calcular.
print("CALCULADOR DE MÉDIA")
print("")

# Criação da váriavel 'Matérias' para identificar a quantidade de matérias para se calcular a média. 
materias = int(input("Digite o número de matérias que você decide calcular: "))
print("")
# Criação de uma lista vazia, para receber os valores das notas.
notas = []

# Definição de uma variável para controlar a quantidade de repetição do código
repeticao = 1

# Etapa de coleta das notas e atribuindo à lista "notas"
while repeticao <= materias:
        novo_item = float(input("Digite uma nota: "))
        notas.append(novo_item)
        
        # Adição de mais um na repetição para identificar que o loop rodou 1 vez
        repeticao += 1
print("--"*30)
print("")
# Somar todos os itens da lista 'notas'
soma = sum(notas)

# Dividir a soma pelo número de matérias
media = soma / materias 

print(f"A média das notas {notas} é = {media}")