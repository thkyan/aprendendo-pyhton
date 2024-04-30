from itertools import count

# contador = count(start=5, step=-1)

# for valor in contador:
#     print(round(valor, 2))

#     if valor >= 10 or valor <= -10:
#         break

contador = count()
lista = ['thayna','thiago','lorrany']
lista = zip(contador, lista)
print(list(lista))