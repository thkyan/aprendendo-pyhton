# from itertools import combinations, permutations, product

# pessoas = ['thayna', 'thiago', 'lorrany', 'larice']
# # for grupo in combinations(pessoas, 2):
# #     print(grupo)

# # for grupo in permutations(pessoas):
# #     print(grupo)

# for grupo in product(pessoas, repeat=2):
#     print(grupo)

def calcular(*args):
    r = sum(1, 4, 5)
    for i in args:
        r += i
    return r
print(calcular)