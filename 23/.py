# l1 = [1, 2 , 3 , 4, 5, 6, 7, 8, 9]
# ex1 = [variavel for variavel in l1]
# ex2 = [v * 2 for v in l1]
# ex3 = [(v, v2) for v in l1 for v2 in range(3)]

# l2 = ['thayna', 'thiago', 'gabriel']
# ex4 = [v.replace('a','@') for v in l2] #serve para trocar um caracter especifico

# tupla = (
#     ('chave', 'valor'),
#     ('chave2', 'valor2'),
# )

# ex5 = [(y, x) for x, y in tupla]

# print(ex5)

# string = '0123456789012345678901234567890123456789'
# n = 10
# lista = [string[i:i+n] for i in range(0, len(string), n)]
# print(lista)

# retorno = '.'.join(lista)
# print(retorno)

###################################################################

# lista = [
#     ('chave', 'valor'),
#     ('chave2', 'valor2'),
# ]

# d1 = {x:y for x, y in enumerate(range(5))}
# d1 = {f'chave_{x}': x**2 for x in range(5)}
# print(d1)


#####################################################
import time
import sys


# def gera():

#     for n in range (100):
#         yield n 
#         time.sleep(0.1)
  

# g = gera()
# for v in g:
#     print(v)

lista = [x for x in range(10000)]
print(type(lista))
lista2 =(x for x in range(10000))
print(type(lista))
print(sys.getsizeof(lista))
print(sys.getsizeof(lista2))