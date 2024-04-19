from itertools import zip_longest, count

indice = count()
cidades =  ['Sao paulo', 'belo horizonte', 'salvador', 'monte belo']
estados = ['sp', 'mg', 'ba']

cidades_estados = zip(
    indice,
    estados, 
    cidades, 
    )

# for valor in cidades_estados:
#     print(valor)

for indice, cidade, estado in cidades_estados:
    print(indice, cidade, estado)