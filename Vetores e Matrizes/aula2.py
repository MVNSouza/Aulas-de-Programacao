V = []
contador = 0 
while contador < 5:
    item = input(f"Insira um valor para a posição de índice > {contador}: ")
    V.append(item)
    contador += 1

for indice, item in enumerate(V):
    print(f"Índice {indice}: '{item}'")