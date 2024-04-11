# Exercício 8
# Crie uma expressão que defina se um aluno foi aprovado, para ser aprovado ele precisa estar acima da média (7) em todas as 3 matérias que ele cursa.

print("Você foi aprovado? Descubra!")

# Entrada

materia1 = float(input("Insira a média da matéria 1: "))
materia2 = float(input("Insira a média da matéria 2: "))
materia3 = float(input("Insira a média da matéria 3: "))

# Processamento

media = (materia1 + materia2 + materia3)/3
aprovacao = media > 7

# Saída

print(aprovacao)