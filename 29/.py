from itertools import combinations, permutations, product

pessoas = ['thayna', 'thiago', 'lorrany', 'larice']
# for grupo in combinations(pessoas, 2):
#     print(grupo)

# for grupo in permutations(pessoas):
#     print(grupo)

for grupo in product(pessoas, repeat=2):
    print(grupo)