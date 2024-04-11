'''
capa de livro preço 29.45
mas a livraria recebe desconto de 40%
transporte = 3 reais para o primeiro + 0.75 a cada adicional
'''

# entrada

quantidade = 60
capa = 29.45
desconto = ((capa*40)/100)*quantidade
transporte = 3+((quantidade-1)*0.75)

# processamento

custoTotal = (capa*quantidade-desconto)+transporte

# saída

print(f"O custo de varejo para {quantidade} de cópias é de R$ {custoTotal}")
